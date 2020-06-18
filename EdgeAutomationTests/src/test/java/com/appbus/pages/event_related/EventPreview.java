package com.appbus.pages.event_related;

import com.appbus.pages.constants.Context;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.popups.Deletable;
import com.appbus.pages.popups.DeleteRepeatedEventPopup;
import com.appbus.pages.popups.DeleteSingleEventPopup;
import org.junit.Assert;
import tests.source.FunctionalTest;

// Non-native, so no need to extends from PageObject
/**
 * Event preview in Calendar grid with 3 buttons
 */
public class EventPreview
{
    private static final String id_EditEvent   = "edit-appointment-button",
                                id_MoveEvent   = "move-appointment-button",
                                id_DeleteEvent = "delete-appointment-button",

                                class_EventTitle = "subject",
                                class_EventDate  = "date",
                                class_Notes      = "notes";

    public EventPreview()
    {
        JSExecutor.injectJQuery();

        try
        {
            Thread.sleep(4000);
        } catch (InterruptedException e)
        {
            e.printStackTrace();
        }

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( JSExecutor.isVisibleViaJQuery("$('#" + id_EditEvent   + "')") &
                 JSExecutor.isVisibleViaJQuery("$('#" + id_MoveEvent   + "')") &
                 JSExecutor.isVisibleViaJQuery("$('#" + id_DeleteEvent + "')") );
    }

    public String getEventTitle()
    {
        return JSExecutor.getTextByClassName(class_EventTitle);
    }

    public String getEventDate()
    {
        return JSExecutor.getTextByClassName(class_EventDate);
    }

    public String getEventNotes()
    {
        return JSExecutor.getTextByClassName(class_Notes);
    }

    public String getEventAlertValue()
    {
        return JSExecutor.getTextViaJQuery("$('.editable-info .field .title:contains(\"Alert\")').next()");
    }

    public NewEvent clickEditEvent()
    {
        JSExecutor.clickByElement(id_EditEvent);
        System.out.println("Edit event was clicked");

        FunctionalTest.switchContext(Context.NATIVE);

        return new NewEvent(FunctionalTest.getDriver(), true);
    }

    public Deletable clickDeleteEvent(boolean isRepeatedEvent)
    {
        JSExecutor.clickByElement(id_DeleteEvent);
        System.out.println("Delete event was clicked");

        FunctionalTest.switchContext(Context.NATIVE);

        return ( isRepeatedEvent == true ) ? new DeleteRepeatedEventPopup(FunctionalTest.getDriver()) : new DeleteSingleEventPopup(FunctionalTest.getDriver());
    }

    public AllEventsSideBar clickShowAllOccurrences()
    {
        JSExecutor.clickViaJQuery("$('.options-panel span:contains(\"Show\")')");

        System.out.println("Show all occurrences was clicked");

        return new AllEventsSideBar();
    }
}
