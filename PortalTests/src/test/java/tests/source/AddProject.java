package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.CreateProject;
import net.portal.pages.HeaderMenu;
import net.portal.pages.service_management.ServiceCatalog;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class AddProject
{
    @Test
    public void addProject() throws InterruptedException
    {
        System.out.println("--------- START OF AddProject ---------");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        ServiceCatalog serviceCatalogPage = headerMenu.clickServiceCatalog();
        Thread.sleep(6_000);

        CreateProject createProjectPopup = serviceCatalogPage.clickCreateProject();
        Thread.sleep(3_000);

        String projName = "AT Proj 5";
        createProjectPopup.setName(projName);
        createProjectPopup.clickSave();
        Thread.sleep(3_000);

        serviceCatalogPage.selectJSLibraries();
        Thread.sleep(4_000);

        System.out.println("Trying to add project with the same name...");
        createProjectPopup = serviceCatalogPage.clickCreateProject();
        Thread.sleep(3_000);

        createProjectPopup.setName(projName);
        createProjectPopup.clickSave();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.PROJECT_NAME_ALREADY_EXISTS.getNotificationText(), notificationPopup.getText());

        createProjectPopup.clickCancel();

        System.out.println("--------- END OF AddProject ---------");
    }
}
