package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.email_related.Email;
import com.appbus.pages.constants.Const;
import com.appbus.pages.constants.Context;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.menuItems.AttachmentSubmenu;
import com.appbus.pages.menuItems.DocumentsMenuItems;
import com.appbus.pages.menuItems.DocumentsSubmenu;
import com.appbus.pages.menuItems.ServiceNavBar;
import com.appbus.pages.tabs.MailTab;
import com.appbus.pages.tabs.SharePointTab;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;

import java.util.Random;

public class AttachViaDocuments
{
    @Test
    public void attachViaDocuments() throws InterruptedException
    {
        ServiceNavBar navBar = new ServiceNavBar(FunctionalTest.getDriver());
        ActiveHamburgerMenu activeHamburgerMenu = navBar.clickHamburgerMenu();
        DocumentsMenuItems documentsMenuItems = activeHamburgerMenu.clickDocuments();

        SharePointTab sharePointTab = documentsMenuItems.clickSharePoint();
        sharePointTab.clickFirstFolder();
        sharePointTab.clickXmlFile();

        DocumentsSubmenu documentsSubmenu = sharePointTab.getSubmenu();
        Email emailWithAttach = documentsSubmenu.clickAttach();

        System.out.println("Make sure that we see added Attachments field...");
        Assert.assertTrue(emailWithAttach.isAttachmentsLabelVisible());

        Thread.sleep(4000);

        System.out.println("Make sure that xml file was attached...");
        MobileElement xmlFile = (MobileElement) FunctionalTest.getDriver().findElement(By.xpath("(//XCUIElementTypeStaticText[@name=\"XML_auto.xml\"])[2]"));
        Assert.assertTrue(xmlFile.isDisplayed());

        FunctionalTest.switchContextToWebViewByURL(Const.VALID_WEBVIEW_URL);
        Thread.sleep(4000);

        emailWithAttach.setToEmail(Const.LOGIN + "@" + Const.DOMAIN + ".net");

        // Generate random integer as identifier [1,100]
        Random generator = new Random();
        int id = generator.nextInt(100) + 1;

        String emailSubject = "Attach via documents " + id;
        emailWithAttach.setSubject(emailSubject);

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2000);

        emailWithAttach.sendEmail();
        Thread.sleep(2000);

        MailTab mailTab = new MailTab(FunctionalTest.getDriver());

        FunctionalTest.switchContextToWebViewByURL(Const.VALID_WEBVIEW_URL);
        Thread.sleep(2000);

        mailTab.clearSearchFiled();

        mailTab.clickRefreshButton();
        Thread.sleep(4000);

        System.out.println("Searching email by subject = " + emailSubject);
        mailTab.searchText(emailSubject);
        Thread.sleep(3000); // Need some time to fetch email by subject

        JSExecutor.injectJQuery();

        System.out.println("Checking that received email has attach icon...");
        Assert.assertTrue((Boolean) FunctionalTest.getDriver().executeScript("return $(\".email-list-scroller__date-and-attachments i\").hasClass(\"icon-icon_editor_attach\")"));

        System.out.println("Click by found email...");
        JSExecutor.clickByElementByClassName("icon-icon_editor_attach");
        Thread.sleep(3000);

        System.out.println("Checking that it has subject = " + emailSubject);
        Assert.assertEquals(emailSubject, JSExecutor.getTextByClassName("subject"));

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(2000);

        System.out.println("Checking that attached XML file is visible...");
        Assert.assertTrue(sharePointTab.isXmlVisible());

        System.out.println("Checking that XML file can be opened...");
        sharePointTab.clickXmlFile();

        // Check some text inside xml document
        Assert.assertTrue(FunctionalTest.getDriver().findElement(By.name("Cristian Osorio")).isDisplayed());

        AttachmentSubmenu attachmentSubmenu = new AttachmentSubmenu(FunctionalTest.getDriver());
        attachmentSubmenu.clickFullscreen();
        Thread.sleep(2000);

        System.out.println("Checking that in fullscreen mode top nav bar is hidden...");

        try
        {
            MobileElement hmbMenuButton = (MobileElement) FunctionalTest.getDriver().findElement(By.name("BT GlobalNav Default@2x"));
        }
        catch(org.openqa.selenium.NoSuchElementException ex)
        {
            System.err.println("Menu button is hidden [OK]");
        }

        attachmentSubmenu.clickBack();

        FunctionalTest.switchContextToWebViewByURL(Const.VALID_WEBVIEW_URL);
        Thread.sleep(3000);

        mailTab.clickBackButton();

        FunctionalTest.switchContext(Context.NATIVE);

        Thread.sleep(7000);
    }
}
