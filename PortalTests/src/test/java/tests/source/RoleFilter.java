package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.RoleDetail;
import net.portal.pages.HeaderMenu;
import net.portal.pages.portal_administration.Roles;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class RoleFilter
{
    @Test
    public void roleFilter() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Roles rolesPage = headerMenu.clickRoles();

        // 1
        RoleDetail roleDetail = rolesPage.addNewRole();
        Thread.sleep(3_000);

        roleDetail.setRoleName("at_role_1");
        roleDetail.expandRoleNode("Reporting");
        roleDetail.selectRole("Visits");
        roleDetail.clickAdd();
        Thread.sleep(3_000);

        // 2
        roleDetail = rolesPage.addNewRole();
        Thread.sleep(3_000);

        roleDetail.setRoleName("at_role_2");
        roleDetail.expandRoleNode("Pool Management");
        roleDetail.selectRole("VDIs");
        roleDetail.selectRole("Environment select");
        roleDetail.clickAdd();
        Thread.sleep(3_000);


        // 3
        roleDetail = rolesPage.addNewRole();
        Thread.sleep(3_000);


        roleDetail.setRoleName("at_role_3");
        roleDetail.expandRoleNode("Reporting");
        roleDetail.selectRole("Visits");
        roleDetail.clickAdd();
        Thread.sleep(5_000);

        rolesPage.clickRefresh();
        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_RELOADED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(4_000);

        rolesPage.filter("Visits");
        rolesPage.clickApply();
        Thread.sleep(2_000);

        System.out.println("Assert that only roles with permissions = Visits are displayed...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(2) span:contains(\"at_role_1\")').is(':visible')"));
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(2) span:contains(\"at_role_3\")').is(':visible')"));
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(2) span:contains(\"ROLE_SUPERUSER\")').is(':visible')"));

        rolesPage.clickReset();
        Thread.sleep(2_000);

        rolesPage.filter("VDIs");
        rolesPage.clickApply();
        Thread.sleep(2_000);

        System.out.println("Assert that only roles with permissions = VDIs are displayed...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(2) span:contains(\"at_role_2\")').is(':visible')"));
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(2) span:contains(\"ROLE_SUPERUSER\")').is(':visible')"));

        rolesPage.selectRole("at_role_2");
        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = rolesPage.deleteRole();
        Thread.sleep(3_000);

        System.out.println("Delete one role with VDI...");
        Assert.assertEquals("name = at_role_2", followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();
        Thread.sleep(3_000);

        // Apply VDI filter
        rolesPage.filter("VDIs");
        rolesPage.clickApply();
        Thread.sleep(3_000);

        System.out.println("Assert that there is only one role...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(2) span:contains(\"ROLE_SUPERUSER\")').is(':visible')"));

        rolesPage.clickReset();
        Thread.sleep(3_000);

        System.out.println("Other two roles should be in the list...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"at_role_1\")').is(':visible')"));
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"at_role_3\")').is(':visible')"));
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"ROLE_SUPERUSER\")').is(':visible')"));
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"ROLE_USER\")').is(':visible')"));

        System.out.println("Remove remain two roles... Visit Roles page again...");
        rolesPage = headerMenu.clickRoles();
        Thread.sleep(3_000);

        rolesPage.selectRole("at_role_1");
        rolesPage.selectRole("at_role_3");

        followingItemsWillBeDeleted = rolesPage.deleteRole();
        Thread.sleep(3_000);

        Assert.assertEquals("name = at_role_1name = at_role_3", followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();
        Thread.sleep(5_000);

        rolesPage.clickReset();
        Thread.sleep(2_000);

        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"ROLE_SUPERUSER\")').is(':visible')"));
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"ROLE_USER\")').is(':visible')"));
    }
}
