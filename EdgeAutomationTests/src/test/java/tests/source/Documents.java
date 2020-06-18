package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.constants.Notifications;
import com.appbus.pages.menuItems.ServiceNavBar;
import com.appbus.pages.tabs.SharePointTab;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class Documents
{

    @Test
    public void documents() throws InterruptedException
    {
        ActiveHamburgerMenu hamburgerMenu = new ActiveHamburgerMenu(FunctionalTest.getDriver());

        SharePointTab sharePointTab = hamburgerMenu.clickDocuments().clickSharePoint();

        sharePointTab.clickFirstFolder();

        Thread.sleep(2000);

        sharePointTab.clickDocxFile();
        Assert.assertTrue(FunctionalTest.getDriver().findElement(By.name("App Review Questionnaire")).isDisplayed());

        sharePointTab.clickXlsxFile();
        Assert.assertTrue(FunctionalTest.getDriver().findElement(By.name("CCAR Results")).isDisplayed());

        Thread.sleep(2000);

        System.out.println("Trying to download selected document...");
        sharePointTab.getSubmenu().clickDownload();

        System.out.println("Checking presence of notification pop-up...");
        MobileElement notificationPopup = (MobileElement)(new WebDriverWait(FunctionalTest.getDriver(), 25)).until(ExpectedConditions.visibilityOfElementLocated(By.name(Notifications.DOCUMENT_DOWNLOADED.getNotificationText())));
        Assert.assertNotNull(notificationPopup);

        ServiceNavBar navBar = new ServiceNavBar(FunctionalTest.getDriver());
        navBar.clickNotification().clickByNotificationMessage(Notifications.DOCUMENT_DOWNLOADED);

        System.out.println("Make sure that xlsx file is saved...");
        MobileElement savedLabel = (MobileElement)(new WebDriverWait(FunctionalTest.getDriver(), 10)).until(ExpectedConditions.visibilityOfElementLocated(By.name("Saved")));
        Assert.assertNotNull(savedLabel); // Make sure that we see Saved label
        Assert.assertTrue(sharePointTab.isDeviceSelected()); // Make sure that Device button is selected

        // Make sure that file is saved
        MobileElement savedFile = (MobileElement) FunctionalTest.getDriver().findElement(By.name("Report1.xlsx"));
        Assert.assertEquals("Report1.xlsx", savedFile.getText());

        Thread.sleep(2000);

        sharePointTab.clickCloud();

        Thread.sleep(2000);

        sharePointTab.clickPdfFile();
        String xpathOfPdfContent = "//XCUIElementTypeApplication[@name='AppBus']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]";
        Assert.assertTrue(FunctionalTest.getDriver().findElement(By.xpath(xpathOfPdfContent)).isDisplayed());

        sharePointTab.getSubmenu().clickDownload(); // Download pdf file

        sharePointTab.clickDevice();

        MobileElement savedFolder = (MobileElement) FunctionalTest.getDriver().findElement(By.name("Saved"));
        savedFile.click();

        System.out.println("Make sure that pdf file is saved...");
        savedFile = (MobileElement) FunctionalTest.getDriver().findElement(By.name("11111.pdf"));
        Assert.assertEquals("11111.pdf", savedFile.getText());

        Thread.sleep(1000);

        savedFile = (MobileElement) FunctionalTest.getDriver().findElement(By.name("Report1.xlsx"));
        sharePointTab.getSubmenu().clickDelete().clickYes(); // Delete selected document

        Thread.sleep(2000);

        try
        {
            savedFile = (MobileElement) FunctionalTest.getDriver().findElement(By.name("Report1.xlsx"));
        }
        catch( NoSuchElementException ex )
        {
            System.out.println("NoSuchElementException: Report.xlsx can't be found ! [OK]");
        }

        Thread.sleep(4000);

        navBar = new ServiceNavBar(FunctionalTest.getDriver());
        navBar.clickHamburgerMenu();
    }
}
