package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.ItemAssignmentDetails;
import net.portal.forms.SelectPolicyOverride;
import net.portal.pages.DeleteItemPopup;
import net.portal.pages.HeaderMenu;
import net.portal.pages.user_and_role_management.Navigation;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import static tests.source.FunctionalTest.driver;

public class NavigationItemOverride
{
    @Test
    public void navigationItemOverride() throws InterruptedException
    {
        System.out.println("--- START OF NavigationItemOverride ---");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Navigation navigationPage = headerMenu.clickNavigation();

        navigationPage.selectProfile("AKM"); // AKM profile should exist with added bottomFixedGroup
        Thread.sleep(3_000);

        navigationPage.selectUIgrp("bottom");
        Thread.sleep(3_000);

        ItemAssignmentDetails itemAssignmentDetails = navigationPage.addNavigationItem();
        Thread.sleep(3_000);

        itemAssignmentDetails.selectItem("documents");
        Thread.sleep(3_000);

        itemAssignmentDetails.clickOverrideCheckbox();
        Thread.sleep(3_000);

        itemAssignmentDetails.setOverridePropertyValue("type", "documents_overriden"); // override type policy with new value

        SelectPolicyOverride selectPolicy = itemAssignmentDetails.addControllerPolicy();
        Thread.sleep(3_000);

        selectPolicy.selectPolicy("persistent");
        selectPolicy.clickOk();
        Thread.sleep(2_000);

        selectPolicy = itemAssignmentDetails.addNavigationPolicy();
        Thread.sleep(3_000);

        selectPolicy.selectPolicy("defaultMark");
        selectPolicy.clickOk();
        Thread.sleep(2_000);

        itemAssignmentDetails.setOverridePropertyValue("defaultMark", "false"); // set value for new added navigation policy

        itemAssignmentDetails.clickAdd();
        Thread.sleep(3_000);

        System.out.println("Asserting that overridden values were applied...");

        Assert.assertEquals("ID:documents", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entityTable tr td:nth-child(1) div:contains(\"ID\"):even').text().replace(/\\n/g,\"\").replace(/\\s/g, '')")));
        Assert.assertEquals("persistenttypedocuments_overridenurlmaps51doc:///webGroupdoc", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entityTable_data tbody:eq(0)').text()")));
        Assert.assertEquals("allowedOfflinetruedefaultMarkfalse", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entityTable_data tbody:eq(1)').text()")));

        // Delete just created nav.item
        DeleteItemPopup deleteItemPopup = navigationPage.deleteItem("documents");
        Thread.sleep(3_000);

        deleteItemPopup.clickYes();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.ITEM_WAS_REMOVED.getNotificationText(), notificationPopup.getText());

        System.out.println("--- END OF NavigationItemOverride ---");
    }
}
