package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class StratumGroupDetail extends PageObject
{
    @FindBy(id = "entity:dialogsForm:name")
    private WebElement groupNameFiled;

    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;

    @FindBy(id = "entity:dialogsForm:cancelEntity")
    private WebElement cancelButton;


    public StratumGroupDetail(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Stratum Group Detail") );
    }

    public void setGroupName(String stratumGroupName)
    {
        groupNameFiled.clear();
        groupNameFiled.sendKeys(stratumGroupName);
    }

    public void setStratum(String stratumName) throws InterruptedException
    {
        // expand stratum select - just to make sure that it is visible during test
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:stratums_panel').css(\"top\", \"100px\")");
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:stratums_panel').css(\"left\", \"100px\")");
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:stratums_panel').css(\"display\", \"block\")");
        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:stratums_panel').css(\"z-index\", \"1041\")");

        Thread.sleep(3_000);

        ((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:stratums_panel label:contains(\"" + stratumName + "\")').click()");

        System.out.println(stratumName + " was set as Stratum ");
    }

    public void clickAdd()
    {
        addButton.click();
        System.out.println("StratumGroupDetail : Add button was clicked");
    }

    public void clickCancel()
    {
        cancelButton.click();
        System.out.println("StratumGroupDetail : Cancel button was clicked");
    }
}
