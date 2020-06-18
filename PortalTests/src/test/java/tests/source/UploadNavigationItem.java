package tests.source;

import net.portal.constants.Const;
import net.portal.constants.Notifications;
import net.portal.forms.ItemAssignmentDetails;
import net.portal.forms.UploadItem;
import net.portal.pages.DeleteNavigationItemPopup;
import net.portal.pages.HeaderMenu;
import net.portal.pages.user_and_role_management.NavigationItems;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;

// This test creates new Navigation Item, downloads json file of just created item, delete item and upload again via Upload Item button
public class UploadNavigationItem
{
    @Test
    public void uploadNavigationItem() throws InterruptedException
    {
        System.out.println("--- START OF UploadNavigationItem ---");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        NavigationItems navigationItemsPage = headerMenu.clickNavigationItems();

        ItemAssignmentDetails itemAssignmentDetails = navigationItemsPage.addNavigationItem();
        Thread.sleep(3_000);

        String navItemID = "A_UploadItemAT";

        itemAssignmentDetails.setId(navItemID);
        itemAssignmentDetails.selectArchetype("PDF");
        Thread.sleep(1_000);

        itemAssignmentDetails.setPropertyValue("_property_edit", "at val 1");
        itemAssignmentDetails.setPropertyValue("_property_edited", "Val 2 AT");
        itemAssignmentDetails.setPropertyValue("url", "https://ru.wikipedia.org");
        itemAssignmentDetails.clickSave();
        Thread.sleep(3_000);

        navigationItemsPage.searchForId(navItemID);
        Thread.sleep(2_000);

        navigationItemsPage.downloadJsonFile(navItemID);
        Thread.sleep(5_000);

        File navItemsJsonFile = new File(Const.DOWNLOAD_FOLDER + "\\" + navItemID + ".json");

        Assert.assertTrue(navItemsJsonFile.exists());

        // Delete just created nav item on web page
        DeleteNavigationItemPopup deleteNavigationItemPopup = navigationItemsPage.deleteNavigationItem(navItemID);
        Thread.sleep(3_000);

        deleteNavigationItemPopup.clickYes();
        Thread.sleep(3_000);

        navigationItemsPage = headerMenu.clickNavigationItems();

        UploadItem uploadItemForm = navigationItemsPage.clickUploadItem();
        Thread.sleep(3_000);

        uploadItemForm.chooseFile(navItemsJsonFile.getAbsolutePath());
        uploadItemForm.clickUpload();
        Thread.sleep(3_000);

        uploadItemForm.clickNext();
        Thread.sleep(3_000);

        uploadItemForm.clickSave();
        Thread.sleep(5_000);

        Assert.assertEquals("Successfully saved.",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#itemUploadWizardDlgForm\\\\:itemUploadWizardDlgFormMessages').text()")));

        uploadItemForm.clickCancel();
        Thread.sleep(3_000);

        navigationItemsPage.searchForId(navItemID);
        Thread.sleep(2_000);

        System.out.println("Assert that just uploaded item was uploaded successfully...");
        Assert.assertEquals("A_UploadItemATAdd ItemEdit ItemDelete ItemMove to another item as childMove to the root levelDownload Json FileItem CopyPDF_property_editat val 1_property_editedVal 2 ATurlhttps://ru.wikipedia.org",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data').text()")));

        System.out.println("*** After-test routine ***");
        deleteNavigationItemPopup = navigationItemsPage.deleteNavigationItem(navItemID);
        Thread.sleep(3_000);

        deleteNavigationItemPopup.clickYes();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

        if( navItemsJsonFile.delete() )
        {
            System.out.println(navItemsJsonFile.getAbsolutePath() + " was deleted");
        }
        else
        {
            System.err.println("Unable to delete " + navItemsJsonFile.getAbsolutePath());
        }

        System.out.println("--- END OF UploadNavigationItem ---");
    }
}
