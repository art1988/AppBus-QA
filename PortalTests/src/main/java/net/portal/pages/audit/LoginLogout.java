package net.portal.pages.audit;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class LoginLogout extends PageObject
{
    @FindBy(id = "loginglogoutStatistic:startDateFilter_input")
    private WebElement startDateField;

    @FindBy(id = "loginglogoutStatistic:endDateFilter_input")
    private WebElement endDateField;

    @FindBy(id = "loginglogoutStatistic:filterApplyButton")
    private WebElement applyButton;



    public LoginLogout(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Audit > Login/Logout") );
    }

    public void clickCSVIcon()
    {
        ((JavascriptExecutor) driver).executeScript("$('#printForm a')[0].click()");

        System.out.println("CSV icon was clicked...");
    }

    public void setStartDate(String startDate)
    {
        startDateField.clear();
        startDateField.sendKeys(startDate);
    }

    public void setEndDate(String endDate)
    {
        endDateField.clear();
        endDateField.sendKeys(endDate);
    }

    public void clickApply()
    {
        applyButton.click();

        System.out.println("LoginLogout : Apply filter button was clicked");
    }
}
