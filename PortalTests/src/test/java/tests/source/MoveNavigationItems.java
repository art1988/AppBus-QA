package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.ItemAssignmentDetails;
import net.portal.forms.MoveToItemAsChild;
import net.portal.forms.MoveToRoot;
import net.portal.forms.SelectParentItem;
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

public class MoveNavigationItems
{
    @Test
    public void moveNavigationItems() throws InterruptedException
    {
        System.out.println("--- START OF MoveNavigationItems ---");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        NavigationItems navigationItemsPage = headerMenu.clickNavigationItems();

        ItemAssignmentDetails itemAssignmentDetails = navigationItemsPage.addNavigationItem();
        Thread.sleep(2_000);

        String navItemId = "A_move_me";

        itemAssignmentDetails.setId(navItemId);

        itemAssignmentDetails.clickSave();
        Thread.sleep(7_000);

        navigationItemsPage.clickRefresh();
        Thread.sleep(7_000);

        SelectParentItem selectParentItemPopup = navigationItemsPage.moveToAnotherItemAsChild(navItemId);
        Thread.sleep(3_000);

        selectParentItemPopup.selectParentItem("barcodeMedical");
        Thread.sleep(2_000);

        MoveToItemAsChild moveToItemAsChildPopup = selectParentItemPopup.clickOk();
        Thread.sleep(4_000);

        moveToItemAsChildPopup.clickYes();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.ITEM_WAS_MOVED.getNotificationText(), notificationPopup.getText());

        System.out.println("Click barcodeMedical link...");
        navigationItemsPage = navigationItemsPage.clickNavigationItemLink("barcodeMedical");
        Thread.sleep(6_000);

        Assert.assertEquals("ROOT \u2192 barcodeMedical", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:breadcrumb_content').text()")));
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:contains(\"" + navItemId + "\")').is(':visible')"));

        MoveToRoot moveToRootPopup = navigationItemsPage.moveToTheRootLevel(navItemId);
        Thread.sleep(2_000);

        moveToRootPopup.clickYes();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.ITEM_WAS_MOVED.getNotificationText(), notificationPopup.getText());

        navigationItemsPage = navigationItemsPage.clickROOTLink();
        Thread.sleep(5_000);

        System.out.println("Making sure that nav item is on the ROOT list...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:contains(\"" + navItemId + "\")').is(':visible')"));

        DeleteNavigationItemPopup deleteNavigationItemPopup = navigationItemsPage.deleteNavigationItem(navItemId);
        Thread.sleep(2_000);

        deleteNavigationItemPopup.clickYes();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

        Assert.assertFalse((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:table_data td:contains(\"" + navItemId + "\")').is(':visible')"));

        System.out.println("--- END OF MoveNavigationItems ---");
    }
}
