package tests.source;

import net.portal.forms.CreateService;
import net.portal.forms.EditServiceName;
import net.portal.pages.HeaderMenu;
import net.portal.pages.service_management.ServiceCatalog;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

public class AddJSService
{
    @Test
    public void addJSService() throws InterruptedException
    {
        System.out.println("--------- START OF AddJSService ---------");

        ServiceCatalog serviceCatalogPage = new ServiceCatalog(FunctionalTest.getDriver());

        serviceCatalogPage.selectServices();

        CreateService createService = serviceCatalogPage.clickCreateService();
        Thread.sleep(3_000);

        createService.selectType("JS service");
        Thread.sleep(3_000);
        createService.clickNext();
        Thread.sleep(10_000);

        System.out.println("Make sure that JS code is already in the editor...");
        Assert.assertTrue(serviceCatalogPage.getCode("serverCodeScriptEditor").startsWith("/**\n" + " * A server-side script allows you"));

        String jsServiceName = "JSService_AT";
        serviceCatalogPage.setName(jsServiceName, "serverCodeScriptEditor");

        serviceCatalogPage.clickScriptParametersTab();
        Thread.sleep(3_000);

        serviceCatalogPage.setRequestMethod("GET");
        serviceCatalogPage.setParamName("devName");
        serviceCatalogPage.clickAddParamButton();
        Thread.sleep(3_000);
        serviceCatalogPage.setParamValue("devName", "AKM");
        Thread.sleep(3_000);

        serviceCatalogPage.clickRunTab();
        serviceCatalogPage.clickSave("serverCodeScriptEditor"); // Need to Save first because hitting by 'Save and Run' doesn't work (Appery issue)
        Thread.sleep(3_000);

        serviceCatalogPage.clickSaveAndRunButton();
        Thread.sleep(8_000);

        System.out.println("Asserting response...");
        Thread.sleep(2_000);

        Assert.assertEquals("application/json200",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $($('[id=\"serverCodeScriptEditor\"]')[0].contentDocument).find(\".responseTable div\").text()")));

        Assert.assertTrue(String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $($('[id=\"serverCodeScriptEditor\"]')[0].contentDocument).find(\"#ResponseBodyTextArea\").val()")).startsWith("{\n" + "\t\"result\": \"Hello AKM!\""));

        serviceCatalogPage.clickCloseEditor();
        Thread.sleep(5_000);

        System.out.println("Edit just created JS Service...");
        EditServiceName editServiceName = serviceCatalogPage.editJSService(jsServiceName);
        Thread.sleep(1_000);

        jsServiceName += " [edited]";
        editServiceName.setName(jsServiceName);
        editServiceName.clickSave();
        Thread.sleep(4_000);

        System.out.println("Checking that new name was applied...");
        Assert.assertEquals(jsServiceName,
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#serviceCatalogForm\\\\:serviceTable_data tr td:contains(\"AT\")').text()")));

        serviceCatalogPage.openAPISpecification(jsServiceName);
        Thread.sleep(3_000);

       // Assert.assertEquals("AT Proj 5 latest [ Base URL: DEV-MSA-QA.botf03.net:9613 ]", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('.info').text()")));

        // Click GET button
        ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('.opblock-summary-method').click()");
        Thread.sleep(3_000);

        Assert.assertEquals("devName", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('.parameter__name').text()")));

        serviceCatalogPage.clickCloseOpenAPISpecification();
        Thread.sleep(4_000);

        serviceCatalogPage.openUIEditor(jsServiceName);
        Thread.sleep(9_000);

        serviceCatalogPage.clickScriptParametersTab();
        Thread.sleep(3_000);

        serviceCatalogPage.setRequestMethod("GET");
        serviceCatalogPage.setParamName("newP_Test");
        serviceCatalogPage.clickAddParamButton();
        Thread.sleep(3_000);
        serviceCatalogPage.setParamValue("newP_Test", "VaL_31");
        Thread.sleep(3_000);

        serviceCatalogPage.clickRunTab();
        Thread.sleep(3_000);

        serviceCatalogPage.clickSaveAndRunButton();
        Thread.sleep(5_000);

        serviceCatalogPage.clickCloseEditor();
        Thread.sleep(5_000);

        serviceCatalogPage.openAPISpecification(jsServiceName);
        Thread.sleep(3_000);

        System.out.println("Making sure that just added param is also in the list... [ED-4031]"); // Check of ED-4031

        // GET was already expanded
        Assert.assertEquals("devNamenewP_Test", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('.parameter__name').text()")));

        serviceCatalogPage.clickCloseOpenAPISpecification();
        Thread.sleep(4_000);

        System.out.println("--------- END OF AddJSService ---------");
    }
}
