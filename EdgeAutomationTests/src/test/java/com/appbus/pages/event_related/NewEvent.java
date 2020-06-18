package com.appbus.pages.event_related;

import com.appbus.pages.PageObject;
import com.appbus.pages.constants.Context;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.popups.Deletable;
import com.appbus.pages.popups.DeleteRepeatedEventPopup;
import com.appbus.pages.popups.DeleteSingleEventPopup;
import com.appbus.pages.popups.UpdateEventPopup;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;
import tests.source.FunctionalTest;

public class NewEvent extends PageObject
{
    @FindBy(name = "New Event")
    private MobileElement titleLabel;

    @FindBy(name = "Edit event")
    private MobileElement titleLabelEditMode;

    @FindBy(name = "Starts")
    private MobileElement startsLabel;

    @FindBy(name = "Alert")
    private MobileElement alertLabel;

    @FindBy(name = "Repeat")
    private MobileElement repeatLabel;

    @FindBy(name = "Invitees")
    private MobileElement inviteesLabel;

    @FindBy(name = "End Repeat")
    private MobileElement endRepeatLabel;

    /**
     * Non native elements
     * id's of new event fields
     */
    private static final String id_Title    = "appointmentTitle",
                                id_Location = "appointmentLocation",
                                id_Notes    = "appointmentBody",
                                id_Apply    = "apply-changes-icon",
                                id_Delete   = "delete-event-icon"; // Trash can icon in edit mode

    public NewEvent(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    /**
     * Only for Edit event object
     * @param driver
     * @param editMode just marker that indicates that this constructor is used under Edit Event mode
     */
    public NewEvent(AppiumDriver driver, boolean editMode)
    {
        super(driver);

        Assert.assertTrue( titleLabelEditMode.isDisplayed() );
    }

    private boolean isInit()
    {
        return titleLabel.isDisplayed();
    }

    public void setTitle(String title)
    {
        JSExecutor.setTextForField(id_Title, title);
    }

    public String getTitle()
    {
        return JSExecutor.getTextViaJQueryFromInput("$('#" + id_Title + "')");
    }

    public void setLocation(String location)
    {
        JSExecutor.setTextForField(id_Location, location);
    }

    public EventStartsOption clickStartsLabel()
    {
        startsLabel.click();
        System.out.println("Starts label was clicked");

        FunctionalTest.switchContext(Context.WEBVIEW);

        return new EventStartsOption();
    }

    public EventAlertOption clickAlertLabel()
    {
        alertLabel.click();
        System.out.println("Alert label was clicked");

        FunctionalTest.switchContext(Context.WEBVIEW);

        return new EventAlertOption();
    }

    public EventInviteesOption clickInviteesLabel()
    {
        inviteesLabel.click();
        System.out.println("Invitees label was clicked");

        FunctionalTest.switchContext(Context.WEBVIEW);

        return new EventInviteesOption();
    }

    public EventRepeatOption clickRepeatLabel()
    {
        repeatLabel.click();
        System.out.println("Repeat label was clicked");

        FunctionalTest.switchContext(Context.WEBVIEW);

        return new EventRepeatOption();
    }

    public EventEndRepeatOption clickEndRepeatLabel()
    {
        endRepeatLabel.click();
        System.out.println("End Repeat label was clicked");

        FunctionalTest.switchContext(Context.WEBVIEW);

        return new EventEndRepeatOption();
    }

    /**
     * Accept as single event
     */
    public void clickAccept()
    {
        JSExecutor.clickByElement(id_Apply);
        System.out.println("Accept button was clicked");
    }

    /**
     * Accept as repeated event
     * @param isRepeatedEvent just marker to indicate that need to show Update Event Popup
     */
    public UpdateEventPopup clickAccept(boolean isRepeatedEvent)
    {
        JSExecutor.clickByElement(id_Apply);
        System.out.println("Accept button was clicked");
        FunctionalTest.switchContext(Context.NATIVE);

        return new UpdateEventPopup(driver);
    }

    public Deletable clickDelete(boolean isRepeatedEvent)
    {
        JSExecutor.clickByElement(id_Delete);
        System.out.println("Delete event was clicked");

        FunctionalTest.switchContext(Context.NATIVE);

        return ( isRepeatedEvent == true ) ? new DeleteRepeatedEventPopup(driver) : new DeleteSingleEventPopup(driver);
    }

    public String getStartsDate()
    {
        return JSExecutor.getTextViaJQuery("$('.edit-info .clickable.field .title:contains(\"Starts\")').next()");
    }

    public String getEndsDate()
    {
        return JSExecutor.getTextViaJQuery("$('.edit-info .clickable.field .title:contains(\"Ends\")').next()");
    }

    /**
     * Get Start Repeat date. Available only after choosing of any of repeat options.
     * @return
     */
    public String getStartRepeatDate()
    {
        JSExecutor.injectJQuery();

        return JSExecutor.getTextViaJQuery("$('.edit-info .clickable.field .title:contains(\"Start Repeat\")').parent().find('span')");
    }

    /**
     * Get End Repeat date. Available only after choosing of any of repeat options.
     * @return
     */
    public String getEndRepeatDate()
    {
        JSExecutor.injectJQuery();

        return JSExecutor.getTextViaJQuery("$('.edit-info .clickable.field .title:contains(\"End Repeat\")').parent().find('span')");
    }

    public void clickAllDayCheckbox()
    {
        JSExecutor.clickViaJQuery("$('.edit-info .switch.round.small').children()[1]");

        System.out.println("All-day checkbox was clicked");
    }

    public void setNotes(String notes)
    {
        JSExecutor.setTextForField(id_Notes, notes);
    }

}
