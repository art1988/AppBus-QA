package tests.source;

import com.appbus.pages.constants.Const;
import com.appbus.pages.constants.Context;
import com.appbus.pages.email_related.Email;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.tabs.MailTab;
import com.appbus.pages.tabs.SharePointTab;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;

public class Reattach
{
    /**
     * Check of ED-3115
     */
    @Test
    public void reattach() throws InterruptedException
    {
        MailTab mailTab = new MailTab(FunctionalTest.getDriver());

        Email email = mailTab.clickNewEmailButton();

        FunctionalTest.switchContextToWebViewByURL(Const.VALID_WEBVIEW_URL);
        Thread.sleep(3000);

        SharePointTab sharePointTab = email.clickAttachFile().clickSharePoint();

        sharePointTab.clickFirstFolder();
        sharePointTab.clickXlsxFile();
        sharePointTab.confirmAttach();

        FunctionalTest.switchContextToWebViewByURL(Const.VALID_WEBVIEW_URL);
        Thread.sleep(3000);

        System.out.println("Trying to remove just attached file...");
        JSExecutor.clickViaJQuery("$(\"span[data-role='remove']\")");

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3000);

        System.out.println("Checking that there is no Attachments label...");

        MobileElement attachmentsLabel = null;
        try
        {
            attachmentsLabel = (MobileElement) FunctionalTest.getDriver().findElement(By.name("Attachments:"));
        }
        catch(org.openqa.selenium.NoSuchElementException ex)
        {
            System.err.println("There is no Attachments: label [OK]");
        }
        Assert.assertNull(attachmentsLabel);

        FunctionalTest.switchContextToWebViewByURL(Const.VALID_WEBVIEW_URL);
        Thread.sleep(3000);

        sharePointTab = email.clickAttachFile().clickSharePoint();

        sharePointTab.clickFirstFolder();
        sharePointTab.clickDocxFile();
        sharePointTab.confirmAttach();

        System.out.println("Making sure that we see _only_ *.docx attached file without *.xlsx file...");

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(3000);

        Assert.assertTrue(sharePointTab.isDocxVisible());
        Assert.assertFalse(sharePointTab.isXlsxVisible());

        Thread.sleep(5000);
    }
}
