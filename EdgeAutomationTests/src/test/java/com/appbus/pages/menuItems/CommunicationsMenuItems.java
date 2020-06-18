package com.appbus.pages.menuItems;

import com.appbus.pages.PageObject;
import com.appbus.pages.tabs.CalendarTab;
import com.appbus.pages.tabs.ContactsTab;
import com.appbus.pages.tabs.MailTab;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;


/**
 *  List of menu items of Communication section
 */
public class CommunicationsMenuItems extends PageObject
{

    @FindBy(name = "Accenture Portal")
    private MobileElement accenturePortal;

    @FindBy(name = "Mail")
    private MobileElement mail;

    @FindBy(name = "Mail (local)")
    private MobileElement mailLocal;

    @FindBy(name = "Calendar")
    private MobileElement calendar;

    @FindBy(name = "Contacts")
    private MobileElement contacts;

    //...


    public CommunicationsMenuItems(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    /**
     *  Use this constructor if you do not want (or unable) to assert initial communications menu items.
     *  For ex. exadel1 user has different menu items: no Accenture Portal, etc.
     * @param driver
     * @param doNotAssertInitialItems - just flag in method signature. Has no meaning
     */
    public CommunicationsMenuItems(AppiumDriver driver, boolean doNotAssertInitialItems)
    {
        super(driver);
    }

    // We see initial menu elements
    private boolean isInit()
    {
        return (accenturePortal.isDisplayed() & mail.isDisplayed() & mailLocal.isDisplayed());
    }

    public MailTab clickMail()
    {
        mail.click();
        System.out.println("Mail tab was clicked");
        return new MailTab(driver);
    }

    public CalendarTab clickCalendar()
    {
        calendar.click();
        System.out.println("Calendar tab was clicked");
        return new CalendarTab(driver);
    }

    public ContactsTab clickContacts()
    {
        contacts.click();
        System.out.println("Contacts tab was clicked");
        return new ContactsTab(driver);
    }

}
