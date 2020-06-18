package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.StratumDetail;
import net.portal.pages.HeaderMenu;
import net.portal.pages.user_and_role_management.AuthenticationStratums;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class UniquenessOfStratum
{
    @Test
    public void uniquenessOfStratum() throws InterruptedException
    {
        System.out.println("--- START OF UniquenessOfStratum ---");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        AuthenticationStratums authenticationStratumsPage = headerMenu.clickAuthenticationStratums();

        StratumDetail stratumDetail = authenticationStratumsPage.addNewStratum();
        Thread.sleep(2_000);

        String stratumName = "stratum item AT 41";
        stratumDetail.setName(stratumName);
        stratumDetail.setExpiration(1);

        stratumDetail.clickAdd();
        Thread.sleep(2_000);

        stratumDetail = authenticationStratumsPage.addNewStratum();
        Thread.sleep(2_000);
        stratumDetail.setName(stratumName);
        stratumDetail.setExpiration(1);

        stratumDetail.clickAdd();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.STRATUM_NAME_SHOULD_BE_UNIQUE.getNotificationText(), notificationPopup.getText());
        Thread.sleep(2_000);

        stratumDetail.clickCancel();
        Thread.sleep(2_000);

        authenticationStratumsPage.selectStratum(stratumName);

        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = authenticationStratumsPage.deleteStratum();
        Thread.sleep(2_000);
        Assert.assertEquals("name = " + stratumName, followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();

        Thread.sleep(2_000);

        System.out.println("--- END OF UniquenessOfStratum ---");
    }
}
