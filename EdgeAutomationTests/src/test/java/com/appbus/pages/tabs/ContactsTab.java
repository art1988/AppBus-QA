package com.appbus.pages.tabs;

import com.appbus.pages.contact_related.Contact;
import com.appbus.pages.PageObject;
import com.appbus.pages.constants.Context;
import com.appbus.pages.helpers.JSExecutor;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;
import tests.source.FunctionalTest;

public class ContactsTab extends PageObject
{
    @FindBy(name = "ADD CONTACT")
    private MobileElement addContact;

    @FindBy(name = "Suggested Contacts")
    private MobileElement suggestedContacts;

    @FindBy(name = "Deleted Items")
    private MobileElement deletedItems;

    /**
     * Non-native elements
     */
    private static final String class_CounterOfSelectedTab = "contacts-folders-list__folder-counter_selected",
                                class_SwitchToVerticalView = "icon-icon_cubes_4",
                                class_SwitchToTileView     = "icon-icon_cubes_3";


    public ContactsTab(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return (addContact.isDisplayed() & suggestedContacts.isDisplayed());
    }

    public Contact clickAddContact()
    {
        addContact.click();
        System.out.println("Add contact was clicked");

        return new Contact(driver);
    }

    public Contact clickContactByName(String contactName)
    {
        JSExecutor.clickViaJQuery("$('.contact-card__title:contains(\"" + contactName + "\")')");
        System.out.println("Contact with name = " + contactName + " was selected");

        FunctionalTest.switchContext(Context.NATIVE);

        return new Contact(driver);
    }

    public void clickSuggestedContacts()
    {
        suggestedContacts.click();
        System.out.println("Suggested Contacts was clicked");
    }

    public void clickDeletedItems()
    {
        deletedItems.click();
        System.out.println("Deleted Items was clicked");
    }

    /**
     * Get counter(number of contacts in folder) of selected left menu item(Contacts, Suggested Contacts or Deleted Items)
     * IMPORTANT: folder must be selected at first by clickSuggestedContacts() or clickDeletedItems() method
     * @return
     */
    public int getCounter()
    {
        return Integer.parseInt(JSExecutor.getTextByClassName(class_CounterOfSelectedTab));
    }

    public void switchToVerticalView()
    {
        JSExecutor.clickByElementByClassName(class_SwitchToVerticalView);

        System.out.println("View was switched to [Vertical]");
    }

    public void switchToTileView()
    {
        JSExecutor.clickByElementByClassName(class_SwitchToTileView);

        System.out.println("View was switched to [Tile]");
    }
}
