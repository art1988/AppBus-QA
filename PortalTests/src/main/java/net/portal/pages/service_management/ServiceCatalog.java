package net.portal.pages.service_management;

import net.portal.forms.*;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class ServiceCatalog extends PageObject
{
    @FindBy(id = "serviceCatalogForm:addProjectButton")
    private WebElement createProjectButton;

    @FindBy(id = "serviceCatalogForm:deleteButton") //span[@class='ui-button-text ui-c'][contains(.,'Remove project')]
    private WebElement removeProjectButton;

    @FindBy(xpath = "//button[@id='serviceCatalogForm:removeProjectConfirmYesButton']/span[@class='ui-button-icon-left ui-icon ui-c ui-icon-check']")
    private WebElement yesButtonOfPopUp;

    @FindBy(xpath = "//div[contains(.,'Are you sure you want to delete?')]") //Sure to delete?
    private WebElement sureToDeleteLabel;

    @FindBy(id = "serviceCatalogForm:createJSLibraryButton")
    private WebElement createJSLibraryButton;

    @FindBy(id = "serviceCatalogForm:createServiceButton")
    private WebElement createServiceButton;

    @FindBy(id = "serviceCatalogForm:addJavaLibButton")
    private WebElement addJavaLibButton;

    @FindBy(id = "serviceCatalogForm:downloadLibTemplateButton")
    private WebElement downloadTemplateButton;

    // Editor controls
    @FindBy(id = "serviceCatalogForm:closeEditorButton")
    private WebElement closeEditorButton;

    @FindBy(id = "serviceCatalogForm:closeSwaggerButton")
    private WebElement closeOpenAPISpecificationButton;


    public ServiceCatalog(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Service Management > Service Catalog") );
    }

    public void clickCloseEditor()
    {
        closeEditorButton.click();
        System.out.println("ServiceCatalog : Close editor was clicked");
    }

    public void clickCloseOpenAPISpecification()
    {
        closeOpenAPISpecificationButton.click();
        System.out.println("ServiceCatalog : Close OpenAPI Specification was clicked");
    }

    /**
     * Set name for specific Editor
     * @param name name to set
     * @param editorId may be jsLibsEditor(Create JS library) or serverCodeScriptEditor(Create JS service)
     */
    public void setName(String name, String editorId)
    {
        ((JavascriptExecutor)driver).executeScript("$($('[id=\"" + editorId + "\"]')[0].contentDocument).find(\"tbody input\").val(\"" + name + "\")");
    }

    /**
     * Set code for specific Editor
     * @param codeText code to set
     * @param editorId may be jsLibsEditor(Create JS library) or serverCodeScriptEditor(Create JS service)
     */
    public void setCode(String codeText, String editorId)
    {
        StringBuffer jsAceCode = new StringBuffer("inner = $($('[id=\"" + editorId + "\"]')[0].contentDocument).find(\".ace_wrapper_inner.ace_editor.ace-xcode\")[0]; ");
        jsAceCode.append("iframe=$('#" + editorId + "')[0]; ");
        jsAceCode.append("e=iframe.contentWindow.ace.edit(inner); ");
        jsAceCode.append("e.setValue(\"" + codeText + "\"); ");

        ((JavascriptExecutor)driver).executeScript(jsAceCode.toString());
    }

    public void setDescription(String description)
    {
        StringBuffer jsAceCode = new StringBuffer("inner = $($('[id=\"jsLibsEditor\"]')[0].contentDocument).find(\".ace_wrapper_inner.ace_editor.ace-xcode\")[1]; ");
        jsAceCode.append("iframe=$('#jsLibsEditor')[0]; ");
        jsAceCode.append("e=iframe.contentWindow.ace.edit(inner); ");
        jsAceCode.append("e.setValue(\"" + description + "\"); ");

        ((JavascriptExecutor)driver).executeScript(jsAceCode.toString());
    }

    /**
     * Get code from specific Editor
     * @param editorId may be jsLibsEditor(Create JS library) or serverCodeScriptEditor(Create JS service)
     * @return text from Ace Editor
     */
    public String getCode(String editorId)
    {
        StringBuffer jsAceCode = new StringBuffer("inner = $($('[id=\"" + editorId + "\"]')[0].contentDocument).find(\".ace_wrapper_inner.ace_editor.ace-xcode\")[0]; ");
        jsAceCode.append("iframe=$('#" + editorId + "')[0]; ");
        jsAceCode.append("e=iframe.contentWindow.ace.edit(inner); ");
        jsAceCode.append("return e.session.getValue(); ");

        return String.valueOf(((JavascriptExecutor)driver).executeScript(jsAceCode.toString()));
    }

    public void clickTest()
    {
        ((JavascriptExecutor)driver).executeScript("$($('[id=\"jsLibsEditor\"]')[0].contentDocument).find(\"#test\").click()");
        System.out.println("Test button was clicked");
    }

    /**
     * Click Save button
     * @param editorId may be jsLibsEditor(Create JS library) or serverCodeScriptEditor(Create JS service)
     */
    public void clickSave(String editorId)
    {
        ((JavascriptExecutor)driver).executeScript("$($('[id=\"" + editorId + "\"]')[0].contentDocument).find(\"tbody .save-script\").click()");
        System.out.println("Save button was clicked");
    }

    public void clickDownload()
    {
        ((JavascriptExecutor)driver).executeScript("$($('[id=\"jsLibsEditor\"]')[0].contentDocument).find(\"#downloadSourceCode i\").click()");
    }

    /**
     * Click Load from file link to upload sorce code of Edit tab
     * @param fullPathToFile
     */
    public void clickUploadSourceCode(String fullPathToFile)
    {
        // Switch to iframe by name
        driver.switchTo().frame("jsLibsEditor");

        WebElement loadFromFileInputElement = driver.findElement(By.id("loadSourceCodeInput"));
        loadFromFileInputElement.sendKeys(fullPathToFile);

        // Switch back to whole <html> element
        driver.switchTo().defaultContent();
    }

    /**
     * Click Load from file link to upload description of API information tab
     * @param fullPathToFile
     */
    public void clickUploadDescription(String fullPathToFile)
    {
        // Switch to iframe by name
        driver.switchTo().frame("jsLibsEditor");

        WebElement loadFromFileInputElement = driver.findElement(By.id("loadDescriptionInput"));
        loadFromFileInputElement.sendKeys(fullPathToFile);

        // Switch back to whole <html> element
        driver.switchTo().defaultContent();
    }

    public CreateProject clickCreateProject()
    {
        createProjectButton.click();
        System.out.println("ServiceCatalog : Create project button was clicked");

        return new CreateProject(driver);
    }

    public RemoveProject clickRemoveProject() throws InterruptedException
    {
        removeProjectButton.click();
        System.out.println("ServiceCatalog : Remove project button was clicked");

        return new RemoveProject(driver);
    }

    public CreateService clickCreateService()
    {
        createServiceButton.click();
        System.out.println("ServiceCatalog : Create Service button was clicked");

        return new CreateService(driver);
    }

    public ServiceCatalog clickCreateJSLibrary()
    {
        createJSLibraryButton.click();
        System.out.println("ServiceCatalog : Create JS library button was clicked");

        // Switch to iframe by name
        driver.switchTo().frame("jsLibsEditor");

        // Wait up to 15 seconds until Library label is visible since
        WebElement testLibraryLabel = (new WebDriverWait(driver, 60)).until(ExpectedConditions.visibilityOfElementLocated(By.id("ui-id-14")));

        // Switch back to whole <html> element
        driver.switchTo().defaultContent();

        return this;
    }

    public JavaLibrary clickAddJavaLib()
    {
        addJavaLibButton.click();
        System.out.println("ServiceCatalog : Add Java Lib button was clicked");

        return new JavaLibrary(driver);
    }

    /**
     * Edit js library by name
     * @param name
     */
    public void editJSLibrary(String name)
    {
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:jsLibsTable_data tr td:contains(\"" + name + "\")').next().next().next().find(\"button\")[0].click()");

        // Switch to iframe by name
        driver.switchTo().frame("jsLibsEditor");

        // Wait up to 15 seconds until Library label is visible since
        WebElement testLibraryLabel = (new WebDriverWait(driver, 15)).until(ExpectedConditions.visibilityOfElementLocated(By.id("ui-id-16")));

        // Switch back to whole <html> element
        driver.switchTo().defaultContent();
    }

    public EditServiceName editJSService(String name)
    {
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:serviceTable_data tr td:contains(\"" + name + "\")').next().next().next().next().find(\"button\")[3].click()");
        System.out.println("Edit the following JS Service: " + name);

        return new EditServiceName(driver);
    }

    public DeleteService deleteJSService(String name)
    {
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:serviceTable_data tr td:contains(\"" + name + "\")').next().next().next().next().find(\"button\")[5].click()");

        return new DeleteService(driver);
    }

    public void openAPISpecification(String jsServiceName) throws InterruptedException
    {
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:serviceTable_data tr td:contains(\"" + jsServiceName + "\")').next().next().next().next().find(\"button\")[0].click()");
        System.out.println("Click Open API Specification for the following JS Service: " + jsServiceName);

        Thread.sleep(3_000);
    }

    /**
     * Click Open UI editor
     * @param serviceName may be JS Service or REST service
     */
    public void openUIEditor(String serviceName)
    {
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:serviceTable_data tr td:contains(\"" + serviceName + "\")').next().next().next().next().find(\"button\")[4].click()");
        System.out.println("Open UI Editor for the following JS Service: " + serviceName);
    }

    public void clickEditTab()
    {
        ((JavascriptExecutor)driver).executeScript("$($('[id=\"jsLibsEditor\"]')[0].contentDocument).find(\"a:contains('Edi')\")[0].click()");
        System.out.println("Edit tab was clicked");
    }

    public void clickAPIInformationTab()
    {
        ((JavascriptExecutor)driver).executeScript("$($('[id=\"jsLibsEditor\"]')[0].contentDocument).find(\"a:contains('API')\")[0].click()");
        System.out.println("API information tab was clicked");
    }

    public void clickScriptParametersTab()
    {
        ((JavascriptExecutor)driver).executeScript("$($('[id=\"serverCodeScriptEditor\"]')[0].contentDocument).find(\"a:contains('parameters')\")[0].click()");
        System.out.println("Script parameters tab was clicked");
    }

    public void clickRunTab()
    {
        ((JavascriptExecutor)driver).executeScript("$($('[id=\"serverCodeScriptEditor\"]')[0].contentDocument).find(\"a:contains('Run')\")[0].click()");
        System.out.println("Run tab was clicked");
    }

    /*
    public void selectMIMEType(String type)
    {
        ((JavascriptExecutor)driver).executeScript("$($('[id=\"jsLibsEditor\"]')[0].contentDocument).find(\"span:contains('Text')\")[0].click()");

    }*/

    /**
     * Set Request method: GET or POST
     * @param value
     */
    public void setRequestMethod(String value)
    {
        StringBuffer jsCode = new StringBuffer("var select = $($('[id=\"serverCodeScriptEditor\"]')[0].contentDocument).find(\"#requestMethod\")[0];");
        jsCode.append("select.value = '" + value + "';");
        jsCode.append("var event = new Event('change', { bubbles: true });");
        jsCode.append("select.dispatchEvent(event);");

        ((JavascriptExecutor)driver).executeScript(jsCode.toString());
    }

    public void setParamName(String paramName)
    {
        ((JavascriptExecutor)driver).executeScript("$($('[id=\"serverCodeScriptEditor\"]')[0].contentDocument).find(\"#paramName\").val(\"" + paramName + "\")");
    }

    public void clickAddParamButton()
    {
        ((JavascriptExecutor)driver).executeScript("$($('[id=\"serverCodeScriptEditor\"]')[0].contentDocument).find(\"#add\").click()");
        System.out.println("Add Param button was clicked");
    }

    /**
     * Set paramValue for paramName
     * @param paramName name of parameter
     * @param paramValue value to set for paramName
     */
    public void setParamValue(String paramName, String paramValue)
    {
        StringBuffer jsCode = new StringBuffer("var input = $($('[id=\"serverCodeScriptEditor\"]')[0].contentDocument).find(\"#params-scroll-wrapper\").find('input[value=\"" + paramName + "\"]').parent().next().next().find(\"input\")[0];");
        jsCode.append("input.value = '" + paramValue + "';");
        jsCode.append("var event = new Event('change', { bubbles: true });");
        jsCode.append("input.dispatchEvent(event);");

        ((JavascriptExecutor)driver).executeScript(jsCode.toString());
    }

    public void clickSaveAndRunButton()
    {
        ((JavascriptExecutor)driver).executeScript("$($('[id=\"serverCodeScriptEditor\"]')[0].contentDocument).find(\"#run_tab button\")[0].click()");
        System.out.println("Save and run button was clicked");
    }

    public DeleteJSlibrary deleteJSLibrary(String jsLibraryName)
    {
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:jsLibsTable_data tr td:contains(\"" + jsLibraryName + "\")').next().next().next().find(\"button\")[1].click()");

        return new DeleteJSlibrary(driver);
    }

    public DeleteJavaLib deleteJavaLib(String javaLibName)
    {
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:javaLibTable_data tr td:contains(\"" + javaLibName + "\")').next().next().next().find(\"button\")[2].click()");

        return new DeleteJavaLib(driver);
    }

    /**
     * Select JS libraries item from Services dropdown
     */
    public void selectJSLibraries()
    {
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:typeSelect_label').click()");
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:typeSelect_3').click()");
    }

    /**
     * Select Java libraries item from Services dropdown
     */
    public void selectJavaLibraries()
    {
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:typeSelect_label').click()");
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:typeSelect_1').click()");
    }

    /**
     * Select Services item from Services dropdown
     */
    public void selectServices()
    {
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:typeSelect_label').click()");
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:typeSelect_0').click()");
    }

    /**
     * Select project by name
     */
    public void selectProject(String projectName)
    {
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:projectsSelect_label').click()");
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:projectsSelect_items li:contains(\"" + projectName + "\")').click()");
        System.out.println("Project with name : " + projectName + " was selected");
    }


    public void downloadJavaLibrary(String javaLibName)
    {
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:javaLibTable_data tr td:contains(\"" + javaLibName + "\")').next().next().next().find(\"button\")[0].click()");
    }

    public JavaLibrary editJavaLibrary(String javaLibName)
    {
        ((JavascriptExecutor)driver).executeScript("$('#serviceCatalogForm\\\\:javaLibTable_data tr td:contains(\"" + javaLibName + "\")').next().next().next().find(\"button\")[1].click()");

        return new JavaLibrary(driver);
    }

    public void clickDownloadLibTemplate()
    {
        downloadTemplateButton.click();
    }

    /**
     * Click TEST button in Appery iframe
     */
    public void clickTESTbutton()
    {
        ((JavascriptExecutor)driver).executeScript("$($('[id=\"apiExpressServiceEditor\"]')[0].contentDocument).find(\".btn.btn-default.btn-sm:contains('Test')\")[0].click()");

        System.out.println("TEST button was clicked");
    }
}
