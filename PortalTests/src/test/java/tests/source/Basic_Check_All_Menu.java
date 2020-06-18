package tests.source;

import net.portal.constants.Notifications;
import net.portal.constants.Retries;
import net.portal.forms.DeleteFollowingUsers;
import net.portal.forms.UserDetail;
import net.portal.pages.HeaderMenu;
import net.portal.pages.WakeUpPortal;
import net.portal.pages.portal_administration.Users;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;

import static tests.source.FunctionalTest.driver;

public class Basic_Check_All_Menu
{

    public void Basic_Check_All_Menu(boolean refresh) throws InterruptedException {

        //File screenshotFile = driver.switchTo().activeElement().getScreenshotAs(OutputType.FILE);
        boolean doPortalWakeUp = true;

        Thread.sleep(3_000);
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());
        WakeUpPortal wkp = new WakeUpPortal(FunctionalTest.getDriver());
        Thread.sleep(2_000);

//User & Role Management (start)

        headerMenu.clickApplication(doPortalWakeUp);
        Boolean noProblems = wkp.fixAllProblems();
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        Boolean success = driver.findElement(By.id("contentColumns")).getText().contains("Edit");
        if (success) System.out.println("User & Role Management > Application page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickProfiles(doPortalWakeUp);
        //noProblems = wkp.fixAllProblems();
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Last Modified Time");
        if (success) System.out.println("User & Role Management > Profiles page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickProfileAssignment(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Device Type");
        if (success) System.out.println("User & Role Management > Profile Assignment page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickAuthenticationStratums(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Expiration");
        if (success) System.out.println("User & Role Management > Authentication Stratums page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickAuthenticationGroups(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Stratums");
        if (success) System.out.println("User & Role Management > Authentication Groups page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickPolicies(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Upload Policy");
        if (success) System.out.println("User & Role Management > Policies page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickPolicyAssignment(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("OS Version");
        if (success) System.out.println("User & Role Management > Policy Assignment page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickArchetypes(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Description");
        if (success) System.out.println("User & Role Management > Archetypes page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickContexts(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Item Context");
        if (success) System.out.println("User & Role Management > Contexts page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickUIGroups(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Default policy values");
        if (success) System.out.println("User & Role Management > UI Groups page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickNavigationItems(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        //success = driver.findElement(By.id("contentColumns")).getText().contains("Entitlement"); //form:table_head
        success = driver.findElement(By.id("contentColumns")).getAttribute("innerHTML").contains("Entitlement");
        if (success) System.out.println("User & Role Management > Navigation Items page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickNavigation(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getAttribute("outerHTML").contains("Navigation Policies");
        if (success) System.out.println("User & Role Management > Navigation page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);
//User & Role Management (finish)

//Service Management (start)
        headerMenu.clickServiceCatalog(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Actions");
        if (success) System.out.println("Service Management > Service Catalog page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickServiceDashboard(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Project");
        if (success) System.out.println("Service Management > Service Dashboard page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickUICatalog(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Last modified");
        if (success) System.out.println("Service Management > UI Catalog page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickDBConnections(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("DB Username");
        if (success) System.out.println("Service Management > DB Connections page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);
//Service Management (finish)
//Pool Management (start)
        headerMenu.clickVDIs(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Computer domain");
        if (success) System.out.println("VDI Management > VDIs page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickPoolProviders(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("API");
        if (success) System.out.println("Pool Management > Pool Providers");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickPools(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Provider");
        if (success) System.out.println("Pool Management > Pools");
        Assert.assertTrue(success);
        Thread.sleep(2_000);
//Pool Management (finish)
//Device management (start)
        headerMenu.clickProvisioningConfig(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Service values");
        if (success) System.out.println("Device management > Provisioning Config page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickUserDevices(doPortalWakeUp); //ED-3950
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Lookup");
        if (success) System.out.println("Device management > User Devices page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);
//Device management (finish)
//Server Configuration (start)
        headerMenu.clickEnvironments(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Environment Description");
        if (success) System.out.println("Server Configuration > Environments page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickConfigs(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Timestamp");
        if (success) System.out.println("Server Configuration > Configs page exists");
        Assert.assertTrue(success);
        Thread.sleep(1_000);

        headerMenu.clickSettings(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Description:");
        if (success) System.out.println("Server Configuration > Settings page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickScheduler(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Job description");
        if (success) System.out.println("Server Configuration > Scheduler page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);
//Server Configuration (finish)
//Audit (start)
        headerMenu.clickContainer(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getAttribute("innerHTML").contains("Message");
        if (success) System.out.println("Audit > Container page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickLoginLogout(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Application");
        if (success) System.out.println("Audit > Login/Logout page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickEmailGroups(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Description");
        if (success) System.out.println("Audit > Email Groups page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickDeviceLog(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("When");
        if (success) System.out.println("Audit > Device Log page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickAlerts(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Body");
        if (success) System.out.println("Audit > Alerts page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);
//Audit (finish)
//Portal administration (start)
        headerMenu.clickUserGroups(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Users");
        if (success) System.out.println("Portal administration > User groups page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickUsers(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("User permissions");
        if (success) System.out.println("Portal administration > Users page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickDBAudit(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Date");
        if (success) System.out.println("Portal administration > DB Audit page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickRoles(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Role permissions");
        if (success) System.out.println("Portal administration > Roles page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickRoleAssignment(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        //System.out.println("driver.findElement(By.id(\"table:tableForm:entityTable_head\")).getAttribute(\"outerHTML\") : " + driver.findElement(By.id("table:tableForm:entityTable_head")).getAttribute("innerHTML"));
        success = driver.findElement(By.id("table:tableForm:entityTable_head")).getAttribute("outerHTML").contains("LDAP group");
        if (success) System.out.println("Portal administration > Role Assignment page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);
//Portal administration (finish)
//Reporting (start)
        headerMenu.clickUserDetails(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("User Sessions Statistic");
        if (success) System.out.println("Reporting > User Details page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickDocumentAudit(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Total usage per file type");
        if (success) System.out.println("Reporting > Document Audit page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickTotalLogins(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Count");
        if (success) System.out.println("Reporting > Total Logins page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickHitsPerPage(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Apply");
        if (success) System.out.println("Reporting > Hits Per Page page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickVisits(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Unique Users:");
        if (success) System.out.println("Reporting > Visits page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);

        headerMenu.clickCrashLog(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Apply");
        if (success) System.out.println("Reporting > Crash Log page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);
/* //ED-3950
        headerMenu.clickUserDevices(); //ED-3950
                if (refresh) driver.navigate().refresh();
        Thread.sleep(5_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Lookup");
        if (success) System.out.println("Device management (Reporting) > User Devices page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);
*/ //ED-3950

        headerMenu.clickActiveUsers(doPortalWakeUp);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000); else Thread.sleep(2_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        success = driver.findElement(By.id("contentColumns")).getText().contains("Working time");
        if (success) System.out.println("Reporting > Active Users page exists");
        Assert.assertTrue(success);
        Thread.sleep(2_000);
//Reporting (finish)
//Log Off (start)
        headerMenu.clickLogOff();
        Thread.sleep(2_000);
        driver.findElement(By.id("formheader:decline")).click();
        System.out.println("Log Off menu item exists");
//Log Off (finish)
    }

    @Test
    public void Basic_Check_All_Menu() throws InterruptedException {
        Basic_Check_All_Menu(false);

    }

}
