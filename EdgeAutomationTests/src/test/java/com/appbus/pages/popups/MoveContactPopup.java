package com.appbus.pages.popups;

import com.appbus.pages.helpers.JSExecutor;
import io.appium.java_client.AppiumDriver;
import org.junit.Assert;

// Non-native screen, so no need to extends from PageObject
public class MoveContactPopup
{
    /**
     * Non-native elements
     */
    private static String class_Title = "block-wrapper-header";

    private static String class_ContactsButton          = "notification-button save", // index [0]
                          class_SuggestedContactsButton = "notification-button save"; // index [1]


    public MoveContactPopup(AppiumDriver driver)
    {
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        JSExecutor.injectJQuery();

        return ( JSExecutor.isVisibleViaJQuery("$('." + class_Title + "')") &
                 JSExecutor.isVisibleViaJQuery("$('.notification-button')") );
    }

    public void moveToSuggestedContacts()
    {
        JSExecutor.clickByElementByClassName(class_SuggestedContactsButton, 1);
        System.out.println("Was clicked by Suggested Contacts");
    }
}
