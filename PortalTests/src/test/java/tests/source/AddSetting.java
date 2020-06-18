package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.SettingDetails;
import net.portal.pages.HeaderMenu;
import net.portal.pages.server_configuration.Settings;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class AddSetting
{
    @Test
    public void addSetting() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Settings settingsPage = headerMenu.clickSettings();

        SettingDetails settingDetails = settingsPage.addSetting();
        Thread.sleep(2_000);

        String groupName = "Auto_Test GroupName",
               name = "Setting name AT",
               value = "361";

        settingDetails.setGroup(groupName);
        settingDetails.setName(name);
        settingDetails.setValue(value);
        settingDetails.clickAdd();
        Thread.sleep(3_000);

        // Check that setting was added
        Assert.assertEquals(name, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + name + "\")').parent().text()")));
        Assert.assertEquals(groupName, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + name + "\")').parent().next().text()")));
        Assert.assertEquals(value, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + name + "\")').parent().next().next().text()")));

        // Select just created setting and delete it
        settingsPage.selectSetting(name);
        Thread.sleep(2_000);

        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = settingsPage.clickDelete();
        Thread.sleep(2_000);

        Assert.assertEquals("name = " + name, followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();
        Thread.sleep(2_000);

        settingsPage.clickRefresh();

        Assert.assertEquals("", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + name + "\")').parent().text()")));

        Thread.sleep(2_000);

        // Create two settings with the same name -> should get warning
        settingDetails = settingsPage.addSetting();
        Thread.sleep(2_000);

        String theSameName = "AT_setting_007";

        settingDetails.setGroup(groupName);
        settingDetails.setName(theSameName);
        settingDetails.setValue(value);
        settingDetails.clickAdd();
        Thread.sleep(2_000);

        settingDetails = settingsPage.addSetting();
        Thread.sleep(2_000);

        settingDetails.setGroup(groupName);
        settingDetails.setName(theSameName);
        settingDetails.setValue(value);
        settingDetails.clickAdd();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SETTING_ALREADY_EXISTS.getNotificationText(), notificationPopup.getText());

        settingDetails.clickCancel();
        Thread.sleep(3_000);

        // Edit setting and set new value
        String newValue = "4207";
        settingsPage.editSetting(theSameName, newValue);
        Thread.sleep(3_000);

        settingsPage = headerMenu.clickSettings();
        Thread.sleep(3_000);

        // Check that value was changed...
        Assert.assertEquals(newValue, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + theSameName + "\")').parent().next().next().text()")));

        // Remove last setting
        settingsPage.selectSetting(theSameName);
        Thread.sleep(2_000);

        followingItemsWillBeDeleted = settingsPage.clickDelete();
        Thread.sleep(2_000);

        Assert.assertEquals("name = " + theSameName, followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();
        Thread.sleep(2_000);
    }
}
