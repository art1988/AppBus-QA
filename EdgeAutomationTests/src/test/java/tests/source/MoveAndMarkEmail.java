package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.constants.Context;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.helpers.Saver;
import com.appbus.pages.menuItems.CommunicationsMenuItems;
import com.appbus.pages.tabs.MailTab;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;

public class MoveAndMarkEmail
{
    @Test
    public void moveAndMarkEmail() throws InterruptedException
    {
        //ActiveHamburgerMenu hamburgerMenu = new ActiveHamburgerMenu(FunctionalTest.getDriver());
        //CommunicationsMenuItems commMenuItems = hamburgerMenu.clickCommunications();
        //MailTab mailTab = commMenuItems.clickMail();
        MailTab mailTab = new MailTab(FunctionalTest.getDriver());   //(1) - bulk test run

        mailTab.clickDeletedItems();

        // Select 2 emails in prev. steps
        FunctionalTest.switchContext(Context.WEBVIEW);
        JSExecutor.injectJQuery();

        int numOfUnreadBefore = 0; // Number of unread e-mails of Deleted Items
        if( JSExecutor.getTextViaJQuery("$('#emailFolders .folder-name:contains(\"Deleted Items\") + span > .label')").equals("") == false )
        {
            numOfUnreadBefore = Integer.parseInt(JSExecutor.getTextViaJQuery("$('#emailFolders .folder-name:contains(\"Deleted Items\") + span > .label')"));
        }

        System.out.println("Number of unread emails in [Deleted Items] _before_ = " + numOfUnreadBefore);

        mailTab.clickSearchButton();
        Thread.sleep(2000);

        mailTab.searchText(Saver.getDraftEmailSubject()); // search for draft email from DraftEmail test
        Thread.sleep(4000);

        // Select email
        JSExecutor.clickViaJQuery("$('.email-list-scroller__check-button')");
        Thread.sleep(2000);

        mailTab.clearSearchFiled();
        Thread.sleep(4000);

        mailTab.searchText(Saver.getEmailSubject()); // search for email from SendNewEmail test
        Thread.sleep(4000);

        JSExecutor.clickViaJQuery("$('.email-list-scroller__check-button')");
        Thread.sleep(2000);

        mailTab.clearSearchFiled(); // Clear search field
        mailTab.clickSearchButton(); // Close search field

        Thread.sleep(4000);
        mailTab.clickMoreButton().markAsUnread();
        Thread.sleep(7000);

        int numOfUnreadAfter = Integer.parseInt(JSExecutor.getTextViaJQuery("$('#emailFolders .folder-name:contains(\"Deleted Items\") + span > .label')"));

        System.out.println("Number of unread emails in [Deleted Items] _after_ = " + numOfUnreadAfter);
        System.out.println("Making sure that unread counter of Deleted Items is correct...");
        Assert.assertEquals(numOfUnreadBefore + 2, numOfUnreadAfter);

        int numOfJunkBefore = 0; // Number of unread e-mails of Junk E-Mail
        if( JSExecutor.getTextViaJQuery("$('#emailFolders .folder-name:contains(\"Junk\") + span > .label')").equals("") == false )
        {
            numOfJunkBefore = Integer.parseInt(JSExecutor.getTextViaJQuery("$('#emailFolders .folder-name:contains(\"Junk\") + span > .label')"));
        }

        System.out.println("Number of unread emails in [Junk E-Mail] _before_ = " + numOfJunkBefore);

        mailTab.clickMoveButton().moveToJunk();
        Thread.sleep(2000);

        int numOfJunkAfter = Integer.parseInt(JSExecutor.getTextViaJQuery("$('#emailFolders .folder-name:contains(\"Junk\") + span > .label')"));

        System.out.println("Number of unread emails in [Junk E-Mail] _after_ = " + numOfJunkAfter);
        System.out.println("Making sure that unread counter of Junk E-Mail is correct...");
        Assert.assertEquals(numOfJunkBefore + 2, numOfJunkAfter);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2000);

        mailTab.clickJunk();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);

        mailTab.checkSelectAllCheckbox();
        mailTab.clickMoreButton().markAsRead();

        Thread.sleep(4000);

        System.out.println("Making sure that unread counter of Junk E-Mail = 0");
        Assert.assertEquals("", JSExecutor.getTextViaJQuery("$('#emailFolders .folder-name:contains(\"Junk\") + span > .label')"));

        mailTab.uncheckSelectAllCheckbox();
        Thread.sleep(2000);
        mailTab.clickSearchButton();
        Thread.sleep(2000);
        mailTab.searchText(Saver.getEmailSubject());
        Thread.sleep(4000);

        // Select email
        JSExecutor.clickViaJQuery("$('.email-list-scroller__check-button')");
        Thread.sleep(4000);

        mailTab.clickMoreButton().markAsImportant();
        mailTab.clearSearchFiled();

        mailTab.clickMoveButton().moveToInbox();

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(4000);

        mailTab.clickInbox();
        Thread.sleep(4000);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);

        mailTab.searchText(Saver.getEmailSubject());

        System.out.println("Making sure that email is still marked as important...");
        Assert.assertTrue((Boolean) FunctionalTest.getDriver().executeScript("return $('.email-list-scroller__message-item .icon-icon_flag').hasClass(\"flag-red\")"));

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(5000);
    }
}
