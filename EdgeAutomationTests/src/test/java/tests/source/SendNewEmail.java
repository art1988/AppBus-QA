package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.constants.Const;
import com.appbus.pages.constants.Context;
import com.appbus.pages.constants.Notifications;
import com.appbus.pages.email_related.Email;
import com.appbus.pages.helpers.Saver;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.menuItems.CommunicationsMenuItems;
import com.appbus.pages.menuItems.ServiceNavBar;
import com.appbus.pages.tabs.MailTab;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.List;
import java.util.Random;

public class SendNewEmail
{
    @Test
    public void sendNewEmail() throws InterruptedException
    {
        ActiveHamburgerMenu hamburgerMenu = new ActiveHamburgerMenu(FunctionalTest.getDriver());
        CommunicationsMenuItems commMenuItems = hamburgerMenu.clickCommunications();
        MailTab mailTab = commMenuItems.clickMail();
        Email email = mailTab.clickNewEmailButton();


        // Generate random integer as identifier [1,100]
        Random generator = new Random();
        int id = generator.nextInt(100) + 1;

        String subject = "Hello from autotest " + id + " !";

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);

        email.setToEmail(Const.LOGIN + "@" + Const.DOMAIN + ".net");
        email.setSubject(subject);

        String messageBody = "line 1\n" + "line 2\n" + "end.";
        email.setMessageBody(messageBody);

        FunctionalTest.switchContext(Context.NATIVE);
        Scroller.scrollUp();
        email.sendEmail();
        Thread.sleep(2000);

        // Save email subject
        Saver.saveEmailSubject(subject);

        // Click refresh button and wait for notification
        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);
        mailTab.clickRefreshButton();
        Thread.sleep(2000);

        FunctionalTest.switchContext(Context.NATIVE);

        System.out.println("Checking presence of notification pop-up...");
        MobileElement notificationPopup = (MobileElement)(new WebDriverWait(FunctionalTest.getDriver(), 20)).until(ExpectedConditions.visibilityOfElementLocated(By.name(Notifications.EMAIL_RECEIVED.getNotificationText())));
        Assert.assertNotNull(notificationPopup);

        Thread.sleep(2000);
        ServiceNavBar navBar = new ServiceNavBar(FunctionalTest.getDriver());
        navBar.clickNotification().clickByNotificationMessage(Notifications.EMAIL_RECEIVED);

        // Check that email is in Sent Items
        mailTab.clickSentItems();

        Thread.sleep(2000);
        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        mailTab.clickSearchButton();
        mailTab.searchText(subject); // Search sent email by subject

        FunctionalTest.switchContext(Context.NATIVE);

        // Get amount of matched emails
        List<WebElement> matched = FunctionalTest.getDriver().findElements(By.xpath("//XCUIElementTypeApplication[@name='AppBus']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[5]"));

        System.out.println("We should see only _one_ e-mail with subject = " + subject);
        System.out.println("Checking...");

        Assert.assertEquals(1, matched.size());

        System.out.println("Click by email with subject = " + subject);
        matched.get(0).click();
        Thread.sleep(2_000);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);

        System.out.println("Making sure that message body equals:\n" + messageBody);
        Assert.assertEquals(messageBody, email.getMessageBody());

        // Click <- back button
        mailTab.clickBackButton();

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2_000);
    }

}
