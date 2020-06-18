package net.portal.forms;

import net.portal.constants.Retries;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class SelectParentItem extends PageObject
{
    @FindBy(id = "ownerItemSelectDlgForm:okButtonNotForOwner")
    private WebElement okButton;

    @FindBy(xpath = "//span[contains(.,'Select parent item')]")
    private WebElement winTitle;

    public SelectParentItem(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#ownerItemSelectDlg_title').text()").equals("Select parent item"));
    }

    public void selectParentItem(String item) throws InterruptedException
    {
        // expand dropdown
        ((JavascriptExecutor) driver).executeScript("$('#ownerItemSelectDlgForm\\\\:ownerItemSelectDropDown label').click()");

        Thread.sleep(1_000);

        // select item
        ((JavascriptExecutor) driver).executeScript("$('#ownerItemSelectDlgForm\\\\:ownerItemSelectDropDown_items li:contains(\"" + item + "\")').click()");
    }

    public MoveToItemAsChild clickOk()
    {
        okButton.click();
        System.out.println("SelectParentItem : Ok button was clicked");
        return new MoveToItemAsChild(driver);
    }

    public MoveToItemAsChild clickOkByTab() throws InterruptedException
    {
        Thread.sleep(1_000);
        Retries.RETRY_10_TIMES.run(() -> winTitle.click()); //Retry
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);
        System.out.println("SelectParentItem : Ok button was selected by TABs and clicked");

        return new MoveToItemAsChild(driver);
    }
}
