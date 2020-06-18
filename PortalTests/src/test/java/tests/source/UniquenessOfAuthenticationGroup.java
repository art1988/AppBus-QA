package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.StratumGroupDetail;
import net.portal.pages.HeaderMenu;
import net.portal.pages.user_and_role_management.AuthenticationGroups;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class UniquenessOfAuthenticationGroup
{
    @Test
    public void uniquenessOfAuthenticationGroup() throws InterruptedException
    {
        System.out.println("--- START OF UniquenessOfAuthenticationGroup ---");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        AuthenticationGroups authenticationGroupsPage = headerMenu.clickAuthenticationGroups();

        StratumGroupDetail stratumGroupDetail = authenticationGroupsPage.addNewAuthenticationGroup();
        Thread.sleep(2_000);

        String stratumGroupName = "Unik group 73";
        stratumGroupDetail.setGroupName(stratumGroupName);

        stratumGroupDetail.clickAdd();
        Thread.sleep(2_000);

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.GROUP_NEEDS_CONTAIN_AT_LEAST_ONE_STRATUM.getNotificationText(), notificationPopup.getText());
        Thread.sleep(2_000);

        // Note : RSA Stratum should be in the list before execution
        stratumGroupDetail.setStratum("RSA");

        stratumGroupDetail.clickAdd();
        Thread.sleep(2_000);

        stratumGroupDetail = authenticationGroupsPage.addNewAuthenticationGroup();
        Thread.sleep(2_000);

        stratumGroupDetail.setGroupName(stratumGroupName);
        stratumGroupDetail.setStratum("RSA");
        stratumGroupDetail.clickAdd();
        Thread.sleep(2_000);

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.STRATUM_GROUP_NAME_SHOULD_BE_UNIQUE.getNotificationText(), notificationPopup.getText());
        Thread.sleep(2_000);

        stratumGroupDetail.clickCancel();
        Thread.sleep(2_000);

        authenticationGroupsPage.selectGroupName(stratumGroupName);
        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = authenticationGroupsPage.deleteGroup();
        Thread.sleep(2_000);
        Assert.assertEquals("name = " + stratumGroupName, followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();

        Thread.sleep(2_000);

        System.out.println("--- END OF UniquenessOfAuthenticationGroup ---");
    }
}
