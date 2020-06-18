package tests.source;

import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.SettingDetails;
import net.portal.pages.HeaderMenu;
import net.portal.pages.server_configuration.Settings;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

public class SettingsGroupFilter
{
    @Test
    public void settingsGroupsFilter() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Settings settingsPage = headerMenu.clickSettings();

        addSetting(settingsPage, "default", "Sett_1", "11");
        addSetting(settingsPage, "default", "Sett_2", "22");

        addSetting(settingsPage, "job", "A.setting.a", "a");
        addSetting(settingsPage, "job", "B.setting.b", "b");
        addSetting(settingsPage, "job", "C.setting.c", "c");

        settingsPage.selectGroup("default");
        System.out.println("Making sure that settings of group 'default' are displayed...");

        Assert.assertTrue(String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data td:nth-child(2)').text()")).contains("Sett_1Sett_2"));
        // Make sure that records are 3 for group default
        Assert.assertTrue(Integer.parseInt(String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr').length;"))) == 3);

        settingsPage.clickReset();

        // Check that filter was reset
        Assert.assertEquals("---- All ----", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#settings\\\\:groupFilter_label').text()")));
        Assert.assertTrue(Integer.parseInt(String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr').length;"))) > 0);

        settingsPage.selectGroup("job");
        Thread.sleep(2_000);
        // Make sure that records are 18 for group job
        Assert.assertTrue(Integer.parseInt(String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr').length;"))) == 18);

        Assert.assertTrue(String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data td:nth-child(2)').text()")).contains("A.setting.aB.setting.bC.setting.c"));

        // Stay on the group job and select just created for this group...

        settingsPage.selectSetting("A.setting.a");
        settingsPage.selectSetting("B.setting.b");
        settingsPage.selectSetting("C.setting.c");

        FollowingItemsWillBeDeleted followingItemsWillBeDeletedPopup = settingsPage.clickDelete();
        Thread.sleep(3_000);

        Assert.assertEquals("name = A.setting.aname = B.setting.bname = C.setting.c", followingItemsWillBeDeletedPopup.getListOfItemsToDelete());

        followingItemsWillBeDeletedPopup.clickDelete();
        Thread.sleep(3_000);

        settingsPage.selectGroup("default");

        settingsPage.selectSetting("Sett_1");
        settingsPage.selectSetting("Sett_2");

        followingItemsWillBeDeletedPopup = settingsPage.clickDelete();
        Thread.sleep(3_000);

        Assert.assertEquals("name = Sett_1name = Sett_2", followingItemsWillBeDeletedPopup.getListOfItemsToDelete());

        followingItemsWillBeDeletedPopup.clickDelete();
        Thread.sleep(3_000);

        settingsPage.clickReset();

        System.out.println("Making sure that filter was reset and records doesn't have deleted items...");
        Assert.assertTrue(Integer.parseInt(String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr').length;"))) == 16);

        Thread.sleep(2_000);
    }

    private void addSetting(Settings settingsPage, String groupName, String name, String value) throws InterruptedException
    {
        SettingDetails settingDetails = settingsPage.addSetting();
        Thread.sleep(1_000);

        settingDetails.setGroup(groupName);
        settingDetails.setName(name);
        settingDetails.setValue(value);

        settingDetails.clickAdd();

        Thread.sleep(2_000);
    }
}
