package tests.source;

import net.portal.forms.CreateService;
import net.portal.pages.service_management.ServiceCatalog;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.util.Set;

public class AddRESTService
{
    @Test
    public void addRESTService() throws InterruptedException
    {
        System.out.println("--------- START OF AddRESTService ---------");

        ServiceCatalog serviceCatalogPage = new ServiceCatalog(FunctionalTest.getDriver());

        serviceCatalogPage.selectServices();

        CreateService createService = serviceCatalogPage.clickCreateService();
        Thread.sleep(2_000);

        createService.selectType("REST service");
        createService.clickNext();
        Thread.sleep(40_000);

        System.out.println("Making sure that main <iframe> of Services is visible...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#apiExpressServiceEditor').is(':visible')"));

        Thread.sleep(1_000);

        serviceCatalogPage.clickCloseEditor();
        Thread.sleep(5_000);

        System.out.println("TEST some existing REST Service...");
        serviceCatalogPage.selectProject("Artur");
        Thread.sleep(3_000);

        serviceCatalogPage.openUIEditor("Ex_REST"); // Ex_REST
        Thread.sleep(8_000);

        String originalTab = FunctionalTest.getDriver().getWindowHandle();
        Set<String> oldWindowsSet = FunctionalTest.getDriver().getWindowHandles();

        serviceCatalogPage.clickTESTbutton();

        String newTab = (new WebDriverWait(FunctionalTest.getDriver(), 5))
                .until(new ExpectedCondition<String>() {
                           public String apply(WebDriver driver) {
                               Set<String> newWindowsSet = driver.getWindowHandles();
                               newWindowsSet.removeAll(oldWindowsSet);
                               return newWindowsSet.size() > 0 ?
                                       newWindowsSet.iterator().next() : null;
                           }
                       }
                );

        // Switch to Service test tab
        FunctionalTest.getDriver().switchTo().window(newTab);

        WebElement buttonTest = (new WebDriverWait(FunctionalTest.getDriver(), 25)).until(ExpectedConditions.visibilityOfElementLocated(By.id("buttonTest")));
        Assert.assertTrue(buttonTest.isDisplayed());

        Assert.assertEquals("Service test", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#projects_tree_container h2').eq(0).text().trim()")));

        System.out.println("Click Test service button...");
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('#buttonTest').click()");
        Thread.sleep(4_000);

        System.out.println("Check that response code is 200 and length is 166 bytes...");

        Assert.assertEquals("200 Success", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#projects_tree_container .control-label:contains(\"HTTP\")').next().text()")));
        Assert.assertEquals("166 bytes", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#projects_tree_container .control-label:contains(\"Length\")').next().text()")));

        System.out.println("Closing Service test tab...");
        FunctionalTest.getDriver().close();

        // Switch back to original tab
        FunctionalTest.getDriver().switchTo().window(originalTab);
        Thread.sleep(2_000);

        serviceCatalogPage.clickCloseEditor();
        Thread.sleep(5_000);

        serviceCatalogPage.selectProject("AT Proj 5");
        Thread.sleep(2_000);

        System.out.println("--------- END OF AddRESTService ---------");
    }
}
