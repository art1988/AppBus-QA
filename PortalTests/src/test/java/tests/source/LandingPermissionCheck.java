package tests.source;

import net.portal.constants.Const;
import net.portal.constants.Notifications;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.RoleAssignmentDetail;
import net.portal.forms.RoleDetail;
import net.portal.pages.HeaderMenu;
import net.portal.pages.LoginPage;
import net.portal.pages.portal_administration.RoleAssignment;
import net.portal.pages.portal_administration.Roles;
import net.portal.pages.server_configuration.Configs;
import net.portal.pages.pool_management.VDIs;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class LandingPermissionCheck
{
    @Test
    public void landingPermissionCheck() throws InterruptedException
    {
        // should be logged in as edapt-setup
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Roles rolesPage = headerMenu.clickRoles();

        RoleDetail roleDetail = rolesPage.addNewRole();

        String roleName = "LandingPermissionCheck_AT2";

        roleDetail.setRoleName(roleName);
        roleDetail.expandRoleNode("Pool Management");
        roleDetail.selectRole("VDIs");

        roleDetail.expandRoleNode("Server configs");
        roleDetail.selectRole("Configs");

        roleDetail.expandRoleNode("Portal administration");
        roleDetail.selectRole("Roles");

        roleDetail.setRoleLandingPermission("VDIS");

        roleDetail.clickAdd();
        Thread.sleep(3_000);

        // Go to Role Assignment page
        RoleAssignment roleAssignmentPage = headerMenu.clickRoleAssignment();

        RoleAssignmentDetail roleAssignmentDetail = roleAssignmentPage.addNewRoleAssignment();
        Thread.sleep(3_000);

        roleAssignmentDetail.setRole(roleName);
        roleAssignmentDetail.setUser("qadev@botf03.net");

        roleAssignmentDetail.clickAdd();
        Thread.sleep(5_000);

        System.out.println("Login as qadev...");
        LoginPage loginPage = headerMenu.clickLogOff().clickOk();

        loginPage.enterUserName(Const.USER_QADEV);
        loginPage.enterPassword(Const.PASSWORD);

        loginPage.clickLogin();

        System.out.println("Check that landing page is VDIs...");
        VDIs vdIsPage = new VDIs(FunctionalTest.getDriver());
        Assert.assertNotNull(vdIsPage);

        System.out.println("Check that header menu has only 3 menu items with one subitem in each item...");

        String menuItems = String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('.main-menu').text().trim().replace(/\\n/g,\"\").replace(/\\s/g, '')"));

        Assert.assertEquals("PoolManagementVDIsServerConfigurationConfigsPortalAdministrationRoles", menuItems);

        System.out.println("Login back as edaps-setup and change landing page and remove one page...");
        loginPage = headerMenu.clickLogOff().clickOk();

        loginPage.enterUserName(Const.USER_EDAPT);
        loginPage.enterPassword(Const.PASSWORD);

        loginPage.clickLogin();

        rolesPage = headerMenu.clickRoles();
        roleDetail = rolesPage.editRole(roleName);
        Thread.sleep(3_000);

        roleDetail.setRoleLandingPermission("CONFIGS");

        roleDetail.expandRoleNode("Pool Management");
        roleDetail.selectRole("VDIs"); // Unselect VDI management page
        roleDetail.clickSave();
        Thread.sleep(5_000);

        System.out.println("Login as qadev and check that landing page is Configs...");
        loginPage = headerMenu.clickLogOff().clickOk();

        loginPage.enterUserName(Const.USER_QADEV);
        loginPage.enterPassword(Const.PASSWORD);

        loginPage.clickLogin();
        Thread.sleep(4_000);

        Configs configsPage = new Configs(FunctionalTest.getDriver());
        Assert.assertNotNull(configsPage);

        System.out.println("Check that header menu has only 2 menu items(without VDIs) with one subitem in each item...");
        menuItems = String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('.main-menu').text().trim().replace(/\\n/g,\"\").replace(/\\s/g, '')"));

        // TODO: need to change expected value after fixing of ED-3508 : it has VDI Management, but shouldn't
        Assert.assertEquals("ServerConfigurationConfigsPortalAdministrationRoles", menuItems);

        // After-test cleanup routine
        loginPage = headerMenu.clickLogOff().clickOk();

        loginPage.enterUserName(Const.USER_EDAPT);
        loginPage.enterPassword(Const.PASSWORD);

        loginPage.clickLogin();

        // go to role assignment
        roleAssignmentPage = headerMenu.clickRoleAssignment();
        roleAssignmentPage.selectRoleAssignment(roleName);
        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = roleAssignmentPage.deleteRoleAssignment();
        Thread.sleep(3_000);

        followingItemsWillBeDeleted.clickDelete();

        Thread.sleep(5_000);

        // go to roles
        rolesPage = headerMenu.clickRoles();
        rolesPage.selectRole(roleName);
        followingItemsWillBeDeleted = rolesPage.deleteRole();
        Thread.sleep(3_000);

        Assert.assertEquals("name = " + roleName, followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

        Thread.sleep(3_000);
    }
}
