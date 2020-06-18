package net.portal.forms;

import net.portal.pages.DeleteConfirmPopup;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

public class PolicyAssDetailMultipleValues  extends PageObject

{
    public PolicyAssDetailMultipleValues(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
        // TODO: if click edit of Policy Value -> then need to init policyValueIndex
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#multipleValuesDlg_title').text()").equals("Multiple values") );
    }

    @FindBy(xpath = "//*[@role='button' and contains(.,'Add')]")
    private WebElement addValueButton;

    @FindBy(xpath = "//span[@id='multipleValuesDlg_title']")
    private WebElement mvTitle;

    @FindBy(xpath = "//span[text()='Values']")
    private WebElement headOfTable;

    public WebElement tempAddValueButton;


    public WebElement getAddValueButton() throws InterruptedException
    {
        headOfTable.click();
        Thread.sleep(1_000);
        //driver.switchTo().activeElement().sendKeys(Keys.valueOf("SHIFT" + "TAB"));
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        tempAddValueButton = driver.switchTo().activeElement();
        return tempAddValueButton;
    }

    public void setFocuseOnFirstField() throws InterruptedException

    {
        mvTitle.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);

    }

    public void clickTmpElem(WebElement tmpElem) throws InterruptedException
    {
        Thread.sleep(1_000);
        tmpElem.click();
    }

}
