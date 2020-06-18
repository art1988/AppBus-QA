package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.constants.Const;
import com.appbus.pages.constants.Context;
import com.appbus.pages.contact_related.Contact;
import com.appbus.pages.email_related.AddContactOption;
import com.appbus.pages.email_related.Email;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.menuItems.CommunicationsMenuItems;
import com.appbus.pages.menuItems.ServiceNavBar;
import com.appbus.pages.tabs.ContactsTab;
import com.appbus.pages.tabs.MailTab;
import org.junit.Assert;
import org.junit.Test;

public class NewContactForMail
{
    @Test
    public void newContactForMail() throws InterruptedException
    {
        ServiceNavBar navBar = new ServiceNavBar(FunctionalTest.getDriver());
        //ActiveHamburgerMenu mm = new ActiveHamburgerMenu(FunctionalTest.getDriver()); // (2) - non-bulk run
        CommunicationsMenuItems communicationsMenuItems = navBar.clickHamburgerMenu().clickCommunications();
        //CommunicationsMenuItems communicationsMenuItems = mm.clickCommunications(); // (2) - non-bulk run

        Scroller.scrollRight("Contacts");

        ContactsTab contactsTab = communicationsMenuItems.clickContacts();

        Contact newContact = contactsTab.clickAddContact();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(8_000);

        String contactName = "张秀英 李敏 王秀英";

        newContact.setName(contactName);
        newContact.setJobTitle("经理");

        newContact.clickContactsSubtab();

        String contactEmail = "chineseWorker@junk.com";
        newContact.setEmail_1(contactEmail);

        newContact.clickAccept();

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2000);

        Scroller.scrollLeft("Mail");

        MailTab mailTab = communicationsMenuItems.clickMail();

        Email newEmail = mailTab.clickNewEmailButton();

        FunctionalTest.switchContext(Context.WEBVIEW);
        AddContactOption addContactOption = newEmail.clickPlusButtonFor(Email.Field.TO, false);

        FunctionalTest.switchContext(Context.WEBVIEW);
        addContactOption.searchFor(contactName);

        Thread.sleep(4000);

        JSExecutor.injectJQuery();

        // Find created contact and click it
        JSExecutor.clickViaJQuery("$('#contactList .item.search-contact-item .name:contains(\"" + contactName + "\")')");

        newEmail.clickPlusButtonFor(Email.Field.TO, true); // Close Add Contact popup

        System.out.println("Checking that e-mail in filed To is correct...");
        Assert.assertEquals(contactEmail, JSExecutor.getTextViaJQuery("$('.email-input.input-to .input-wrapper')"));

        newEmail.setCcEmail(Const.LOGIN + "@" + Const.DOMAIN + ".net");

        String emailSubj = "Email with new contact and cc to yourself";
        newEmail.setSubject(emailSubj);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3000);

        newEmail.sendEmail();
        Thread.sleep(4000);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3000);

        mailTab.clickRefreshButton();
        Thread.sleep(3000);

        mailTab.clickSearchButton();
        mailTab.searchText(emailSubj);

        // Click by email via found subject
        JSExecutor.clickViaJQuery("$('.email-list-scroller__message-item .email-list-scroller__message-content .email-list-scroller__message-subject:contains(\"" + emailSubj + "\")')");
        Thread.sleep(10000);

        System.out.println("Checking that TO filed has email address = " + contactEmail);
        Assert.assertEquals(contactEmail, JSExecutor.getTextViaJQuery("$('.addres-body div:contains(\"TO\")')").substring(2));

        System.out.println("Delete this email...");
        mailTab.clickDeleteSingleEmailButton().clickOk();

        FunctionalTest.switchContext(Context.NATIVE);

        Scroller.scrollRight("Contacts");
        contactsTab = communicationsMenuItems.clickContacts();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        Contact chineseWorkerContact = contactsTab.clickContactByName(contactName);
        Thread.sleep(2000);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        System.out.println("Delete chinese worker contact from Contacts folder...");
        chineseWorkerContact.clickDelete().confirmDelete();

        contactsTab.clickDeletedItems();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        chineseWorkerContact = contactsTab.clickContactByName(contactName);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        System.out.println("Trying to delete chinese worker contact completely from Deleted Items folder...");
        chineseWorkerContact.clickDelete().confirmDelete();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        Assert.assertEquals("", JSExecutor.getTextViaJQuery("$('.contact-card__title:contains(\"" + contactName + "\")')"));

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2000);

        Scroller.scrollLeft("Accenture Portal");
    }
}
