package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class RdpDetails extends PageObject
{
    @FindBy(id = "entity:dialogsForm:computerIp")
    private WebElement computerIPField;

    @FindBy(id = "entity:dialogsForm:computerName")
    private WebElement computerNameFiled;

    @FindBy(id = "entity:dialogsForm:computerPort")
    private WebElement computerPortFiled;

    @FindBy(id = "entity:dialogsForm:computerDomain")
    private WebElement computerDomainFiled;

    @FindBy(id = "entity:dialogsForm:username")
    private WebElement usernameFiled;

    // Add in case if Add New was clicked
    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addButton;

    // Save in case if Edit button was clicked
    @FindBy(id = "entity:dialogsForm:saveEntity")
    private WebElement saveButton;


    public RdpDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Rdp details") );
    }

    public void setComputerIP(String ip)
    {
        computerIPField.clear();
        computerIPField.sendKeys(ip);
    }

    public void setComputerName(String name)
    {
        computerNameFiled.clear();
        computerNameFiled.sendKeys(name);
    }

    public void setComputerPort(String port)
    {
        computerPortFiled.clear();
        computerPortFiled.sendKeys(port);
    }

    public void setComputerDomain(String domain)
    {
        computerDomainFiled.clear();
        computerDomainFiled.sendKeys(domain);
    }

    public void setUsername(String username)
    {
        usernameFiled.clear();
        usernameFiled.sendKeys(username);
    }

    public void clickAdd()
    {
        addButton.click();
        System.out.println("RdpDetails : Add button was clicked");
    }

    /**
     * Use this method after editing
     */
    public void clickSave()
    {
        saveButton.click();
        System.out.println("RdpDetails : Save button was clicked");
    }

}
