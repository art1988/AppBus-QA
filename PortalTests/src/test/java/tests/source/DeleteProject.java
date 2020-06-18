package tests.source;

import net.portal.forms.DeleteJSlibrary;
import net.portal.forms.RemoveProject;
import net.portal.pages.service_management.ServiceCatalog;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

public class DeleteProject
{
    @Test
    public void deleteProject() throws InterruptedException
    {
        System.out.println("--------- START OF DeleteProject ---------");

        ServiceCatalog serviceCatalogPage = new ServiceCatalog(FunctionalTest.getDriver());

        serviceCatalogPage.selectJSLibraries();
        Thread.sleep(4_000);

        // Delete JS Library
        DeleteJSlibrary deleteJSlibraryPopup = serviceCatalogPage.deleteJSLibrary("Upload_from_file");
        Thread.sleep(2_000);

        deleteJSlibraryPopup.clickYes();
        Thread.sleep(4_000);

        Assert.assertFalse(String.valueOf(((JavascriptExecutor)FunctionalTest.getDriver()).executeScript("return $('#serviceCatalogForm\\\\:jsLibsTable_data tr td:nth-child(1)').text()")).contains("Upload_from_file"));

        RemoveProject removeProjectPopup = serviceCatalogPage.clickRemoveProject();
        Thread.sleep(3_000);

        removeProjectPopup.clickYes();
        Thread.sleep(3_000);

        String projName = "AT Proj 5";

        System.out.println("Making sure that project was deleted successfully...");
        ((JavascriptExecutor)FunctionalTest.getDriver()).executeScript("$('#serviceCatalogForm\\\\:projectsSelect_label').click()"); // expand dropdown
        Thread.sleep(500);

        Assert.assertFalse(String.valueOf(((JavascriptExecutor)FunctionalTest.getDriver()).executeScript("return $('#serviceCatalogForm\\\\:projectsSelect_panel').text()")).contains(projName));

        ((JavascriptExecutor)FunctionalTest.getDriver()).executeScript("$('#serviceCatalogForm\\\\:projectsSelect_label').click()"); // close dropdown

        Thread.sleep(5_000);

        System.out.println("--------- END OF DeleteProject ---------");
    }
}
