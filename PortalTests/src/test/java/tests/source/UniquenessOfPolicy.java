package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.PolicyDetail;
import net.portal.pages.DeletePolicyConfirmation;
import net.portal.pages.HeaderMenu;
import net.portal.pages.user_and_role_management.Policies;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class UniquenessOfPolicy
{
    @Test
    public void uniquenessOfPolicy() throws InterruptedException
    {
        System.out.println("--- START OF UniquenessOfPolicy ---");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Policies policiesPage = headerMenu.clickPolicies();

        PolicyDetail propertyDetail = policiesPage.addPolicy();
        Thread.sleep(2_000);

        String nameOfPolicy = "new_policy_name_123";

        propertyDetail.setName(nameOfPolicy);
        propertyDetail.clickAdd();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 15)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_ADDED.getNotificationText(), notificationPopup.getText());

        // Create new policy with the same name...
        propertyDetail = policiesPage.addPolicy();
        Thread.sleep(2_000);

        propertyDetail.setName(nameOfPolicy);
        propertyDetail.clickAdd();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 15)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.PROPERTY_NAME_SHOULD_BE_UNIQUE.getNotificationText(), notificationPopup.getText());

        propertyDetail.clickCancel();
        Thread.sleep(4_000);

        policiesPage.searchForName(nameOfPolicy);
        policiesPage.clickApplyFilter();
        Thread.sleep(4_000);

        DeletePolicyConfirmation deletePolicyConfirmation = policiesPage.deletePolicy(nameOfPolicy);
        Thread.sleep(2_000);

        deletePolicyConfirmation.clickYes();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

        System.out.println("--- END OF UniquenessOfPolicy ---");
    }
}
