package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.constants.Context;
import com.appbus.pages.constants.Gender;
import com.appbus.pages.contact_related.Contact;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.menuItems.CommunicationsMenuItems;
import com.appbus.pages.menuItems.ServiceNavBar;
import com.appbus.pages.tabs.ContactsTab;
import org.junit.Assert;
import org.junit.Test;

public class Contacts
{
    @Test
    public void contacts() throws InterruptedException
    {
        ServiceNavBar navBar = new ServiceNavBar(FunctionalTest.getDriver()); // (1) - bulk test run
        ActiveHamburgerMenu hamburgerMenu = navBar.clickHamburgerMenu(); // (1)
                                            //new ActiveHamburgerMenu(FunctionalTest.getDriver()); // (2) - non-bulk
        CommunicationsMenuItems commMenuItems = hamburgerMenu.clickCommunications();

        Scroller.scrollRight("Contacts");

        ContactsTab contactsTab = commMenuItems.clickContacts();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(3000);

        int numOfContacts = contactsTab.getCounter();
        System.out.println("Current num of contacts : " + numOfContacts);
        FunctionalTest.switchContext(Context.NATIVE);

        Contact newContact = contactsTab.clickAddContact();


        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(5000);

        String name       = "Nicole Prascovia Elikolani Valiente Scherzinger",
               job        = "Photographic Processing Machine Operator",
               company    = "Häagen-Dazs",
               department = "Institute for Social, Behavioral and Economic Research",
               birthday   = "1979-04-23";

        newContact.setName(name);
        newContact.setJobTitle(job);
        newContact.setCompany(company);
        newContact.setDepartment(department);
        newContact.setBirthday(birthday);

        Thread.sleep(1000);
        newContact.clickContactsSubtab();

        String businessPhone = "1.855.558.2436",
               mobilePhone   = "1-541-754-3010",
               homePhone     = "+49 2345 55776",
               website       = "http://www.myverygoodsite.com/",
               email1        = "email1@myverygoodsite.com",
               email2        = "email2@junk.org",
               email3        = "email3@gmail.com",
               imid          = "823 FT";

        newContact.setBusinessPhone(businessPhone);
        newContact.setMobilePhone(mobilePhone);
        newContact.setHomePhone(homePhone);
        newContact.setWebsite(website);
        newContact.setEmail_1(email1);
        newContact.setEmail_2(email2);
        newContact.setEmail_3(email3);
        newContact.setIMID(imid);

        Thread.sleep(1000);
        newContact.clickAddressSubtab();

        String work_street  = "E 46th Street",
               work_city    = "New York",
               work_state   = "New Jersey",
               work_postal  = "10017",
               work_country = "USA";

        newContact.setWorkStreet(work_street);
        newContact.setWorkCity(work_city);
        newContact.setWorkState(work_state);
        newContact.setWorkPostalCode(work_postal);
        newContact.setWorkCountry(work_country);

        String home_street  = "Gorwin Drive",
               home_city    = "Medway",
               home_state   = "MA",
               home_postal  = "02053",
               home_counrty = "US";

        newContact.setHomeStreet(home_street);
        newContact.setHomeCity(home_city);
        newContact.setHomeState(home_state);
        newContact.setHomePostalCode(home_postal);
        newContact.setHomeCountry(home_counrty);

        Thread.sleep(1000);
        newContact.clickMoreSubtab();

        String languages = "English, German, Chinese",
               hobbies   = "Cars, Books; knitting",
               gender    = Gender.female.name();

        newContact.setLanguage(languages);
        newContact.setHobbies(hobbies);
        newContact.setGender(gender);

        Scroller.scrollUp();
        newContact.clickAccept();

        Thread.sleep(3000);

        System.out.println("Make sure that amount of contacts were increased +1...");
        Assert.assertEquals(numOfContacts + 1, contactsTab.getCounter());

        JSExecutor.injectJQuery();

        // Refresh number of Contacts counter
        numOfContacts = contactsTab.getCounter();
        Thread.sleep(4_000);

        int numOfDeletedContacts = 0; // Number of Deleted Items before deletion
        if( JSExecutor.getTextViaJQuery("$('.contacts-folders-list .contacts-folders-list__folder-name:contains(\"Deleted Items\")').next()").equals("") == false )
        {
            numOfDeletedContacts =  Integer.valueOf(JSExecutor.getTextViaJQuery("$('.contacts-folders-list .contacts-folders-list__folder-name:contains(\"Deleted Items\")').next()"));
        }

        contactsTab.switchToVerticalView();
        Thread.sleep(2000);

        // Find just created contact and click it
        JSExecutor.clickViaJQuery("$('.contacts-list-wrapper .contacts-list-wrapper__contact-name:contains(\"" + name + "\")')");

        System.out.println("Trying to delete selected contact...");
        newContact.clickDelete().confirmDelete();

        Thread.sleep(2000);
        FunctionalTest.switchContext(Context.WEBVIEW);

        contactsTab.switchToTileView();
        Thread.sleep(2000);

        System.out.println("Make sure that amount of contacts = " + (--numOfContacts));
        Assert.assertEquals(numOfContacts, contactsTab.getCounter());

        FunctionalTest.switchContext(Context.NATIVE);
        // Select Deleted Items
        contactsTab.clickDeletedItems();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        System.out.println("Make sure that amount of deleted contacts were increased +1...");
        Assert.assertEquals(numOfDeletedContacts + 1, contactsTab.getCounter());

        // Click created contact in Deleted Items Section
        contactsTab.clickContactByName(name);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        int numOfSuggestedBefore = 0; // Number of suggested contacts
        if( JSExecutor.getTextViaJQuery("$('.contacts-folders-list .contacts-folders-list__folder-name:contains(\"Suggested\")').next()").equals("") == false )
        {
            numOfSuggestedBefore = Integer.parseInt(JSExecutor.getTextViaJQuery("$('.contacts-folders-list .contacts-folders-list__folder-name:contains(\"Suggested\")').next()"));
        }

        // Move it to Suggested Contacts
        newContact.clickMove().moveToSuggestedContacts();

        FunctionalTest.switchContext(Context.NATIVE);
        contactsTab.clickSuggestedContacts();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);
        System.out.println("Make sure that amount of Suggested Contacts were increased +1...");
        Assert.assertEquals(numOfSuggestedBefore + 1, contactsTab.getCounter());

        // Click this contact again
        contactsTab.clickContactByName(name);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        // Delete it completely from Deleted Items section
        newContact.clickDelete().confirmDelete();

        contactsTab.clickDeletedItems();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        newContact = contactsTab.clickContactByName(name);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        System.out.println("*** Asserting that contact saves all it's fields... ***");

        // Assertion block of all fields of all subtabs of selected contact
        // By default Profile subtab opens first -> check it first
        Assert.assertEquals(name, newContact.getName());
        Assert.assertEquals(job, newContact.getJobTitle());
        Assert.assertEquals(company, newContact.getCompany());
        Assert.assertEquals(department, newContact.getDepartment());
        Assert.assertEquals(birthday, newContact.getBirthday());

        newContact.clickContactsSubtab();
        Thread.sleep(1_000);

        Assert.assertEquals(businessPhone, newContact.getBusinessPhone());
        Assert.assertEquals(mobilePhone, newContact.getMobilePhone());
        Assert.assertEquals(homePhone, newContact.getHomePhone());
        Assert.assertEquals(website, newContact.getWebsite());
        Assert.assertEquals(email1, newContact.getEmail_1());
        Assert.assertEquals(email2, newContact.getEmail_2());
        Assert.assertEquals(email3, newContact.getEmail_3());
        Assert.assertEquals(imid, newContact.getIMID());

        newContact.clickAddressSubtab();
        Thread.sleep(1_000);

        Assert.assertEquals(work_street, newContact.getWorkStreet());
        Assert.assertEquals(work_city, newContact.getWorkCity());
        Assert.assertEquals(work_state, newContact.getWorkState());
        Assert.assertEquals(work_postal, newContact.getWorkPostalCode());
        Assert.assertEquals(work_country, newContact.getWorkCountry());

        Assert.assertEquals(home_street, newContact.getHomeStreet());
        Assert.assertEquals(home_city, newContact.getHomeCity());
        Assert.assertEquals(home_state, newContact.getHomeState());
        Assert.assertEquals(home_postal, newContact.getHomePostalCode());
        Assert.assertEquals(home_counrty, newContact.getHomeCountry());

        newContact.clickMoreSubtab();
        Thread.sleep(1_000);

        /*    Is not implemented yet, see: ED-3257
        Assert.assertEquals(languages, newContact.getLanguage());
        Assert.assertEquals(hobbies, newContact.getHobbies());
        Assert.assertEquals(gender, newContact.getGender());
        */

        System.out.println("Trying to delete this contact completely from Deleted Items section...");
        newContact.clickDelete().confirmDelete();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4000);

        // Making sure that counter is OK
        Assert.assertEquals(numOfDeletedContacts, contactsTab.getCounter());
        // Making sure that we do not see 'Nicole Prascovia' contact anymore
        Assert.assertEquals("", JSExecutor.getTextViaJQuery("$('.contact-card .contact-card__title:contains(\"" + name + "\")')"));

        // Click contacts
        JSExecutor.clickViaJQuery("$('.contacts-folders-list .contacts-folders-list__folder-item').first()");

        FunctionalTest.switchContext(Context.NATIVE);
    }
}
