package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.constants.Context;
import com.appbus.pages.helpers.Saver;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.popups.DeleteEmailPopup;
import com.appbus.pages.tabs.MailTab;
import io.appium.java_client.MobileElement;
import org.junit.Test;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.List;

public class DeleteEmail
{
    @Test
    public void deleteEmail() throws InterruptedException
    {
        MailTab mailTab = new MailTab(FunctionalTest.getDriver());

        FunctionalTest.switchContext(Context.WEBVIEW);

        // Select email
        MobileElement selectEmailCheckBox = (MobileElement) FunctionalTest.getDriver().findElement(By.className("icon-icon_unchecked"));

        selectEmailCheckBox.click();

        DeleteEmailPopup deleteEmailPopup = mailTab.clickDeleteEmailButton();

        System.out.println("Check that we see Delete selected message pop up...");
        Assert.assertEquals("Delete selected messages?", deleteEmailPopup.getTitle());

        deleteEmailPopup.clickOk();

        MobileElement noMessagesText = (MobileElement) (new WebDriverWait(FunctionalTest.getDriver(), 25)).until(ExpectedConditions.presenceOfElementLocated(By.name("No messages for current folder")));
        System.out.println("Check that label 'No messages...' appear...");
        Assert.assertEquals("No messages for current folder", noMessagesText.getText());

        mailTab.clickDeletedItems();

        // Get amount of matched emails
        //List matched = FunctionalTest.getDriver().findElements(By.xpath("//XCUIElementTypeApplication[@name='AppBus']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[5]"));
        MobileElement email = (MobileElement) FunctionalTest.getDriver().findElement(By.name(Saver.getEmailSubject()));

        Thread.sleep(4000);

        System.out.println("We should see only _one_ e-mail with subject = " + Saver.getEmailSubject());
        System.out.println("Checking...");

        Assert.assertEquals(Saver.getEmailSubject(), email.getText());

        Thread.sleep(2000);

        FunctionalTest.switchContext(Context.WEBVIEW);

        mailTab.clickSearchButton();
    }
}
