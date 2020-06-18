package com.appbus.pages.email_related;

import com.appbus.pages.AttachScreen;
import com.appbus.pages.PageObject;
import com.appbus.pages.constants.Context;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.popups.SaveDraftPopup;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;
import tests.source.FunctionalTest;


public class Email extends PageObject
{
    @FindBy(name = "Send")
    private MobileElement sendButton;

    /**
     * Non native elements
     * id's of New Email
     */
    private static final String id_ToField  = "emailInput-to",
                                id_CcField  = "emailInput-cc",
                                id_BccField = "emailInput-bcc",
                                id_Subject  = "new-email-subject-input",
                                id_Attach   = "icon-icon_editor_attach",
                                id_Close    = "close-button-icon";

    private static final String class_Aa = "icon-icon_aa";

    private static final String id_PlusForToField = "add-contact-dropdown-toggler-to",
                                id_PlusForCcField = "add-contact-dropdown-toggler-cc";

    public enum Field {TO, CC, BCC};

    @FindBy(name = "Attachments:")
    private MobileElement attachmentsLabel;


    public Email(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return sendButton.isDisplayed();
    }

    public void setToEmail(String to)
    {
        JSExecutor.setTextForField(id_ToField, to);
    }

    public void setCcEmail(String cc)
    {
        JSExecutor.setTextForField(id_CcField, cc);
    }

    public void setSubject(String subject)
    {
        JSExecutor.setTextForField(id_Subject, subject);
    }

    public void setMessageBody(String text)
    {
        // Use self written function insertTextInDraft() to set email message body
        // Using arguments[0] because text can have \n, \t symbols
        driver.executeScript("window.insertTextInDraft(arguments[0])", text);
    }

    public String getMessageBody()
    {
        // Get message body text from inner iframe
        return String.valueOf(driver.executeScript("return document.getElementById('message-content-iframe').contentWindow.document.body.innerText;"));
    }

    public AttachScreen clickAttachFile()
    {
        JSExecutor.clickByElement(id_Attach);
        System.out.println("Attach button was clicked");

        FunctionalTest.switchContext(Context.NATIVE);

        return new AttachScreen(driver);
    }

    public RichEditor clickAa()
    {
        JSExecutor.clickByElementByClassName(class_Aa);
        System.out.println("Aa button was clicked");

        return new RichEditor();
    }

    /**
     *  Inner class that represents RichEditor of email
     */
    public class RichEditor
    {
        private final String event = "const event = new MouseEvent('mousedown', {'view': window,'bubbles': true,'cancelable': true}); ";

        /**
         * Controls of RichEditor
         */
        public static final String class_bold      = "awesome-icon-bold",
                                   class_italic    = "awesome-icon-italic",
                                   class_underline = "awesome-icon-underline",
                                   class_quote     = "awesome-icon-blockquote",
                                   class_ul        = "awesome-icon-ul",
                                   class_ol        = "awesome-icon-ol",
                                   class_link      = "awesome-icon-link";

        RichEditor()
        {
            JSExecutor.injectJQuery();

            Assert.assertTrue( isInit() );
        }

        private boolean isInit()
        {
            return ( JSExecutor.isVisibleViaJQuery("$('." + class_bold + "')")   &
                     JSExecutor.isVisibleViaJQuery("$('." + class_italic + "')") &
                     JSExecutor.isVisibleViaJQuery("$('." + class_ul + "')"));
        }

        public void clickRichEditorControl(String class_of_control, String message)
        {
            StringBuffer jsCode = new StringBuffer(event);
            jsCode.append("document.querySelector('." + class_of_control + "').dispatchEvent(event)");

            driver.executeScript(jsCode.toString());

            System.out.println(message);
        }
    }

    public void sendEmail() throws InterruptedException
    {
        if(sendButton.isDisplayed())
        {
            sendButton.click();
            System.out.println("Send email was clicked");
            Thread.sleep(2000);
            return;
        }

        System.err.println("Unable to locate Send button");
    }

    public SaveDraftPopup closeEmail()
    {
        JSExecutor.clickByElement(id_Close);
        System.out.println("e-mail was closed");

        FunctionalTest.switchContext(Context.NATIVE);

        return new SaveDraftPopup(driver);
    }

    public AddContactOption clickPlusButtonFor(Field field, boolean needToClose)
    {
        switch (field)
        {
            case TO: JSExecutor.clickByElement(id_PlusForToField); break;
            case CC: JSExecutor.clickByElement(id_PlusForCcField); break;
        }

        if( needToClose == true )
        {
            System.out.println("Plus button for " + field.name() + " filed was clicked [Closed]");
            return null;
        }

        System.out.println("Plus button for " + field.name() + " filed was clicked [Opened]");

        FunctionalTest.switchContext(Context.NATIVE);

        return new AddContactOption(driver);
    }

    public boolean isAttachmentsLabelVisible()
    {
        return attachmentsLabel.isDisplayed();
    }
}
