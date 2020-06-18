package tests.source;

import com.appbus.pages.email_related.Email;
import com.appbus.pages.constants.Const;
import com.appbus.pages.constants.Context;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.helpers.Saver;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.popups.DeleteDraftPopup;
import com.appbus.pages.popups.SaveDraftPopup;
import com.appbus.pages.tabs.MailTab;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.List;
import java.util.Random;

public class DraftEmail
{
    @Test
    public void draftTest() throws InterruptedException
    {
        JSExecutor.injectJQuery();

        int draftsNumBefore = 0; // Get amount of emails in Drafts folder before creating of new draft
        if( JSExecutor.getTextViaJQuery("$('#emailFolders .folder-name:contains(\"Drafts\") + span > .label')").equals("") == false )
        {
            draftsNumBefore = Integer.parseInt(JSExecutor.getTextViaJQuery("$('#emailFolders .folder-name:contains(\"Drafts\") + span > .label')"));
        }

        System.out.println("Amount of emails in Drafts folder before creating of new draft = " + draftsNumBefore);
        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2_000);

        MailTab mailTab = new MailTab(FunctionalTest.getDriver());
        Email email = mailTab.clickNewEmailButton();

        // Generate random integer as identifier [1,100]
        Random generator = new Random();
        int id = generator.nextInt(100) + 1;

        String subject = "Draft test subj " + id;

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        email.setToEmail(Const.LOGIN + "@" + Const.DOMAIN + ".net");
        email.setSubject(subject + " ");

        String draftMessageBody = "Draft example autotest\n" + "end.";
        email.setMessageBody(draftMessageBody);

        Scroller.scrollUp();

        SaveDraftPopup saveDraftPopup = email.closeEmail();

        System.out.println("Check that we see Delete Draft pop up...");
        Assert.assertEquals("Delete Draft", saveDraftPopup.getTitle());

        saveDraftPopup.clickSave();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);

        // Get amount of emails in Drafts folder after creating of draft
        int draftsNumAfter = Integer.parseInt(JSExecutor.getTextViaJQuery("$('#emailFolders .folder-name:contains(\"Drafts\") + span > .label')"));

        System.out.println("Amount of emails in Drafts folder after creating of draft = " + draftsNumAfter);
        System.out.println("Making sure that amount of drafts were increased by +1...");
        Assert.assertEquals(draftsNumBefore + 1, draftsNumAfter);

        // Save draft email subject
        Saver.saveDraftEmailSubject(subject);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2_000);

        mailTab.clickDrafts();

        Thread.sleep(2000);

        FunctionalTest.switchContext(Context.WEBVIEW);
        mailTab.clickSearchButton();
        mailTab.searchText(subject); // Search draft email by subject


        FunctionalTest.switchContext(Context.NATIVE);

        // Get amount of matched emails
        List<WebElement> matched = FunctionalTest.getDriver().findElements(By.xpath("//XCUIElementTypeApplication[@name='AppBus']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[5]"));

        System.out.println("We should see only _one_ e-mail with subject = " + subject);
        System.out.println("Checking...");
        Assert.assertEquals(1, matched.size());

        System.out.println("Click by email with subject = " + subject);
        matched.get(0).click();
        Thread.sleep(2_000);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);

        System.out.println("Making sure that message body equals:\n" + draftMessageBody);
        Assert.assertEquals(draftMessageBody, email.getMessageBody());

        // Click <- back button
        mailTab.clickBackButton();

        // Delete selected draft
        FunctionalTest.switchContext(Context.WEBVIEW);

        // Select email
        MobileElement selectEmailCheckBox = (MobileElement) FunctionalTest.getDriver().findElement(By.className("icon-icon_unchecked"));

        selectEmailCheckBox.click();

        DeleteDraftPopup deleteDraftPopup = mailTab.clickDeleteDraftButton();

        System.out.println("Check that we see Delete selected draft pop up...");
        Assert.assertEquals("Delete selected drafts?", deleteDraftPopup.getTitle());

        deleteDraftPopup.clickOk();

        MobileElement noMessagesText = (MobileElement) (new WebDriverWait(FunctionalTest.getDriver(), 25)).until(ExpectedConditions.presenceOfElementLocated(By.name("No messages for current folder")));
        System.out.println("Check that label 'No messages...' appear...");
        Assert.assertEquals("No messages for current folder", noMessagesText.getText());

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2_000);
        System.out.println("Making sure that amount of drafts were decreased by -1...");

        int draftsNumCurrent = Integer.parseInt(JSExecutor.getTextViaJQuery("$('#emailFolders .folder-name:contains(\"Drafts\") + span > .label')"));
        Assert.assertEquals(draftsNumCurrent, draftsNumAfter - 1);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2_000);
        mailTab.clickDeletedItems(); // Go back to Deleted Items

        Thread.sleep(5000);

        // Get amount of matched emails
        matched = FunctionalTest.getDriver().findElements(By.xpath("//XCUIElementTypeApplication[@name='AppBus']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeWebView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[5]"));

        System.out.println("We should see only _one_ e-mail with subject = " + subject);
        System.out.println("Checking...");

        Assert.assertEquals(1, matched.size());
        Thread.sleep(2000);

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(2000);

        mailTab.clearSearchFiled();
        mailTab.clickSearchButton();

        Thread.sleep(2000);
        FunctionalTest.switchContext(Context.NATIVE);
    }
}
