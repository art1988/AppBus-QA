package tests.source;

import net.portal.constants.Const;
import net.portal.constants.Notifications;
import net.portal.forms.PolicyDetail;
import net.portal.forms.UploadPolicy;
import net.portal.pages.DeleteConfirmPopup;
import net.portal.pages.DeletePolicyConfirmation;
import net.portal.pages.HeaderMenu;
import net.portal.pages.user_and_role_management.Policies;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;

public class DownloadUploadPolicy
{
    @Test
    public void downloadUploadPolicy() throws InterruptedException
    {
        System.out.println("--- START OF DownloadUploadPolicy ---");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Policies policiesPage = headerMenu.clickPolicies();

        PolicyDetail propertyDetail = policiesPage.addPolicy();
        Thread.sleep(1_000);

        String policyName = "download_upload_name_AT",
               policyDescription = "DownloadUploadPolicy description";

        propertyDetail.setName(policyName);
        propertyDetail.setDescription(policyDescription);
        propertyDetail.setType("LIST");
        Thread.sleep(1_000);

        propertyDetail.checkItem();
        propertyDetail.addItemProperty("PDF", "CON", false, false);
        propertyDetail.checkDevice();
        propertyDetail.checkDeviceMultiple();
        propertyDetail.checkProvision();
        propertyDetail.checkProvisionService();

        propertyDetail.clickAdd();
        Thread.sleep(4_000);

        policiesPage.searchForName(policyName);
        Thread.sleep(2_000);

        policiesPage.clickApplyFilter();
        Thread.sleep(2_000);

        policiesPage.downloadPolicy(policyName);
        Thread.sleep(4_000);

        System.out.println("Checking that file was downloaded...");
        File policyFile = new File(Const.DOWNLOAD_FOLDER + "\\" + policyName + ".json");
        Assert.assertTrue(policyFile.exists());

        System.out.println("Delete just created policy...");
        propertyDetail = policiesPage.clickEdit(policyName);
        Thread.sleep(1_000);

        propertyDetail.selectAllItemProperties();
        DeleteConfirmPopup deleteConfirmPopup = propertyDetail.deleteItemProperty();
        Thread.sleep(1_000);
        deleteConfirmPopup.clickYes();
        Thread.sleep(1_000);
        propertyDetail.clickSave();
        Thread.sleep(2_000);

        DeletePolicyConfirmation deletePolicyConfirmation = policiesPage.deletePolicy(policyName);
        Thread.sleep(2_000);

        deletePolicyConfirmation.clickYes();
        Thread.sleep(2_000);

        // Visit Policies page again...
        policiesPage = headerMenu.clickPolicies();

        System.out.println("Making sure that there is no more policy with name : " + policyName);
        // Make sure that there is no more policy with name

        policiesPage.searchForName(policyName);
        policiesPage.clickApplyFilter();
        Thread.sleep(2_000);

        Assert.assertEquals("No records found.", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data').text()")));

        // Visit Policies page again...
        policiesPage = headerMenu.clickPolicies();

        UploadPolicy uploadPolicyForm = policiesPage.uploadPolicy();
        Thread.sleep(1_000);

        uploadPolicyForm.chooseFile(policyFile.getAbsolutePath());
        Thread.sleep(1_000);
        uploadPolicyForm.clickUpload();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.POLICY_SUCCESSFULLY_SAVED.getNotificationText(), notificationPopup.getText());

        uploadPolicyForm.clickClose();

        // Visit Policies page again...
        policiesPage = headerMenu.clickPolicies();

        // Search for uploaded policy
        policiesPage.searchForName(policyName);
        policiesPage.clickApplyFilter();
        Thread.sleep(2_000);

        System.out.println("Assert that all setting were uploaded correctly...");

        Assert.assertEquals("PDF", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td td:nth-child(1)').text()")));
        Assert.assertEquals("DownloadUploadPolicy descriptionCONTROLLER", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(2)').text()")));
        Assert.assertEquals("LIST", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(3)').text()")));

        Assert.assertTrue(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(5)').find('img').attr(\"src\")").equals("/edapt-admin/images/x-mark-24.png"));
        Assert.assertTrue(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(6)').find('img').attr(\"src\")").equals("/edapt-admin/images/ok-mark-24.png")); // Device mark

        Assert.assertTrue(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(7)').find('img').attr(\"src\")").equals("/edapt-admin/images/ok-mark-24.png")); // Provision mark

        Assert.assertTrue(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td td:nth-child(3)').find('img').attr(\"src\")").equals("/edapt-admin/images/x-mark-24.png"));
        Assert.assertTrue(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td td:nth-child(4)').find('img').attr(\"src\")").equals("/edapt-admin/images/ok-mark-24.png"));


        System.out.println("*** After test clean-up ***");
        propertyDetail = policiesPage.clickEdit(policyName);
        Thread.sleep(1_000);

        propertyDetail.selectAllItemProperties();
        deleteConfirmPopup = propertyDetail.deleteItemProperty();
        Thread.sleep(1_000);
        deleteConfirmPopup.clickYes();
        Thread.sleep(1_000);
        propertyDetail.clickSave();
        Thread.sleep(2_000);

        deletePolicyConfirmation = policiesPage.deletePolicy(policyName);
        Thread.sleep(2_000);

        deletePolicyConfirmation.clickYes();
        Thread.sleep(2_000);

        if( policyFile.delete() )
        {
            System.out.println(policyFile.getAbsolutePath() + " was deleted...");
        }

        System.out.println("--- END OF DownloadUploadPolicy ---");
    }
}
