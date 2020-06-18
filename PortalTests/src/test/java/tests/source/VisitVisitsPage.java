package tests.source;

import net.portal.forms.ApplicationDetail;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.pages.HeaderMenu;
import net.portal.pages.reporting.Visits;
import net.portal.pages.user_and_role_management.Application;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

public class VisitVisitsPage
{
    @Test
    public void visitVisitsPage() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Visits visitsPage = headerMenu.clickVisits();

        System.out.println("Make sure that Apply button is visible...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:searchApplyButton').is(':visible')"));

        System.out.println("Add new Application and make sure that it is in the list...");

        Application applicationPage = headerMenu.clickApplication();

        ApplicationDetail applicationDetail = applicationPage.addNewApplication();
        Thread.sleep(3_000);

        String applicationName = "AP_333";

        applicationDetail.setName(applicationName);
        applicationDetail.clickAdd();
        Thread.sleep(3_000);

        visitsPage = headerMenu.clickVisits();

        visitsPage.selectApplication(applicationName);
        Thread.sleep(3_000);

        Assert.assertEquals(applicationName, visitsPage.getSelectedApplication());

        // After-test routine
        // delete application
        applicationPage = headerMenu.clickApplication();

        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = applicationPage.deleteApplication(applicationName);
        Thread.sleep(2_000);

        followingItemsWillBeDeleted.clickDelete();
        Thread.sleep(2_000);

        visitsPage = headerMenu.clickVisits();

        Assert.assertEquals("*", visitsPage.getSelectedApplication());
    }
}
