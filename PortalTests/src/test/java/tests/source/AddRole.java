package tests.source;

import net.portal.constants.Const;
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

import java.io.File;

public class AddRole
{
    @Test
    public void addRole() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Roles rolesPage = headerMenu.clickRoles();

        RoleDetail roleDetail = rolesPage.addNewRole();
        Thread.sleep(1_000);

        String roleName = "UniqueName";

        roleDetail.setRoleName(roleName);

        roleDetail.expandRoleNode("Server configs");
        roleDetail.selectRole("Configs");

        roleDetail.expandRoleNode("Portal administration");
        roleDetail.selectRole("Roles");
        roleDetail.selectRole("User groups");

        roleDetail.setRoleLandingPermission("CONFIGS");

        roleDetail.clickAdd();
        Thread.sleep(3_000);

        // Check that Role landing permission = CONFIGS
        Assert.assertEquals("Configs", ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + roleName + "\")').parent().next().text()"));

        System.out.println("Download just created role...");
        rolesPage.clickDownload(roleName);
        Thread.sleep(3_000);

        rolesPage.selectRole(roleName);
        Thread.sleep(3_000);

        System.out.println("Delete just created role...");
        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = rolesPage.deleteRole();
        Thread.sleep(2_000);
        Assert.assertEquals("name = " + roleName, followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();
        Thread.sleep(2_000);

        System.out.println("Create new role from file...");
        File roleFile = new File(Const.DOWNLOAD_FOLDER + "\\" + roleName + ".txt");

        roleDetail = rolesPage.addNewRole();
        Thread.sleep(2_000);
        roleDetail.setRoleName(roleName);
        roleDetail.chooseFile(roleFile.getAbsolutePath());
        roleDetail.clickUpload();
        Thread.sleep(4_000);
        roleDetail.clickAdd();
        Thread.sleep(3_000);

        System.out.println("Check that role was added successfully... Visit Role page again to refresh...");
        rolesPage = headerMenu.clickRoles();
        Thread.sleep(3_000);

        Assert.assertEquals("Configs", ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + roleName + "\")').parent().next().text()"));
        Assert.assertEquals("Server configs (Configs); Portal administration (User groups, Roles)", ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + roleName + "\")').parent().next().next().text()"));

        System.out.println("Trying to add new role with the same name...");

        roleDetail = rolesPage.addNewRole();
        Thread.sleep(2_000);

        roleDetail.setRoleName(roleName);
        roleDetail.expandRoleNode("Audit");
        roleDetail.selectRole("Alerts");
        Thread.sleep(2_000);

        roleDetail.clickAdd();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.ROLE_NAME_SHOULD_BE_UNIQUE_FOR_ENVIRONMENT.getNotificationText(), notificationPopup.getText());

        roleDetail.clickCancel();
        Thread.sleep(2_000);

        // After-test routine: delete created role and downloaded file

        rolesPage.selectRole(roleName);
        followingItemsWillBeDeleted = rolesPage.deleteRole();
        Thread.sleep(2_000);

        Assert.assertEquals("name = " + roleName, followingItemsWillBeDeleted.getListOfItemsToDelete());

        followingItemsWillBeDeleted.clickDelete();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

        // delete file...
        if( roleFile.delete() )
        {
            System.out.println(roleFile.getAbsolutePath() + " was successfully deleted...");
        }

        Thread.sleep(4_000);
    }
}
