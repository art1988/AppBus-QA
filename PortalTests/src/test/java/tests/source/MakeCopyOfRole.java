package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.RoleAssignmentDetail;
import net.portal.forms.RoleDetail;
import net.portal.pages.HeaderMenu;
import net.portal.pages.portal_administration.RoleAssignment;
import net.portal.pages.portal_administration.Roles;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class MakeCopyOfRole
{
    @Test
    public void makeCopyOfRole() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Roles rolesPage = headerMenu.clickRoles();

        RoleDetail roleDetail = rolesPage.addNewRole();
        Thread.sleep(3_000);

        String roleName = "Role_copy_me";

        roleDetail.setRoleName(roleName);

        roleDetail.expandRoleNode("Service Management");
        roleDetail.selectRole("DB Connections");

        roleDetail.expandRoleNode("Server configs");
        roleDetail.selectRole("Configs");

        roleDetail.setRoleLandingPermission("DB_CONNECTIONS");

        roleDetail.clickAdd();
        Thread.sleep(3_000);

        System.out.println("Make copy of role : " + roleName);
        roleDetail = rolesPage.copyRole(roleName);
        Thread.sleep(3_000);

        roleDetail.setRoleName("COPY OF : originalRole");
        roleDetail.clickAdd();
        Thread.sleep(3_000);

        System.out.println("Delete original role item...");
        rolesPage.selectRole(roleName);
        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = rolesPage.deleteRole();
        Thread.sleep(3_000);

        Assert.assertEquals("name = Role_copy_me", followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();
        Thread.sleep(3_000);

        System.out.println("Making sure that copy has the same permissions as original...");
        // Check Role name
        Assert.assertEquals("COPY OF : originalRole", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"COPY\")').parent().text()")));
        // Check Role landing permission
        Assert.assertEquals("DB Connections", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"COPY\")').parent().next().text()")));
        // Check Role permissions
        Assert.assertEquals("Service Management (DB Connections); Server configs (Configs)", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"COPY\")').parent().next().next().text()")));

        System.out.println("Go to 'Role Assignment' page and check that copy is in the list...");
        RoleAssignment roleAssignmentPage = headerMenu.clickRoleAssignment();

        RoleAssignmentDetail roleAssignmentDetail = roleAssignmentPage.addNewRoleAssignment();
        Thread.sleep(3_000);

        // Expand Role dropdown
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#entity\\\\:dialogsForm\\\\:property-role span').click()");
        Thread.sleep(2_000);

        // Check that copy is on the list
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entity\\\\:dialogsForm\\\\:property-role_items li:contains(\"COPY\")').is(':visible')"));

        // Collapse Role dropdown
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#entity\\\\:dialogsForm\\\\:property-role span').click()");
        Thread.sleep(2_000);

        roleAssignmentDetail.clickCancel();
        Thread.sleep(3_000);

        // After-test routine: go back to Roles and delete COPY
        rolesPage = headerMenu.clickRoles();

        rolesPage.selectRole("COPY OF");
        followingItemsWillBeDeleted = rolesPage.deleteRole();
        Thread.sleep(3_000);

        Assert.assertEquals("name = COPY OF : originalRole", followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());
    }
}
