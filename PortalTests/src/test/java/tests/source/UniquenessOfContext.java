package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.ContextDetail;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.pages.HeaderMenu;
import net.portal.pages.user_and_role_management.Contexts;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class UniquenessOfContext
{
    @Test
    public void uniquenessOfContext() throws InterruptedException
    {
        System.out.println("--- START OF UniquenessOfContext ---");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Contexts contextsPage = headerMenu.clickContexts();

        ContextDetail applicationDetail = contextsPage.addContext();

        String contextName = "Unik con 441";
        applicationDetail.setName(contextName);
        applicationDetail.setDescription("description_4");

        applicationDetail.clickAdd();
        Thread.sleep(1_000);

        applicationDetail = contextsPage.addContext();
        Thread.sleep(1_000);
        applicationDetail.setName(contextName);
        applicationDetail.setDescription("description_4");

        applicationDetail.clickAdd();
        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.ITEM_CONTEXT_NAME_SHOULD_BE_UNIQUE.getNotificationText(), notificationPopup.getText());

        applicationDetail.clickCancel();
        Thread.sleep(2_000);

        contextsPage.selectContext(contextName);
        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = contextsPage.deleteContext();
        Thread.sleep(6_000);

        Assert.assertEquals("name = " + contextName, followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();

        Thread.sleep(1_000);

        System.out.println("--- END OF UniquenessOfContext ---");
    }
}
