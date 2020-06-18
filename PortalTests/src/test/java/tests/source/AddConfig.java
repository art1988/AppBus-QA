package tests.source;

import net.portal.constants.Const;
import net.portal.forms.ConfigDetails;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.pages.server_configuration.Configs;
import net.portal.pages.HeaderMenu;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

import java.io.File;

public class AddConfig
{
    @Test
    public void addConfig() throws InterruptedException
    {
        makeFolderForFileSamples();

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Configs configsPage = headerMenu.clickConfigs();

        ConfigDetails configDetailsForm = configsPage.addNewConfig();

        /* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
        System.out.println("Adding of [binary] config...");

        String configName = "Config autotest binary";
        configDetailsForm.setName(configName);
        configDetailsForm.chooseFile(Const.BINARY_FILE_SAMPLE);
        configDetailsForm.clickUpload();
        Thread.sleep(8_000);

        // Binary checkbox is checked by default, let's get content
        Assert.assertEquals("Content representation is not available for binary configs.", configDetailsForm.getContent());

        configDetailsForm.clickAdd();
        Thread.sleep(7_000);

        System.out.println("Check that config was added...");
        Assert.assertTrue(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + configName + "\")').text()").equals(configName));

        System.out.println("Check that it has binary mark...");
        Assert.assertTrue(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + configName + "\")').parent().next().find('img').attr(\"src\")").equals("/edapt-admin/images/ok-mark-24.png"));

        System.out.println("Check that view content button is disabled...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + configName + "\")').parent().next().next().find('button')[0].hasAttribute(\"disabled\")"));

        System.out.println("Trying to download binary config...");
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + configName + "\")').parent().next().next().find('button')[1].click()");
        Thread.sleep(4_000);
        File binaryFile = new File(Const.DOWNLOAD_FOLDER + "\\" + configName);
        Assert.assertTrue(binaryFile.exists());

        // Edit binary config: change it's name...
        configDetailsForm = configsPage.editConfig(configName);
        Thread.sleep(1_000);

        configName += " [edited]";
        configDetailsForm.setName(configName);
        configDetailsForm.clickSave();
        Thread.sleep(4_000);

        // Check that name was changed
        Assert.assertTrue(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + configName + "\")').text()").equals(configName));

        System.out.println("Deleting of binary config...");
        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = configsPage.deleteConfig(configName);

        Assert.assertEquals("name = " + configName, followingItemsWillBeDeleted.getListOfItemsToDelete());

        followingItemsWillBeDeleted.clickDelete();
        Thread.sleep(3_000);

        /* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
        System.out.println("Adding of [non-binary] config...");

        configDetailsForm = configsPage.addNewConfig();
        Thread.sleep(2_000);

        configName = "Config autotest non-binary";
        configDetailsForm.setName(configName);
        configDetailsForm.chooseFile(Const.TEXT_FILE_SAMPLE);
        configDetailsForm.clickUpload();
        Thread.sleep(6_000);

        // Uncheck binary checkbox...
        configDetailsForm.clickBinaryCheckbox();
        Thread.sleep(3_000);

        // ...and get file content
        String iniFileContent = configDetailsForm.getContent();
        Assert.assertTrue(iniFileContent.contains("[drivers]"));
        Assert.assertTrue(iniFileContent.contains("[386Enh]"));

        configDetailsForm.clickAdd();
        Thread.sleep(3_000);

        System.out.println("Check that config was added... Visit Configs page again to refresh...");
        configsPage = headerMenu.clickConfigs();
        Thread.sleep(3_000);

        Assert.assertTrue(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + configName + "\")').text()").equals(configName));

        System.out.println("Check that it has non-binary mark...");
        Assert.assertTrue(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + configName + "\")').parent().next().find('img').attr(\"src\")").equals("/edapt-admin/images/x-mark-24.png"));

        System.out.println("Check that view content button is enabled...");
        Assert.assertFalse((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + configName + "\")').parent().next().next().find('button')[0].hasAttribute(\"disabled\")"));

        System.out.println("Trying to download non-binary config...");
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + configName + "\")').parent().next().next().find('button')[1].click()");
        Thread.sleep(4_000);
        File nonBinaryFile = new File(Const.DOWNLOAD_FOLDER + "\\" + configName);
        Assert.assertTrue(nonBinaryFile.exists());

        // Edit non-binary config: upload new file...
        configDetailsForm = configsPage.editConfig(configName);
        Thread.sleep(1_000);

        configDetailsForm.chooseFile(Const.TEXT_FILE_SAMPLE_2);
        configDetailsForm.clickUpload();
        Thread.sleep(6_000);

        String logFileContent = configDetailsForm.getContent();

        Assert.assertTrue(logFileContent.contains("ETW"));
        Assert.assertTrue(logFileContent.contains("PowerShell"));

        configDetailsForm.clickSave();
        Thread.sleep(5_000);

        // Visit non-binary config and check modified content
        configDetailsForm = configsPage.editConfig(configName);
        Thread.sleep(3_000);

        logFileContent = configDetailsForm.getContent();

        Assert.assertTrue(logFileContent.contains("ETW"));
        Assert.assertTrue(logFileContent.contains("PowerShell"));

        configDetailsForm.clickCancel();
        Thread.sleep(3_000);

        System.out.println("Deleting of non-binary config...");
        followingItemsWillBeDeleted = configsPage.deleteConfig(configName);

        Assert.assertEquals("name = Config autotest non-binary", followingItemsWillBeDeleted.getListOfItemsToDelete());

        followingItemsWillBeDeleted.clickDelete();
        Thread.sleep(3_000);

        // After-test clean-up: delete downloaded files
        if(binaryFile.delete() && nonBinaryFile.delete())
        {
            System.out.println(binaryFile.getAbsolutePath() + " and " + nonBinaryFile.getAbsolutePath() + " were deleted");
        } else
        {
            System.err.println("Unable to delete " + binaryFile.getAbsolutePath() + " or " + nonBinaryFile.getAbsolutePath());
        }
    }

    private static void makeFolderForFileSamples()
    {
        File samplesFolder = new File(System.getProperty("user.dir") + "\\Samples");

        if( !samplesFolder.exists() )
        {
            if( samplesFolder.mkdirs() )
            {
                System.out.println("Sample folder was created...");
            }
            else
            {
                System.err.println("Error: Unable to create Sample folder !");
            }
        }
        else
        {
            System.out.println("Sample folder is already exists...");
        }
    }
}
