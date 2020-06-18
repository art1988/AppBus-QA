package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class CreateProject extends PageObject
{
    @FindBy(name = "addProjectForm:projectName")
    private WebElement nameField;

    @FindBy(id = "addProjectForm:projectSaveButton")
    private WebElement saveButton;

    @FindBy(id = "addProjectForm:projectCancelButton")
    private WebElement cancelButton;


    public CreateProject(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#addProjectDlg_title').text()").equals("Create project") );
    }

    public void setName(String projectName)
    {
        nameField.sendKeys(projectName);
    }

    public void clickSave()
    {
        saveButton.click();
        System.out.println("CreateProject : Save button was clicked");
    }

    public void clickCancel()
    {
        cancelButton.click();
        System.out.println("CreateProject : Cancel button was clicked");
    }
}
