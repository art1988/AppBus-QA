package tests.source;

import net.portal.constants.Const;
import net.portal.forms.ConfigDetails;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.pages.HeaderMenu;
import net.portal.pages.server_configuration.Configs;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

public class Basic_AddConfig
{
    @Test
    public void basic_AddConfig() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Configs configsPage = headerMenu.clickConfigs();

        ConfigDetails configDetailsForm = configsPage.addNewConfig();
        Thread.sleep(6_000);

        String configName = "BASIC_Config";

        configDetailsForm.setName(configName);
        configDetailsForm.chooseFile(Const.TEXT_FILE_SAMPLE);
        configDetailsForm.clickUpload();
        Thread.sleep(8_000);

        configDetailsForm.clickAdd();
        Thread.sleep(3_000);

        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = configsPage.deleteConfig(configName);
        Thread.sleep(6_000);

        followingItemsWillBeDeleted.clickDelete();
        Thread.sleep(5_000);

        Assert.assertEquals("", ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:contains(\"" + configName + "\")').text()"));
        //$('#table\\:tableForm\\:entityTable_data tr td,td span:contains("BASIC_config")').text()
    }
}
