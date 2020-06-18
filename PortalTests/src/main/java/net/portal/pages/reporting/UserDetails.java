package net.portal.pages.reporting;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class UserDetails extends PageObject
{
    @FindBy(id = "form:startDateFilter_input")
    private WebElement startDateField;

    @FindBy(id = "form:endDateFilter_input")
    private WebElement endDateField;

    @FindBy(id = "form:applyButton")
    private WebElement applyButton;



    public UserDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Reporting > User Details") );
    }

    public void setUser(String username)
    {
        // expand
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:userDropDownList span').click()");

        // select
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:userDropDownList_items li:contains(\"" + username + "\")').click()");
    }

    public void setStartFilterDate(String startDate)
    {
        startDateField.clear();
        startDateField.sendKeys(startDate);
    }

    public void setEndFilterDate(String endDate)
    {
        endDateField.clear();
        endDateField.sendKeys(endDate);
    }

    public void clickApplyButton()
    {
        applyButton.click();
        System.out.println("User Details : Apply filer button was clicked");
    }
}
