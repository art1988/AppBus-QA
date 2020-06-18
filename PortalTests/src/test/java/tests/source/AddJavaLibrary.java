package tests.source;

import net.portal.constants.Const;
import net.portal.constants.Notifications;
import net.portal.forms.DeleteJavaLib;
import net.portal.forms.JavaLibrary;
import net.portal.pages.service_management.ServiceCatalog;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;

public class AddJavaLibrary
{
    @Test
    public void addJavaLibrary() throws InterruptedException
    {
        System.out.println("--------- START OF AddJavaLibrary ---------");

        ServiceCatalog serviceCatalogPage = new ServiceCatalog(FunctionalTest.getDriver());

        serviceCatalogPage.selectJavaLibraries();
        Thread.sleep(3_000);

        JavaLibrary javaLibraryPopup = serviceCatalogPage.clickAddJavaLib();
        Thread.sleep(3_000);

        String javaLibName = "AT Java lib",
               description = "Java library description";

        javaLibraryPopup.setName(javaLibName);
        javaLibraryPopup.setDescription(description);
        javaLibraryPopup.chooseFile(Const.JAVA_FILE_SAMPLE);
        javaLibraryPopup.clickUpload();
        Thread.sleep(2_000);

        javaLibraryPopup.clickSave();
        Thread.sleep(3_000);

        // Add Java lib with the same name -> should get warning notification
        javaLibraryPopup = serviceCatalogPage.clickAddJavaLib();
        Thread.sleep(3_000);

        javaLibraryPopup.setName(javaLibName);

        javaLibraryPopup.clickSave();

        System.out.println("Check uniqueness of Java lib...");
        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.JAVA_LIB_NAME_ALREADY_EXISTS.getNotificationText(), notificationPopup.getText());
        Thread.sleep(1_000);

        javaLibraryPopup.clickCancel();
        Thread.sleep(1_000);

        System.out.println("Trying to download Java library...");
        serviceCatalogPage.downloadJavaLibrary(javaLibName);
        Thread.sleep(3_000);

        // Rename just created Java lib
        javaLibraryPopup = serviceCatalogPage.editJavaLibrary(javaLibName);
        Thread.sleep(1_000);

        javaLibName += " [edited]";
        javaLibraryPopup.setName(javaLibName);
        javaLibraryPopup.clickSave();
        Thread.sleep(3_000);

        // Switch page to JS libraries
        serviceCatalogPage.selectJSLibraries();
        Thread.sleep(3_000);

        // Switch page back to Java libraries and check that new name was saved
        serviceCatalogPage.selectJavaLibraries();
        Thread.sleep(3_000);

        Assert.assertEquals(javaLibName, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#serviceCatalogForm\\\\:javaLibTable_data tr td:nth-child(1)').text()")));
        Assert.assertEquals(description, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#serviceCatalogForm\\\\:javaLibTable_data tr td:nth-child(3)').text()")));

        Thread.sleep(4_000);

        System.out.println("Delete just created Java library");
        DeleteJavaLib deleteJavaLibPopup = serviceCatalogPage.deleteJavaLib(javaLibName);
        Thread.sleep(3_000);

        deleteJavaLibPopup.clickYes();
        Thread.sleep(3_000);

        Assert.assertEquals("No records found.", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#serviceCatalogForm\\\\:javaLibTable_data tr td:nth-child(1)').text()")));

        Thread.sleep(2_000);
        System.out.println("Trying to download lib template...");
        serviceCatalogPage.clickDownloadLibTemplate();

        File libTemplateFile = new File(Const.DOWNLOAD_FOLDER + "\\" + "java-lib-template.zip");
        while ( !libTemplateFile.exists() )
        {
            Thread.sleep(3_000);
        }

        Assert.assertTrue(libTemplateFile.exists());

        // Delete it..
        if(libTemplateFile.delete())
        {
            System.out.println("java-lib-template.zip was successfully deleted");
        }

        System.out.println("--------- END OF AddJavaLibrary ---------");
    }
}
