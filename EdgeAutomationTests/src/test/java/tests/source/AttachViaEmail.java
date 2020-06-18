package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.email_related.Email;
import com.appbus.pages.constants.Const;
import com.appbus.pages.constants.Context;
import com.appbus.pages.constants.Notifications;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.menuItems.AttachmentSubmenu;
import com.appbus.pages.menuItems.CommunicationsMenuItems;
import com.appbus.pages.menuItems.ServiceNavBar;
import com.appbus.pages.tabs.MailTab;
import com.appbus.pages.tabs.SharePointTab;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.Random;

public class AttachViaEmail
{
    @Test
    public void attachViaEmail() throws InterruptedException
    {
        ActiveHamburgerMenu activeHamburgerMenu = new ActiveHamburgerMenu(FunctionalTest.getDriver());
        CommunicationsMenuItems commMenuItems = activeHamburgerMenu.clickCommunications();
        MailTab mailTab = commMenuItems.clickMail();

        Email newEmail = mailTab.clickNewEmailButton();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3_000);

        newEmail.setToEmail(Const.LOGIN + "@" + Const.DOMAIN + ".net");

        // Generate random integer as identifier [1,100]
        Random generator = new Random();
        int id = generator.nextInt(100) + 1;

        String emailSubject = "Attach via email " + id;
        newEmail.setSubject(emailSubject);

        SharePointTab sharePointTab = newEmail.clickAttachFile().clickSharePoint();
        sharePointTab.clickFirstFolder();

        sharePointTab.clickXlsxFile();
        sharePointTab.confirmAttach();

        System.out.println("Make sure that we see added Attachments field...");
        Assert.assertTrue(newEmail.isAttachmentsLabelVisible());

        System.out.println("Make sure that *.xlsx file was attached...");
        Assert.assertTrue(sharePointTab.isXlsxVisible());

        FunctionalTest.switchContext(Context.WEBVIEW);

        sharePointTab = newEmail.clickAttachFile().clickSharePoint();
        sharePointTab.clickFirstFolder();

        Scroller.pullDownToShowSearchFiled();

        sharePointTab.searchFor("pdf");
        sharePointTab.clickPdfFile();
        sharePointTab.confirmAttach();

        System.out.println("Make sure that *.pdf file was attached...");
        Assert.assertTrue(sharePointTab.isPdfVisible());

        newEmail.sendEmail();
        Thread.sleep(2000);

        FunctionalTest.switchContext(Context.WEBVIEW);

        mailTab.clickRefreshButton();
        Thread.sleep(2000);

        mailTab.clickSearchButton();
        mailTab.searchText(emailSubject);

        JSExecutor.injectJQuery();

        System.out.println("Checking that received email has attach icon...");
        Assert.assertTrue((Boolean) FunctionalTest.getDriver().executeScript("return $(\".email-list-scroller__date-and-attachments i\").hasClass(\"icon-icon_editor_attach\")"));

        // Click received email
        JSExecutor.clickByElementByClassName("icon-icon_editor_attach");

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2000);

        Assert.assertTrue(sharePointTab.isXlsxVisible());
        Assert.assertTrue(sharePointTab.isPdfVisible());

        System.out.println("Checking that xlsx file can be opened...");
        sharePointTab.clickXlsxFile();
        Assert.assertTrue(FunctionalTest.getDriver().findElement(By.name("CCAR Results")).isDisplayed());

        AttachmentSubmenu attachmentSubmenu = new AttachmentSubmenu(FunctionalTest.getDriver());
        attachmentSubmenu.clickBack();

        System.out.println("Checking that pdf file can be opened...");
        sharePointTab.clickPdfFile();
        Thread.sleep(5000);

        MobileElement pdfContent = (MobileElement) FunctionalTest.getDriver().findElement(By.xpath("//XCUIElementTypeApplication[@name=\"AppBus\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther"));
        Assert.assertTrue(pdfContent.isDisplayed());

        attachmentSubmenu.clickBack();

        sharePointTab.clickXlsxFile();
        attachmentSubmenu.clickDownload();

        System.out.println("Checking presence of notification pop-up...");
        MobileElement notificationPopup = (MobileElement)(new WebDriverWait(FunctionalTest.getDriver(), 15)).until(ExpectedConditions.visibilityOfElementLocated(By.name(Notifications.DOCUMENT_DOWNLOADED.getNotificationText())));
        Assert.assertNotNull(notificationPopup);

        ServiceNavBar navBar = new ServiceNavBar(FunctionalTest.getDriver());
        navBar.clickNotification().clickByNotificationMessage(Notifications.DOCUMENT_DOWNLOADED);

        System.out.println("Making sure that Attachments label is visible...");
        Assert.assertTrue(FunctionalTest.getDriver().findElement(By.name("Attachments")).isDisplayed());

        Assert.assertTrue(sharePointTab.isDeviceSelected()); // Make sure that Device button is selected
        Assert.assertTrue(FunctionalTest.getDriver().findElement(By.name("CCAR Results")).isDisplayed()); // Make sure that we see file contents

        Thread.sleep(5000);
    }
}
