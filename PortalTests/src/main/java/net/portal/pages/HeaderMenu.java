package net.portal.pages;

import net.portal.constants.Retries;
import net.portal.forms.LogOff;
import net.portal.pages.audit.*;
import net.portal.pages.device_management.ProvisioningConfig;
import net.portal.pages.device_management.UserDevices;
import net.portal.pages.pool_management.PoolProviders;
import net.portal.pages.pool_management.VDIs;
import net.portal.pages.portal_administration.DBAudit;
import net.portal.pages.portal_administration.RoleAssignment;
import net.portal.pages.portal_administration.Roles;
import net.portal.pages.portal_administration.Users;
import net.portal.pages.reporting.*;
import net.portal.pages.server_configuration.Configs;
import net.portal.pages.server_configuration.Environments;
import net.portal.pages.server_configuration.Scheduler;
import net.portal.pages.server_configuration.Settings;
import net.portal.pages.service_management.DBConnections;
import net.portal.pages.service_management.ServiceCatalog;
import net.portal.pages.service_management.ServiceDashboard;
import net.portal.pages.service_management.UICatalog;
import net.portal.pages.user_and_role_management.*;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.FindBy;

public class HeaderMenu extends PageObject
{
    @FindBy(id = "close-menu")
    private WebElement closeMenuTriangle;

    @FindBy(id = "environmentForm:environmentSelect_label")
    private WebElement environmentDropDown;

    @FindBy(id = "formheader:logoutMenuItem")
    private WebElement logoffButton;

    @FindBy(id = "sidebar")
    private WebElement leftBar;

    @FindBy(id = "userAndRoleManagementMenuItem")
    private WebElement userAndRoleManagement;

    @FindBy(id = "content_header")
    private WebElement contentHeader;

        @FindBy(id = "profilesSubMenuItem")
        private WebElement usrAndRlMngmtProfiles;

        @FindBy(id = "applicationsSubMenuItem")
        private WebElement usrAndRlMngmtApplications;

        @FindBy(id = "profileAssignmentSubMenuItem")
        private WebElement usrAndRlMngmtProfileAssignments;

        @FindBy(id = "authenticationStratumsSubMenuItem")
        private WebElement usrAndRlMngmtAuthStratums;

        @FindBy(id = "authenticationGroupsSubMenuItem")
        private WebElement usrAndRlMngmtAuthGroups;

        @FindBy(id = "policiesSubMenuItem")
        private WebElement usrAndRlMngmtPolicies;

        @FindBy(id = "policyAssignmentSubMenuItem")
        private WebElement usrAndRlMngmtPolicyAssignments;

        @FindBy(id = "archetypesSubMenuItem")
        private WebElement usrAndRlMngmtArchetypes;

        @FindBy(id = "contextsSubMenuItem")
        private WebElement usrAndRlMngmtContexts;

        @FindBy(id = "uiGroupsSubMenuItem")
        private WebElement usrAndRlMngmtUIgroups;

        @FindBy(id = "navigationItemsSubMenuItem")
        private WebElement usrAndRlMngmtNavigationItems;

        @FindBy(id = "navigationSubMenuItem")
        private WebElement usrAndRlMngmtNavigation;

    @FindBy(id = "serverConfigsMenuItem")
    private WebElement serverConfiguration;

        @FindBy(id = "environmentsSubMenuItem")
        private WebElement srvrCnfgrtnEnvironments;

        @FindBy(id = "configsSubMenuItem")
        private WebElement srvrCnfgrtnConfigs;

        @FindBy(id = "settingsSubMenuItem")
        private WebElement srvrCnfgrtnSettings;

        @FindBy(id = "schedulerSubMenuItem")
        private WebElement srvrCnfgrtnScheduler;

    @FindBy(id = "auditMenuItem")
    private WebElement audit;

        @FindBy(id = "containerSubMenuItem")
        private WebElement auditContainer;

        @FindBy(id = "loginLogoutSubMenuItem")
        private WebElement auditLoginLogout;

        @FindBy(id = "emailGroupsSubMenuItem")
        private WebElement auditEmailGroups;

        @FindBy(id = "deviceLogSubMenuItem")
        private WebElement auditDeviceLog;

        @FindBy(id = "alertsSubMenuItem")
        private WebElement auditAlerts;

    @FindBy(id = "portalAdministrationMenuItem")
    private WebElement portalAdministration;

        @FindBy(id = "userGroupsSubMenuItem")
        private WebElement prtlAdmnUserGroups;

        @FindBy(id = "usersSubMenuItem")
        private WebElement prtlAdmnUsers;

        @FindBy(id = "dbAuditSubMenuItem")
        private WebElement prtlAdmnDBaudit;

        @FindBy(id = "rolesSubMenuItem")
        private WebElement prtlAdmnRoles;

        @FindBy(id = "roleAssignmentSubMenuItem")
        private WebElement prtlAdmnRoleAssignment;

    @FindBy(id = "poolManagementMenuItem")
    private WebElement poolManagement;

        @FindBy(id = "vdisSubMenuItem")
        private WebElement plMngmntVDIs;

        @FindBy(id = "poolProvidersSubMenuItem")
        private WebElement plMngmntPoolProviders;

    @FindBy(id = "serviceManagementMenuItem")
    private WebElement serviceManagement;

        @FindBy(id = "serviceCatalogSubMenuItem")
        private WebElement srvcMngmtServiceCatalog;

        @FindBy(id = "serviceDashboardSubMenuItem")
        private WebElement srvcMngmtServiceDashboard;

        @FindBy(id = "uiCatalogSubMenuItem")
        private WebElement srvcMngmtUIcatalog;

        @FindBy(id = "dbConnectionsSubMenuItem")
        private WebElement srvcMngmtDBconnections;

    @FindBy(id = "reportsMenuItem")
    private WebElement reporting;

        @FindBy(id = "activeUsersSubMenuItem")
        private WebElement reportingActiveUsers;

        @FindBy(id = "userDetailsSubMenuItem")
        private WebElement reportingUserDetails;

        @FindBy(id = "documentAuditSubMenuItem")
        private WebElement reportingDocumentAudit;

        @FindBy(id = "totalLoginsSubMenuItem")
        private WebElement reportingTotalLogins;

        @FindBy(id = "hitPerPageSubMenuItem")
        private WebElement reportingHitPerPage;

        @FindBy(id = "visitsSubMenuItem")
        private WebElement reportingVisits;

        @FindBy(id = "crashLogSubMenuItem")
        private WebElement reportingCrashLog;

    @FindBy(id = "deviceManagementMenuItem")
    private WebElement deviceManagement;

        @FindBy(id = "provisionConfigSubMenuItem")
        private WebElement dvcMngmtProvisionConfig;

        @FindBy(id = "userDevicesSubMenuItem")
        private WebElement dvcMngmtUserDevices;


    private Actions action = new Actions(driver);
    JavascriptExecutor JSexecutor = (JavascriptExecutor)driver;
    WakeUpPortal wakePortal = new WakeUpPortal(driver);

    public HeaderMenu(WebDriver driver)
    {
        super(driver);
    }

    public void clickElementAndWaitText(String mainLinkText, String linkText, String urltext) throws InterruptedException
    {
        clickElementAndWaitText(mainLinkText, linkText, urltext, 10, false);
    }

    public void clickElementAndWaitText(String mainLinkText, String linkText, String urltext, int j, boolean refresh) throws InterruptedException
    {
        int pause = 1000;
        for (int i=0; i < j; i++) {
            try {
                if (i==1) System.out.println("HeaderMenu: Can't click the Element: " + driver.findElement(By.linkText(linkText)).getText() + " will try " + (j-1) + " times more");
                action.moveToElement(driver.findElement(By.linkText(linkText))).click().build().perform();
                System.out.println("HeaderMenu: Sucessfully clicked the following link: " + linkText);
                if (refresh) driver.navigate().refresh();
                if (refresh) Thread.sleep(5_000); else Thread.sleep(1_000);

                if (driver.getCurrentUrl().contains(urltext)) {
                    System.out.println("HeaderMenu: Target text is " + urltext);
                    System.out.println("HeaderMenu: Got the target text for Web Element: " + driver.getCurrentUrl());

                    String id = "environmentForm:environmentSelect_label";
                    System.out.println("HeaderMenu: " + driver.findElement(By.id(id)).getText());
                    if (driver.findElement(By.id(id)).getText().equals("&nbsp;")) {
                        driver.navigate().refresh(); pause = 1000*(i+3); Thread.sleep(pause);
                        System.out.println("HeaderMenu: AHTUNG!!! I've got blocked page, it's " + driver.getCurrentUrl());
                    }
                    else {System.out.println("HeaderMenu: Good. I've got environment value, it's " + driver.findElement(By.id(id)).getText()); break;}
                }
                else {
                        action.moveToElement(driver.findElement(By.linkText(mainLinkText))).click().build().perform();
                        System.out.println("HeaderMenu: Didn't get the target url: " + urltext + " , so, just clicked the following item: " + mainLinkText); pause = 1000*(i+1);  Thread.sleep(pause);
                    }
            } catch (Exception e) {
                Thread.sleep(1_000); if (i==j-1) System.out.println("HeaderMenu: Can't click the Element: " + linkText + " , i = " + i);
                driver.navigate().back();
                Thread.sleep(5_000);
                wakePortal.fixAllProblems(); //fix
                System.out.println("action.moveToElement(driver.findElement(By.linkText(mainLinkText))).toString() : " + action.moveToElement(driver.findElement(By.linkText(mainLinkText))).toString()); //z
                action.moveToElement(driver.findElement(By.linkText(mainLinkText))).click().build().perform();
                System.out.println("HeaderMenu: Clicked maim item (from CATCH) : " + mainLinkText + " again.");
            }
        }

    }

    public void clickElementAndWaitText(String mainLinkText, String linkText, String urltext, int j) throws InterruptedException
    {
        clickElementAndWaitText(mainLinkText, linkText, urltext, j, false);
    }

    public ActiveUsers clickActiveUsers(boolean doWakeUp) throws InterruptedException
    {
        if (!reportingActiveUsers.isDisplayed()) reporting.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu reportingActiveUsers is displayed: " + reportingActiveUsers.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Reporting", "Active Users", "activeusers.jsf");
        System.out.println(reportingActiveUsers.getText() + "element was clicked (reportingActiveUsers)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Active Users was clicked");

        return new ActiveUsers(driver);
    }

    public ActiveUsers clickActiveUsers() throws InterruptedException
    {
        this.clickActiveUsers(false);
        return new ActiveUsers(driver);
    }

    public UserDetails clickUserDetails(boolean doWakeUp) throws InterruptedException
    {
        if (!reportingUserDetails.isDisplayed()) reporting.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu reportingUserDetails is displayed: " + reportingUserDetails.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Reporting", "User Details","useractivestatistic.jsf");
        System.out.println(reportingUserDetails.getText() + "element was clicked (reportingUserDetails)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: User Details was clicked");

        return new UserDetails(driver);
    }

    public UserDetails clickUserDetails() throws InterruptedException
    {
        this.clickUserDetails(false);
        return new UserDetails(driver);
    }

    public void clickDocumentAudit(boolean doWakeUp) throws InterruptedException //DocumentAudit
    {
        if (!reportingDocumentAudit.isDisplayed()) reporting.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu reportingDocumentAudit is displayed: " + reportingDocumentAudit.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Reporting", "Document Audit", "documentsstatistic.jsf");
        System.out.println(reportingDocumentAudit.getText() + "element was clicked (reportingDocumentAudit)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Document Audit was clicked");

        //return new DocumentAudit(driver);
    }

    public void clickDocumentAudit() throws InterruptedException //DocumentAudit
    {
        this.clickDocumentAudit(false);
        //return new DocumentAudit(driver);
    }

    public TotalLogins clickTotalLogins(boolean doWakeUp) throws InterruptedException
    {
        if (!reportingTotalLogins.isDisplayed()) reporting.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu reportingTotalLogins is displayed: " + reportingTotalLogins.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Reporting", "Total Logins", "statisticsuser.jsf");
        System.out.println(reportingTotalLogins.getText() + "element was clicked (reportingTotalLogins)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Total Logins was clicked");

        return new TotalLogins(driver);
    }

    public TotalLogins clickTotalLogins() throws InterruptedException
    {
        this.clickTotalLogins(false);
        return new TotalLogins(driver);
    }

    public HitsPerPage clickHitsPerPage(boolean doWakeUp) throws InterruptedException
    {
        if (!reportingHitPerPage.isDisplayed()) reporting.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu reportingHitPerPage is displayed: " + reportingHitPerPage.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Reporting", "Hits Per Page", "barchart.jsf");
        System.out.println(reportingHitPerPage.getText() + "element was clicked (reportingHitPerPage)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Hits Per Page was clicked");

        return new HitsPerPage(driver);
    }

    public HitsPerPage clickHitsPerPage() throws InterruptedException
    {
        this.clickHitsPerPage(false);
        return new HitsPerPage(driver);
    }

    public Visits clickVisits(boolean doWakeUp) throws InterruptedException
    {
        if (!reportingVisits.isDisplayed()) reporting.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu reportingVisits is displayed: " + reportingVisits.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Reporting", "Visits", "linechart.jsf");
        System.out.println(reportingVisits.getText() + "element was clicked (reportingVisits)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Visits Page was clicked");

        return new Visits(driver);
    }

    public Visits clickVisits() throws InterruptedException
    {
        this.clickVisits(false);
        return new Visits(driver);
    }

    public CrashLog clickCrashLog(boolean doWakeUp) throws InterruptedException
    {
        if (!reportingCrashLog.isDisplayed()) reporting.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu reportingCrashLog is displayed: " + reportingCrashLog.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Reporting", "Crash Log", "crashlogstatistic.jsf");
        System.out.println(reportingCrashLog.getText() + "element was clicked (reportingCrashLog)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Crash Log Page was clicked");

        return new CrashLog(driver);
    }

    public CrashLog clickCrashLog() throws InterruptedException
    {
        this.clickCrashLog(false);
        return new CrashLog(driver);
    }

    public Profiles clickProfiles(boolean doWakeUp) throws InterruptedException
    {
        if (!usrAndRlMngmtProfiles.isDisplayed()) userAndRoleManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu usrAndRlMngmtProfiles is displayed: " + usrAndRlMngmtProfiles.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
         //   (new WebDriverWait(driver, 10))
         //       .until(ExpectedConditions.presenceOfElementLocated(By.id("profilesSubMenuItem"))); //.visibilityOf(usrAndRlMngmtProfiles)); .elementToBeClickable(usrAndRlMngmtProfiles));
         // System.out.println("Profiles element is presented");
         //Thread.sleep(3_000);
         //action.moveToElement(driver.findElement(By.linkText("Profiles"))).click().build().perform();
         //action.moveToElement(usrAndRlMngmtProfiles).perform();
         //action.moveToElement(usrAndRlMngmtProfiles, 1, 1).click().perform();
         this.clickElementAndWaitText("User & Role Management", "Profiles", "profile.jsf");

         System.out.println(usrAndRlMngmtProfiles.getText() + "element was clicked (usrAndRlMngmtProfiles)");
         Thread.sleep(3_000);
         Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
         System.out.println("HeaderMenu [last message]: Profiles was clicked");

         return new Profiles(driver);
    }

    public Profiles clickProfiles() throws InterruptedException
    {
        this.clickProfiles(false);
        return new Profiles(driver);
    }

    public Application clickApplication(boolean doWakeUp) throws InterruptedException
    {
        if (!usrAndRlMngmtApplications.isDisplayed()) userAndRoleManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu usrAndRlMngmtApplications is displayed: " + usrAndRlMngmtApplications.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("User & Role Management", "Applications", "applications.jsf");
        System.out.println(usrAndRlMngmtApplications.getText() + "element was clicked (usrAndRlMngmtApplications)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Applications was clicked");

        return new Application(driver);
    }

    public Application clickApplication() throws InterruptedException
    {
        this.clickApplication(false);
        return new Application(driver);
    }

    public ProfileAssignment clickProfileAssignment(boolean doWakeUp) throws InterruptedException
    {
        if (!usrAndRlMngmtProfileAssignments.isDisplayed()) userAndRoleManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu usrAndRlMngmtProfileAssignments is displayed: " + usrAndRlMngmtProfileAssignments.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("User & Role Management", "Profile Assignment", "assignments.jsf");
        System.out.println(usrAndRlMngmtProfileAssignments.getText() + "element was clicked (usrAndRlMngmtProfileAssignments)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Profile Assignment was clicked");

        return new ProfileAssignment(driver);
    }

    public ProfileAssignment clickProfileAssignment() throws InterruptedException
    {
        this.clickProfileAssignment(false);
        return new ProfileAssignment(driver);
    }

    public AuthenticationStratums clickAuthenticationStratums(boolean doWakeUp) throws InterruptedException
    {
        if (!usrAndRlMngmtAuthStratums.isDisplayed()) userAndRoleManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu usrAndRlMngmtAuthStratums is displayed: " + usrAndRlMngmtAuthStratums.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("User & Role Management", "Authentication Stratums", "stratum.jsf");
        System.out.println(usrAndRlMngmtAuthStratums.getText() + "element was clicked (usrAndRlMngmtAuthStratums)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Authentication Stratums was clicked");

        return new AuthenticationStratums(driver);
    }

    public AuthenticationStratums clickAuthenticationStratums() throws InterruptedException
    {
        this.clickAuthenticationStratums(false);
        return new AuthenticationStratums(driver);
    }

    public AuthenticationGroups clickAuthenticationGroups(boolean doWakeUp) throws InterruptedException
    {
        if (!usrAndRlMngmtAuthGroups.isDisplayed()) userAndRoleManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu usrAndRlMngmtAuthGroups is displayed: " + usrAndRlMngmtAuthGroups.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("User & Role Management", "Authentication Groups", "stratum-group.jsf");
        System.out.println(usrAndRlMngmtAuthGroups.getText() + "element was clicked (usrAndRlMngmtAuthGroups)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Authentication Groups was clicked");

        return new AuthenticationGroups(driver);
    }

    public AuthenticationGroups clickAuthenticationGroups() throws InterruptedException
    {
        this.clickAuthenticationGroups(false);
        return new AuthenticationGroups(driver);
    }

    public Policies clickPolicies(boolean doWakeUp) throws InterruptedException
    {
        if (!usrAndRlMngmtPolicies.isDisplayed()) userAndRoleManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu usrAndRlMngmtPolicies is displayed: " + usrAndRlMngmtPolicies.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("User & Role Management", "Policies", "policies.jsf");
        System.out.println(usrAndRlMngmtPolicies.getText() + "element was clicked (usrAndRlMngmtPolicies)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Policies was clicked");

        return new Policies(driver);
    }

    public Policies clickPolicies() throws InterruptedException
    {
        this.clickPolicies(false);
        return new Policies(driver);
    }

    public PolicyAssignment clickPolicyAssignment(boolean doWakeUp) throws InterruptedException
    {
        if (!usrAndRlMngmtPolicyAssignments.isDisplayed()) userAndRoleManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu usrAndRlMngmtPolicyAssignments is displayed: " + usrAndRlMngmtPolicyAssignments.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("User & Role Management", "Policy Assignment", "policy-assignment.jsf");
        System.out.println(usrAndRlMngmtPolicyAssignments.getText() + "element was clicked (usrAndRlMngmtPolicyAssignments)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Policy Assignment was clicked");

        return new PolicyAssignment(driver);
    }

    public PolicyAssignment clickPolicyAssignment() throws InterruptedException
    {
        this.clickPolicyAssignment(false);
        return new PolicyAssignment(driver);
    }

    public Archetypes clickArchetypes(boolean doWakeUp) throws InterruptedException
    {
        if (!usrAndRlMngmtArchetypes.isDisplayed()) userAndRoleManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu usrAndRlMngmtArchetypes is displayed: " + usrAndRlMngmtArchetypes.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("User & Role Management", "Archetypes", "navigation-item-controller-type.jsf");
        System.out.println(usrAndRlMngmtArchetypes.getText() + "element was clicked (usrAndRlMngmtArchetypes)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Archetypes was clicked");

        return new Archetypes(driver);
    }

    public Archetypes clickArchetypes() throws InterruptedException
    {
        this.clickArchetypes(false);
        return new Archetypes(driver);
    }

    public Contexts clickContexts(boolean doWakeUp) throws InterruptedException
    {
        if (!usrAndRlMngmtContexts.isDisplayed()) userAndRoleManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu usrAndRlMngmtContexts is displayed: " + usrAndRlMngmtContexts.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("User & Role Management", "Contexts", "navigation-item-context.jsf");
        System.out.println(usrAndRlMngmtContexts.getText() + "element was clicked (usrAndRlMngmtContexts)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Contexts was clicked");

        return new Contexts(driver);
    }

    public Contexts clickContexts() throws InterruptedException
    {
        this.clickContexts(false);
        return new Contexts(driver);
    }

    public UIGroups clickUIGroups(boolean doWakeUp) throws InterruptedException
    {
        if (!usrAndRlMngmtUIgroups.isDisplayed()) userAndRoleManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu usrAndRlMngmtUIgroups is displayed: " + usrAndRlMngmtUIgroups.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("User & Role Management", "UI Groups", "navigation-group.jsf");
        System.out.println(usrAndRlMngmtUIgroups.getText() + "element was clicked (usrAndRlMngmtUIgroups)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: UI Groups was clicked");

        return new UIGroups(driver);
    }

    public UIGroups clickUIGroups() throws InterruptedException
    {
        this.clickUIGroups(false);
        return new UIGroups(driver);
    }

    public NavigationItems clickNavigationItems(boolean doWakeUp) throws InterruptedException
    {

        if (!usrAndRlMngmtNavigationItems.isDisplayed()) userAndRoleManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu usrAndRlMngmtNavigationItems is displayed: " + usrAndRlMngmtNavigationItems.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("User & Role Management", "Navigation Items", "navigation-item.jsf");
        System.out.println(usrAndRlMngmtNavigationItems.getText() + "element was clicked (usrAndRlMngmtNavigationItems)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Navigation Items was clicked");

        return new NavigationItems(driver);
    }

    public NavigationItems clickNavigationItems() throws InterruptedException
    {
        this.clickNavigationItems(false);
        return new NavigationItems(driver);
    }

    public Navigation clickNavigation(boolean doWakeUp) throws InterruptedException
    {
        if (!usrAndRlMngmtNavigation.isDisplayed()) userAndRoleManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu usrAndRlMngmtNavigation is displayed: " + usrAndRlMngmtNavigation.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("User & Role Management", "Navigation", "navigation.jsf");
        System.out.println(usrAndRlMngmtNavigation.getText() + "element was clicked (usrAndRlMngmtNavigation)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Navigation was clicked");

        return new Navigation(driver);
    }

    public Navigation clickNavigation() throws InterruptedException
    {
        this.clickNavigation(false);
        return new Navigation(driver);
    }

    public ServiceCatalog clickServiceCatalog(boolean doWakeUp) throws InterruptedException
    {
        if (!srvcMngmtServiceCatalog.isDisplayed()) serviceManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu srvcMngmtServiceCatalog is displayed: " + srvcMngmtServiceCatalog.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Service Management","Service Catalog", "service-catalog.jsf");
        System.out.println(srvcMngmtServiceCatalog.getText() + "element was clicked (srvcMngmtServiceCatalog)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Service Catalog was clicked");

        return new ServiceCatalog(driver);
    }

    public ServiceCatalog clickServiceCatalog() throws InterruptedException
    {
        this.clickServiceCatalog(false);
        return new ServiceCatalog(driver);
    }

    public ServiceDashboard clickServiceDashboard(boolean doWakeUp) throws InterruptedException
    {
        if (!srvcMngmtServiceDashboard.isDisplayed()) serviceManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu srvcMngmtServiceDashboard is displayed: " + srvcMngmtServiceDashboard.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Service Management","Service Dashboard", "service-dashboard.jsf");
        System.out.println(srvcMngmtServiceDashboard.getText() + "element was clicked (srvcMngmtServiceDashboard)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Service Catalog was clicked");

        return new ServiceDashboard(driver);
    }

    public ServiceDashboard clickServiceDashboard() throws InterruptedException
    {
        this.clickServiceDashboard(false);
        return new ServiceDashboard(driver);
    }

    public UICatalog clickUICatalog(boolean doWakeUp) throws InterruptedException
    {
        if (!srvcMngmtUIcatalog.isDisplayed()) serviceManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu srvcMngmtUIcatalog is displayed: " + srvcMngmtUIcatalog.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Service Management","UI Catalog", "ui-catalog.jsf");
        System.out.println(srvcMngmtUIcatalog.getText() + "element was clicked (srvcMngmtUIcatalog)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: UI Catalog was clicked");

        return new UICatalog(driver);
    }

    public UICatalog clickUICatalog() throws InterruptedException
    {
        this.clickUICatalog(false);
        return new UICatalog(driver);
    }

    public DBConnections clickDBConnections(boolean doWakeUp) throws InterruptedException
    {
        if (!srvcMngmtDBconnections.isDisplayed()) serviceManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu srvcMngmtDBconnections is displayed: " + srvcMngmtDBconnections.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Service Management","DB Connections", "db-connections.jsf");
        System.out.println(srvcMngmtDBconnections.getText() + "element was clicked (srvcMngmtDBconnections)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: DB Connections was clicked");

        return new DBConnections(driver);
    }

    public DBConnections clickDBConnections() throws InterruptedException
    {
        this.clickDBConnections(false);
        return new DBConnections(driver);
    }

    public VDIs clickVDIs(boolean doWakeUp) throws InterruptedException
    {
        if (!plMngmntVDIs.isDisplayed()) poolManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu plMngmntVDIs is displayed: " + plMngmntVDIs.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Pool Management","VDIs", "rdp.jsf");
        System.out.println(plMngmntVDIs.getText() + "element was clicked (plMngmntVDIs)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: VDIs was clicked");

        return new VDIs(driver);
    }

    public VDIs clickVDIs() throws InterruptedException
    {
        this.clickVDIs(false);
        return new VDIs(driver);
    }

    public PoolProviders clickPoolProviders(boolean doWakeUp)  throws InterruptedException
    {
        if (!plMngmntPoolProviders.isDisplayed()) poolManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu plMngmntPoolProviders is displayed: " + plMngmntPoolProviders.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Pool Management","Pool Providers", "pool-providers.jsf");
        System.out.println(plMngmntPoolProviders.getText() + "element was clicked (plMngmntPoolProviders)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Pool Providers was clicked");

        return new PoolProviders(driver);
    }

    public PoolProviders clickPoolProviders()  throws InterruptedException
    {
        this.clickPoolProviders(false);
        return new PoolProviders(driver);
    }

    public void clickPools(boolean doWakeUp)  throws InterruptedException //Pools
    {
        if (!plMngmntPoolProviders.isDisplayed()) poolManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu plMngmntPoolProviders is displayed: " + plMngmntPoolProviders.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Pool Management","Pools", "pool.jsf");
        System.out.println(plMngmntPoolProviders.getText() + "element was clicked (plMngmntPools)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Pools was clicked");

        //return new PoolProviders(driver);
    }

    public void clickPools()  throws InterruptedException //Pools
    {
        this.clickPools(false);
        //return new Pools(driver);
    }

    public ProvisioningConfig clickProvisioningConfig(boolean doWakeUp)  throws InterruptedException
    {
        if (!dvcMngmtProvisionConfig.isDisplayed()) deviceManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu dvcMngmtProvisionConfig is displayed: " + dvcMngmtProvisionConfig.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Device management", "Provisioning Config", "provision-config.jsf");
        System.out.println(dvcMngmtProvisionConfig.getText() + "element was clicked (dvcMngmtProvisionConfig)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Device management > Provisioning Config was clicked");

        return new ProvisioningConfig(driver);
    }

    public ProvisioningConfig clickProvisioningConfig()  throws InterruptedException
    {
        this.clickProvisioningConfig(false);
        return new ProvisioningConfig(driver);
    }

    public UserDevices clickUserDevices(boolean doWakeUp)  throws InterruptedException //UserDevices ED-3950
    {
        if (!dvcMngmtUserDevices.isDisplayed()) deviceManagement.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu dvcMngmtUserDevices is displayed: " + dvcMngmtUserDevices.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Device management", "User Devices", "userdevices.jsf");
        System.out.println(dvcMngmtUserDevices.getText() + "element was clicked (dvcMngmtUserDevices)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Device management > User Devices was clicked");

        return new UserDevices(driver);
    }

    public UserDevices clickUserDevices()  throws InterruptedException //UserDevices ED-3950
    {
        this.clickUserDevices(false);
        return new UserDevices(driver);
    }

    public Environments clickEnvironments(boolean doWakeUp) throws InterruptedException
    {
        if (!srvrCnfgrtnEnvironments.isDisplayed()) serverConfiguration.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu srvrCnfgrtnEnvironments is displayed: " + srvrCnfgrtnEnvironments.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Server Configuration","Environments", "environment.jsf");
        System.out.println(srvrCnfgrtnEnvironments.getText() + "element was clicked (srvrCnfgrtnEnvironments)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Environments was clicked");

        return new Environments(driver);
    }

    public Environments clickEnvironments() throws InterruptedException
    {
        this.clickEnvironments(false);
        return new Environments(driver);
    }

    public Configs clickConfigs(boolean doWakeUp) throws InterruptedException
    {
        if (!srvrCnfgrtnConfigs.isDisplayed()) serverConfiguration.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu srvrCnfgrtnConfigs is displayed: " + srvrCnfgrtnConfigs.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Server Configuration","Configs", "configs.jsf");
        System.out.println(srvrCnfgrtnConfigs.getText() + "element was clicked (srvrCnfgrtnConfigs)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Configs was clicked");

        return new Configs(driver);
    }

    public Configs clickConfigs() throws InterruptedException
    {
        this.clickConfigs(false);
        return new Configs(driver);
    }

    public Settings clickSettings(boolean doWakeUp) throws InterruptedException
    {
        if (!srvrCnfgrtnSettings.isDisplayed()) serverConfiguration.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu srvrCnfgrtnSettings is displayed: " + srvrCnfgrtnSettings.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Server Configuration","Settings", "settings.jsf");
        System.out.println(srvrCnfgrtnSettings.getText() + "element was clicked (srvrCnfgrtnSettings)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Settings was clicked");

        return new Settings(driver);
    }

    public Settings clickSettings() throws InterruptedException
    {
        this.clickSettings(false);
        return new Settings(driver);
    }

    public Scheduler clickScheduler(boolean doWakeUp) throws InterruptedException
    {
        if (!srvrCnfgrtnScheduler.isDisplayed()) serverConfiguration.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu srvrCnfgrtnScheduler is displayed: " + srvrCnfgrtnScheduler.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Server Configuration","Scheduler", "scheduler.jsf");
        System.out.println(srvrCnfgrtnScheduler.getText() + "element was clicked (srvrCnfgrtnScheduler)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Scheduler was clicked");

        return new Scheduler(driver);
    }

    public Scheduler clickScheduler() throws InterruptedException
    {
        this.clickScheduler(false);
        return new Scheduler(driver);
    }

    public Container clickContainer(boolean doWakeUp) throws InterruptedException
    {
        if (!auditContainer.isDisplayed()) audit.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu auditContainer is displayed: " + auditContainer.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Audit","Container", "logs.jsf");
        System.out.println(auditContainer.getText() + "element was clicked (auditContainer)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Container was clicked");

        return new Container(driver);
    }

    public Container clickContainer() throws InterruptedException
    {
        this.clickContainer(false);
        return new Container(driver);
    }

    public LoginLogout clickLoginLogout(boolean doWakeUp) throws InterruptedException
    {
        if (!auditLoginLogout.isDisplayed()) audit.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu auditLoginLogout is displayed: " + auditLoginLogout.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Audit","Login/Logout", "loginlogoutstatistics.jsf");
        System.out.println(auditLoginLogout.getText() + "element was clicked (auditLoginLogout)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Login/Logout was clicked");

        return new LoginLogout(driver);
    }

    public LoginLogout clickLoginLogout() throws InterruptedException
    {
        this.clickLoginLogout(false);
        return new LoginLogout(driver);
    }

    public EmailGroups clickEmailGroups(boolean doWakeUp) throws InterruptedException
    {
        if (!auditEmailGroups.isDisplayed()) audit.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu auditEmailGroups is displayed: " + auditEmailGroups.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Audit","Email Groups", "emailgroup.jsf");
        System.out.println(auditEmailGroups.getText() + "element was clicked (auditEmailGroups)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Email Groups was clicked");

        return new EmailGroups(driver);
    }

    public EmailGroups clickEmailGroups() throws InterruptedException
    {
        this.clickEmailGroups(false);
        return new EmailGroups(driver);
    }

    public DeviceLog clickDeviceLog(boolean doWakeUp) throws InterruptedException
    {
        if (!auditDeviceLog.isDisplayed()) audit.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu auditDeviceLog is displayed: " + auditDeviceLog.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Audit","Device Log", "devicelog.jsf");
        System.out.println(auditDeviceLog.getText() + "element was clicked (auditDeviceLog)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Device Log was clicked");

        return new DeviceLog(driver);
    }

    public DeviceLog clickDeviceLog() throws InterruptedException
    {
        this.clickDeviceLog(false);
        return new DeviceLog(driver);
    }

    public Alerts clickAlerts(boolean doWakeUp) throws InterruptedException
    {
        if (!auditAlerts.isDisplayed()) audit.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu auditAlerts is displayed: " + auditAlerts.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Audit","Alerts", "logevent.jsf");
        System.out.println(auditAlerts.getText() + "element was clicked (auditAlerts)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Alerts was clicked");

        return new Alerts(driver);
    }

    public Alerts clickAlerts() throws InterruptedException
    {
        this.clickAlerts(false);
        return new Alerts(driver);
    }

    public UserGroups clickUserGroups(boolean doWakeUp) throws InterruptedException
    {
        if (!prtlAdmnUserGroups.isDisplayed()) portalAdministration.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu prtlAdmnUserGroups is displayed: " + prtlAdmnUserGroups.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Portal administration","User Groups", "group.jsf");
        System.out.println(prtlAdmnUserGroups.getText() + "element was clicked (prtlAdmnUserGroups)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: User groups was clicked");

        return new UserGroups(driver);
    }

    public UserGroups clickUserGroups() throws InterruptedException
    {
        this.clickUserGroups(false);
        return new UserGroups(driver);
    }

    public Users clickUsers(boolean doWakeUp) throws InterruptedException
    {
        if (!prtlAdmnUsers.isDisplayed()) portalAdministration.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu prtlAdmnUsers is displayed: " + prtlAdmnUsers.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Portal administration","Users", "users.jsf");
        System.out.println(prtlAdmnUsers.getText() + "element was clicked (prtlAdmnUsers)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Users was clicked");

        return new Users(driver);
    }

    public Users clickUsers() throws InterruptedException
    {
        this.clickUsers(false);
        return new Users(driver);
    }

    public DBAudit clickDBAudit(boolean doWakeUp) throws InterruptedException
    {
        if (!prtlAdmnDBaudit.isDisplayed()) portalAdministration.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu prtlAdmnDBaudit is displayed: " + prtlAdmnDBaudit.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Portal administration","DB Audit", "modification-log.jsf");
        System.out.println(prtlAdmnDBaudit.getText() + "element was clicked (prtlAdmnDBaudit)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: DB Audit was clicked");

        return new DBAudit(driver);
    }

    public DBAudit clickDBAudit() throws InterruptedException
    {
        this.clickDBAudit(false);
        return new DBAudit(driver);
    }

    public Roles clickRoles(boolean doWakeUp) throws InterruptedException
    {
        if (!prtlAdmnRoles.isDisplayed()) portalAdministration.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu prtlAdmnRoles is displayed: " + prtlAdmnRoles.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Portal administration","Roles", "roles.jsf");
        System.out.println(prtlAdmnRoles.getText() + "element was clicked (prtlAdmnRoles)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Roles was clicked");

        return new Roles(driver);
    }

    public Roles clickRoles() throws InterruptedException
    {
        this.clickRoles(false);
        return new Roles(driver);
    }

    public RoleAssignment clickRoleAssignment(boolean doWakeUp) throws InterruptedException
    {
        if (!prtlAdmnRoleAssignment.isDisplayed()) portalAdministration.findElement(By.className("menu-toggler")).click();
        Thread.sleep(1_000);
        System.out.println("HeaderMenu prtlAdmnRoleAssignment is displayed: " + prtlAdmnRoleAssignment.isDisplayed());
        Thread.sleep(1_000);
        if (doWakeUp) wakePortal.fixEnvProblemCycle(); //fix
        this.clickElementAndWaitText("Portal administration","Role Assignment", "role-assignments.jsf");
        System.out.println(prtlAdmnRoleAssignment.getText() + "element was clicked (prtlAdmnRoleAssignment)");
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> driver.findElement(By.id("contentColumns")).getClass()); //Retry
        System.out.println("HeaderMenu [last message]: Role Assignment was clicked");

        return new RoleAssignment(driver);
    }

    public RoleAssignment clickRoleAssignment() throws InterruptedException
    {
        this.clickRoleAssignment(false);
        return new RoleAssignment(driver);
    }

    /**
     * Only expands Environment dropdown
     */
    public void expandEnvironmentDropdown()
    {
        //was: ((JavascriptExecutor) driver).executeScript("$('#environmentForm\\\\:environmentSelect label').click()");
        environmentDropDown.click();
    }

    /**
     * Select environment from the list.
     * Need to expand first.
     * @param envName
     */
    public void selectEnvironment(String envName)
    {
        // click by envName
        ((JavascriptExecutor) driver).executeScript("$('#environmentForm\\\\:environmentSelect_items li:contains(\"" + envName + "\")').click()");
    }

    public LogOff clickLogOff()
    {
        logoffButton.click();
        System.out.println("HeaderMenu [only message]: Log Off was clicked");

        return new LogOff(driver);
    }

    public void clickCloseMenu()
    {
        closeMenuTriangle.click();
        System.out.println("HeaderMenu: Close menue triangle was clicked");
    }
}
