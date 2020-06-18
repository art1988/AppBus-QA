package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.LoginPage;
import com.appbus.pages.constants.Const;
import com.appbus.pages.constants.Context;
import com.appbus.pages.event_related.EventInviteesOption;
import com.appbus.pages.event_related.EventPreview;
import com.appbus.pages.event_related.NewEvent;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.menuItems.CommunicationsMenuItems;
import com.appbus.pages.menuItems.ServiceNavBar;
import com.appbus.pages.tabs.CalendarTab;
import com.appbus.pages.tabs.MailTab;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.List;

// Note: EXADEL contact should exists in Contacts before executing of this test
public class Invitees
{
    @Test
    public void invitees() throws InterruptedException
    {
        //ActiveHamburgerMenu hamburgerMenu = new ActiveHamburgerMenu(FunctionalTest.getDriver()); // (1) - single run
        //CommunicationsMenuItems commMenuItems = hamburgerMenu.clickCommunications();             // (1)

        ServiceNavBar serviceNavBar = new ServiceNavBar(FunctionalTest.getDriver()); // (2) - bulk run
        ActiveHamburgerMenu hamburgerMenu = serviceNavBar.clickHamburgerMenu();      // (2)
        CommunicationsMenuItems commMenuItems = hamburgerMenu.clickCommunications(); // (2)

        Scroller.scrollRight("Calendar");

        CalendarTab calendarTab = commMenuItems.clickCalendar();
        calendarTab.clickToday();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3_000);

        NewEvent newEvent = calendarTab.clickNewEvenButton();

        String eventTitle = "! invitees_TEST",
               notesMessage = "This is invitees test";

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3_000);

        newEvent.setTitle(eventTitle);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3_000);

        EventInviteesOption eventInviteesOption = newEvent.clickInviteesLabel();

        eventInviteesOption.selectInviteeByName("EXADEL");
        eventInviteesOption.clickAccept();
        eventInviteesOption.clickAccept();

        newEvent.setNotes(notesMessage);

        newEvent.clickAccept();

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3_000);

        System.out.println("*** Event with invitee was created ***");
        System.out.println("Making sure that there is no email for organizer...");

        Scroller.scrollLeft("Mail");

        MailTab mailTab = commMenuItems.clickMail();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3_000);

        mailTab.clickRefreshButton();
        mailTab.clickSearchButton();
        Thread.sleep(3_000);
        mailTab.searchText(eventTitle);
        Thread.sleep(3_000);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3_000);

        MobileElement noMessagesText = (MobileElement) (new WebDriverWait(FunctionalTest.getDriver(), 25)).until(ExpectedConditions.presenceOfElementLocated(By.name("No messages for current folder")));
        System.out.println("Check that label 'No messages...' appear...");
        Assert.assertEquals("No messages for current folder", noMessagesText.getText());

        System.out.println("*** Now, login with exadel1 user... ***");

        serviceNavBar = new ServiceNavBar(FunctionalTest.getDriver());

        hamburgerMenu = serviceNavBar.clickHamburgerMenu();
        LoginPage loginPage = hamburgerMenu.clickLogout();

        loginPage.enterUser(Const.EXADEL_USER);
        loginPage.enterPassword(Const.EXADEL_PSWD);

        hamburgerMenu = loginPage.logon();
        commMenuItems = hamburgerMenu.clickCommunications(true);

        System.out.println("Making sure that email is in Inbox for exadel invitee...");

        mailTab = commMenuItems.clickMail();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3_000);

        mailTab.clickSearchButton();
        Thread.sleep(3_000);
        mailTab.searchText(eventTitle);
        Thread.sleep(3_000);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3_000);

        // Get amount of matched emails
        List<WebElement> matched = FunctionalTest.getDriver().findElements(By.xpath("//XCUIElementTypeApplication[@name='AppBus']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[5]"));

        System.out.println("We should see only _one_ e-mail with title = " + eventTitle);
        System.out.println("Checking...");

        Assert.assertEquals(1, matched.size());

        System.out.println("Click by email with subject = " + eventTitle);
        matched.get(0).click();
        Thread.sleep(2_000);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);

        // TODO: in the future buttons Accept/Decline will be added - check it's presence
        System.out.println("Making sure that message body = You are invited to the event");
        Assert.assertEquals("You are invited to the event", FunctionalTest.getDriver().executeScript("return document.getElementById('message-content-iframe').contentWindow.document.body.innerText;"));

        // Delete selected email
        mailTab.clickDeleteSingleEmailButton().clickOk();

        Scroller.scrollRight("Calendar");

        calendarTab = commMenuItems.clickCalendar();
        calendarTab.clickToday();

        MobileElement eventWithInvitee = CalendarTab.findEventByName(eventTitle);
        Assert.assertNotNull(eventWithInvitee);

        eventWithInvitee.click();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3_000);

        EventPreview eventPreview = new EventPreview();

        Assert.assertTrue(eventPreview.getEventNotes().contains(notesMessage));

        newEvent = eventPreview.clickEditEvent();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3_000);

        System.out.println("Checking that all fields are disabled except 3: Alert, Invitees and Color...");

        Assert.assertTrue((Boolean) FunctionalTest.getDriver().executeScript("return $('.edit-info #appointmentTitle').parent().hasClass(\"disabled\")"));
        Assert.assertTrue((Boolean) FunctionalTest.getDriver().executeScript("return $('.edit-info #appointmentLocation').parent().hasClass(\"disabled\")"));
        Assert.assertTrue(isFieldDisable("Timezone") && isFieldDisable("All-day") && isFieldDisable("Starts") && isFieldDisable("Ends") && isFieldDisable("Repeat"));

        Assert.assertFalse(isFieldDisable("Alert") && isFieldDisable("Invitees") && isFieldDisable("Color"));

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3_000);

        eventInviteesOption = newEvent.clickInviteesLabel();

        System.out.println("Assert that there are only 2 invitees...");
        Assert.assertEquals("2", String.valueOf(FunctionalTest.getDriver().executeScript("return $('.edit-info .invitees-item').length")));

        System.out.println("Assert that qadev has organizer label...");
        Assert.assertEquals("qadev@botf03.netorganizer", JSExecutor.getTextViaJQuery("$('.edit-info .title .inviteesEmail:contains(\"qadev\")')"));

        eventInviteesOption.clickClose();

        newEvent.clickDelete(false).delete(true);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3_000);

        Assert.assertNull(CalendarTab.findEventByName(eventTitle));

        System.out.println("*** Login back as qadev and check that decline email is in Inbox ***");

        hamburgerMenu = serviceNavBar.clickHamburgerMenu();
        loginPage = hamburgerMenu.clickLogout();

        loginPage.enterUser(Const.LOGIN);
        loginPage.enterPassword(Const.PASSWORD);

        hamburgerMenu = loginPage.logon();
        commMenuItems = hamburgerMenu.clickCommunications();

        mailTab = commMenuItems.clickMail();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3_000);

        mailTab.clickSearchButton();
        Thread.sleep(3_000);
        mailTab.searchText("Declined: " + eventTitle);
        Thread.sleep(3_000);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3_000);

        // Get amount of matched emails
        matched = FunctionalTest.getDriver().findElements(By.xpath("//XCUIElementTypeApplication[@name='AppBus']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[5]"));

        System.out.println("We should see only _one_ declined e-mail");
        System.out.println("Checking...");

        Assert.assertEquals(1, matched.size());

        // Click by declined email
        matched.get(0).click();
        Thread.sleep(2_000);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);

        // Delete declined email
        mailTab.clickDeleteSingleEmailButton().clickOk();

        Scroller.scrollRight("Calendar");

        calendarTab = commMenuItems.clickCalendar();
        calendarTab.clickToday();

        CalendarTab.findEventByName(eventTitle).click();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3_000);

        eventPreview = new EventPreview();
        eventPreview.clickDeleteEvent(false).delete(true);

        Thread.sleep(2_000);

        Assert.assertNull(CalendarTab.findEventByName(eventTitle));

        Scroller.scrollLeft("Mail");
        mailTab = commMenuItems.clickMail();
    }

    private boolean isFieldDisable(String fieldTitle)
    {
        return (boolean) FunctionalTest.getDriver().executeScript("return $('.edit-info .field .title:contains(\"" + fieldTitle + "\")').parent().hasClass(\"disabled\")");
    }

}
