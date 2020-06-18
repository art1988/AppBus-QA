package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.PoolProviderDetails;
import net.portal.pages.DeletePoolProvider;
import net.portal.pages.HeaderMenu;
import net.portal.pages.pool_management.PoolProviders;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class AddPoolProvider
{
    @Test
    public void addPoolProvider() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        PoolProviders poolProvidersPage = headerMenu.clickPoolProviders();

        String poolName = "AT_P_name",
               metadataURL    = "https://www.google.com/",
               addInstanceURL = "https://lenta.ru/",
               deleteInstanceURL = "https://stackoverflow.com",
               validateInstanceURL = "https://www.youtube.com/watch?v=JMUxFas6U1Y";


        PoolProviderDetails poolProviderDetails = poolProvidersPage.addPoolProvider();
        Thread.sleep(3_000);

        poolProviderDetails.setName(poolName);
        poolProviderDetails.setMetadataURL(metadataURL);
        poolProviderDetails.setAddInstanceURL(addInstanceURL);
        poolProviderDetails.setDeleteInstanceURL(deleteInstanceURL);
        poolProviderDetails.setValidateInstanceURL(validateInstanceURL);

        poolProviderDetails.clickSave();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.POOL_PROVIDER_WAS_SUCCESSFULLY_SAVED.getNotificationText(), notificationPopup.getText());

        System.out.println("Making sure that pool was added successfully...");

        Assert.assertEquals(poolName, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#poolProviders\\\\:poolProvidersTable_data tr td:contains(\"" + poolName + "\")').text()")));
        Assert.assertEquals("Metadata URL: https://www.google.com/Add instance URL: https://lenta.ru/Delete instance URL: https://stackoverflow.comValidate instance URL: https://www.youtube.com/watch?v=JMUxFas6U1Y",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#poolProviders\\\\:poolProvidersTable_data tr td:contains(\"" + poolName + "\")').next().text()")));

        System.out.println("Checking uniqueness of Pool Provider...");

        poolProviderDetails = poolProvidersPage.addPoolProvider();
        Thread.sleep(3_000);

        poolProviderDetails.setName(poolName);
        poolProviderDetails.setMetadataURL(metadataURL);
        poolProviderDetails.setAddInstanceURL(metadataURL);
        poolProviderDetails.setDeleteInstanceURL(metadataURL);
        poolProviderDetails.setValidateInstanceURL(metadataURL);

        poolProviderDetails.clickSave();

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.POOL_PROVIDER_NAME_ALREADY_EXISTS.getNotificationText(), notificationPopup.getText());

        poolProviderDetails.clickCancel();
        Thread.sleep(3_000);

        System.out.println("Edit just created item...");
        poolProviderDetails = poolProvidersPage.editPoolProvider(poolName);
        Thread.sleep(3_000);

        poolName += " [ed]";
        addInstanceURL = "https://yandex.ru/";

        poolProviderDetails.setName(poolName);
        poolProviderDetails.setAddInstanceURL(addInstanceURL);

        poolProviderDetails.clickSave();
        Thread.sleep(4_000);

        System.out.println("Making sure that pool was edited successfully...");

        Assert.assertEquals(poolName, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#poolProviders\\\\:poolProvidersTable_data tr td:contains(\"" + poolName + "\")').text()")));
        Assert.assertEquals("Metadata URL: https://www.google.com/Add instance URL: https://yandex.ru/Delete instance URL: https://stackoverflow.comValidate instance URL: https://www.youtube.com/watch?v=JMUxFas6U1Y",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#poolProviders\\\\:poolProvidersTable_data tr td:contains(\"" + poolName + "\")').next().text()")));

        System.out.println("Delete pool provider...");
        DeletePoolProvider deletePoolProviderPopup = poolProvidersPage.deletePoolProvider(poolName);
        Thread.sleep(3_000);

        deletePoolProviderPopup.clickYes();
        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.POOL_PROVIDER_WAS_SUCCESSFULLY_REMOVED.getNotificationText(), notificationPopup.getText());

        Thread.sleep(4_000);
    }
}
