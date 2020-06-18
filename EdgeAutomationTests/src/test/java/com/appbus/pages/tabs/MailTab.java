package com.appbus.pages.tabs;

import com.appbus.pages.email_related.Email;
import com.appbus.pages.email_related.MailMoreOption;
import com.appbus.pages.email_related.MailMoveOption;
import com.appbus.pages.PageObject;
import com.appbus.pages.constants.Context;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.popups.DeleteDraftPopup;
import com.appbus.pages.popups.DeleteEmailPopup;
import com.appbus.pages.popups.DeleteSingleEmailPopup;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.support.FindBy;
import tests.source.FunctionalTest;

public class MailTab extends PageObject
{
    @FindBy(name = "New Email")
    private MobileElement newEmailButton;

    @FindBy(name = "Inbox")
    private MobileElement inbox;

    @FindBy(name = "Outbox")
    private MobileElement outbox;

    @FindBy(name = "Sent Items")
    private MobileElement sentItems;

    @FindBy(name = "Deleted Items")
    private MobileElement deletedItems;

    @FindBy(name = "Drafts")
    private MobileElement drafts;

    @FindBy(name = "Junk E-Mail")
    private MobileElement junkEmail;

    /**
     * Non native elements
     */
    private static final String id_SearchButton     =  "small-text-filter-toggler",
                                id_SearchField      =  "messagesSearchInput",
                                id_DeleteButton     =  "small-more-button-delete",
                                id_MoveButton       =  "small-move-to-button-toggler",
                                id_MoreButton       =  "small-more-button-toggler",
                                id_CloseEmailButton =  "close-button-icon";

    private static final String id_RefreshButton    =  "email-top-spinner";

    private static final String class_ClearSearchField   =  "icon-icon_close_filled",
                                class_DeleteSingleEmail  =  "icon-icon_garbage",
                                class_ArrowBack          =  "icon-icon_back";


    public MailTab(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return (newEmailButton.isDisplayed() & junkEmail.isDisplayed());
    }

    /**
     * Click delete email button in Inbox, Sent Items, etc. section
     **/
    public DeleteEmailPopup clickDeleteEmailButton()
    {
        JSExecutor.clickByElement(id_DeleteButton);
        System.out.println("Delete button was pressed");

        FunctionalTest.switchContext(Context.NATIVE);

        return new DeleteEmailPopup(driver);
    }

    /**
     * Click delete email button in Draft section
     */
    public DeleteDraftPopup clickDeleteDraftButton()
    {
        JSExecutor.clickByElement(id_DeleteButton);
        System.out.println("Delete button was clicked");

        FunctionalTest.switchContext(Context.NATIVE);

        return new DeleteDraftPopup(driver);
    }

    /**
     * Click delete email button in View Mode
     */
    public DeleteSingleEmailPopup clickDeleteSingleEmailButton()
    {
        JSExecutor.clickByElementByClassName(class_DeleteSingleEmail);
        System.out.println("Delete button was clicked");

        FunctionalTest.switchContext(Context.NATIVE);

        return new DeleteSingleEmailPopup(driver);
    }

    public void clickSearchButton()
    {
        JSExecutor.clickByElement(id_SearchButton);
    }

    public void searchText(String textToSearch)
    {
        JSExecutor.setTextForField(id_SearchField, textToSearch);
    }

    public Email clickNewEmailButton()
    {
        newEmailButton.click();
        System.out.println("New Email button was clicked");

        return new Email(driver);
    }

    public MailTab clickInbox()
    {
        inbox.click();
        System.out.println("Inbox was clicked");

        return this;
    }

    public MailTab clickSentItems()
    {
        sentItems.click();
        System.out.println("Sent Items was clicked");

        return this;
    }

    public MailTab clickDeletedItems()
    {
        deletedItems.click();
        System.out.println("Deleted Items was clicked");

        return this;
    }

    public MailTab clickDrafts()
    {
        drafts.click();
        System.out.println("Drafts was clicked");

        return this;
    }

    public MailTab clickJunk()
    {
        junkEmail.click();
        System.out.println("Junk E-Mail was clicked");

        return this;
    }

    /**
     * Select checkbox to _check_ all emails
     */
    public void checkSelectAllCheckbox()
    {
        driver.findElement(By.cssSelector("#check-all-action-btn .icon-icon_unchecked")).click();
        System.out.println("Select all checkbox was clicked [checked]");
    }

    /**
     * Select checkbox to _uncheck_ all emails
     */
    public void uncheckSelectAllCheckbox()
    {
        driver.findElement(By.cssSelector("#check-all-action-btn .icon-icon_checked")).click();
        System.out.println("Select all checkbox was clicked [unchecked]");
    }

    public void clearSearchFiled()
    {
        JSExecutor.clickByElementByClassName(class_ClearSearchField);
        System.out.println("Search field was cleared");
    }

    public void clickRefreshButton()
    {
        JSExecutor.clickByElement(id_RefreshButton);
        System.out.println("Refresh button was clicked");
    }

    public MailMoveOption clickMoveButton()
    {
        JSExecutor.clickByElement(id_MoveButton);
        System.out.println("Move button was clicked");

        return new MailMoveOption();
    }

    public MailMoreOption clickMoreButton()
    {
        JSExecutor.clickByElement(id_MoreButton);
        System.out.println("More button was clicked");

        return new MailMoreOption();
    }

    /**
     * Click arrow back button in list view
     */
    public void clickBackButton()
    {
        JSExecutor.clickByElementByClassName(class_ArrowBack);
        System.out.println("Back button was clicked");
    }
}
