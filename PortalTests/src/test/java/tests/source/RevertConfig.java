package tests.source;

import net.portal.constants.Const;
import net.portal.constants.Notifications;
import net.portal.forms.ConfigDetails;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.RestorePreviousConfig;
import net.portal.pages.HeaderMenu;
import net.portal.pages.server_configuration.Configs;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class RevertConfig
{
    @Test
    public void revertConfig() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Configs configsPage = headerMenu.clickConfigs();

        ConfigDetails configDetailsForm = configsPage.addNewConfig();
        Thread.sleep(2_000);

        String configName = "Aa_nonBin_Revert_Test";

        configDetailsForm.setName(configName);
        configDetailsForm.chooseFile(Const.TEXT_FILE_SAMPLE);
        configDetailsForm.clickUpload();
        Thread.sleep(6_000);

        // Uncheck binary checkbox...
        configDetailsForm.clickBinaryCheckbox();
        Thread.sleep(1_000);

        configDetailsForm.clickAdd();
        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_ADDED.getNotificationText(), notificationPopup.getText());

        Thread.sleep(4_000);

        // Edit just added config and set new Context
        configDetailsForm = configsPage.editConfig(configName);
        Thread.sleep(3_000);

        configDetailsForm.setContent("I am new line");

        configDetailsForm.clickSave();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_UPDATED.getNotificationText(), notificationPopup.getText());

        Thread.sleep(4_000);

        System.out.println("Making sure that 'Revert previous version' icon is active...");

        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + configName + "\")').parent().next().next().find(\"button\").eq(2).is(':visible')"));

        System.out.println("Edit just added config and make sure that new content was saved...");
        configDetailsForm = configsPage.editConfig(configName);
        Thread.sleep(3_000);

        Assert.assertEquals("I am new line", configDetailsForm.getContent());

        configDetailsForm.clickCancel();
        Thread.sleep(3_000);

        RestorePreviousConfig restorePreviousConfigPopup = configsPage.restorePreviousConfig(configName);
        Thread.sleep(2_000);

        restorePreviousConfigPopup.clickYes();
        Thread.sleep(2_000);

        configDetailsForm = configsPage.editConfig(configName);
        Thread.sleep(3_000);

        String iniFileContent = configDetailsForm.getContent();
        Assert.assertTrue(iniFileContent.contains("[drivers]"));
        Assert.assertTrue(iniFileContent.contains("[386Enh]"));

        // set new line again
        configDetailsForm.setContent("I am new line 2");

        configDetailsForm.clickSave();
        Thread.sleep(3_000);

        System.out.println("Trying to delete config that has 'able to revert' status... [ED-4013]"); // Checking of ED-4013
        configsPage = headerMenu.clickConfigs();
        Thread.sleep(3_000);


        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = configsPage.deleteConfig(configName);
        Thread.sleep(2_000);

        followingItemsWillBeDeleted.clickDelete();
        Thread.sleep(2_000);

        System.out.println("Checking that item is no longer in the list...");
        Assert.assertFalse((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(2) span:contains(\"" + configName + "\")').is(':visible')"));

        Thread.sleep(2_000);


        System.out.println("Check that restore previous config affects Binary(Non-binary) mark... [ED-4019]"); // Checking of ED-4019
        configName = "A_binOrTxt";

        configDetailsForm = configsPage.addNewConfig();
        Thread.sleep(2_000);

        configDetailsForm.setName(configName);
        configDetailsForm.chooseFile(Const.BINARY_FILE_SAMPLE);
        configDetailsForm.clickUpload();
        Thread.sleep(6_000);

        configDetailsForm.clickAdd();
        Thread.sleep(2_000);

        configDetailsForm = configsPage.editConfig(configName);
        Thread.sleep(3_000);

        configDetailsForm.chooseFile(Const.TEXT_FILE_SAMPLE);
        configDetailsForm.clickUpload();
        Thread.sleep(6_000);

        // Uncheck bin mark
        configDetailsForm.clickBinaryCheckbox();
        Thread.sleep(2_000);

        configDetailsForm.clickSave();
        Thread.sleep(3_000);

        System.out.println("Check that binary mark is off...");
        Assert.assertTrue(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + configName + "\")').parent().next().find('img').attr(\"src\")").equals("/edapt-admin/images/x-mark-24.png"));

        restorePreviousConfigPopup = configsPage.restorePreviousConfig(configName);
        Thread.sleep(2_000);

        restorePreviousConfigPopup.clickYes();
        Thread.sleep(2_000);

        System.out.println("Check that binary mark is on after restoring...");
        Assert.assertTrue(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + configName + "\")').parent().next().find('img').attr(\"src\")").equals("/edapt-admin/images/ok-mark-24.png"));

        followingItemsWillBeDeleted = configsPage.deleteConfig(configName);
        Thread.sleep(2_000);

        // todo: add assert of name of del

        followingItemsWillBeDeleted.clickDelete();
        Thread.sleep(2_000);
    }
}
