package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class TableModificationDetails extends PageObject
{
    @FindBy(id = "form:tableModificationDetailOkButton")
    private WebElement okButton;


    public TableModificationDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#form\\\\:tableModificationDlg_title').text()").equals("Table Modification Details") );
    }

    public String getId()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#form\\\\:display tr td:contains(\"Id\")').next().text()"));
    }

    public String getUsername()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#form\\\\:display tr td:contains(\"User\")').next().text()"));
    }

    public String getType()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#form\\\\:display tr td:contains(\"Type\")').next().text()"));
    }

    public String getObject()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#form\\\\:display tr td:contains(\"Obj\")').next().text()"));
    }

    public String getDate()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#form\\\\:display tr td:contains(\"Date\")').next().text()"));
    }

    public void clickOk()
    {
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:tableModificationDetailOkButton').click()");

        System.out.println("TableModificationDetails : Ok button was clicked");
    }
}
