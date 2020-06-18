package tests.source;

import net.portal.constants.Notifications;
import net.portal.pages.DeleteJob;
import net.portal.pages.HeaderMenu;
import net.portal.pages.server_configuration.Scheduler;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class DeleteScheduledJob
{
    @Test
    public void deleteScheduledJob() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Scheduler schedulerPage = headerMenu.clickScheduler();

        String jobName = "AT sc_job";

        schedulerPage.viewTriggers(jobName);
        Thread.sleep(2_000);

        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('.ui-expanded-row-content.ui-widget-content tbody').text().startsWith(\"SIMPLEEvery 7 Sec\")"));

        DeleteJob deleteJob = schedulerPage.deleteJob(jobName);

        deleteJob.clickYes();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.JOB_WAS_SUCCESSFULLY_REMOVED.getNotificationText(), notificationPopup.getText());
    }
}
