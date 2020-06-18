package net.portal.pages.audit;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Container extends PageObject
{
    @FindBy(id = "form:userFilter")
    private WebElement userFilerField;

    @FindBy(id = "form:restoreFiltersButton")
    private WebElement resetButton;

    @FindBy(id = "form:applyFiltersButton")
    private WebElement applyButton;

    @FindBy(id = "form:startFilterDate_input")
    private WebElement startFilterDateField;

    @FindBy(id = "form:endFilterDate_input")
    private WebElement endFilterDateField;



    public Container(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Audit > Container") );
    }

    public void filterByUser(String username)
    {
        userFilerField.clear();
        userFilerField.sendKeys(username);
    }

    public void clickApply()
    {
        applyButton.click();

        System.out.println("Container : Apply filter button was clicked");
    }

    public void clickReset()
    {
        resetButton.click();

        System.out.println("Container : Reset filter button was clicked");
    }

    /**
     *
     * @param startDate in format MM/dd/yyyy HH:mm
     */
    public void setStartFilterDate(String startDate)
    {
        startFilterDateField.clear();
        startFilterDateField.sendKeys(startDate);
    }

    /**
     *
     * @param endDate in format MM/dd/yyyy HH:mm
     */
    public void setEndFilterDate(String endDate)
    {
        endFilterDateField.clear();
        endFilterDateField.sendKeys(endDate);
    }

    public void setSeverity(String severityName)
    {
        // expand Severity dropdown
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:severity_label').trigger('mousedown')");

        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:severity_panel ul li:contains(\"" + severityName + "\")').find(\"input\").click()");
    }

    /**
     * Trigger columns to show or hide depending on current state. It may be already checked(i.e. shown) or not.
     * @param columnNames list of columns to trigger. Columns names should have precise names !
     */
    public void visibleColumns(String[] columnNames) throws InterruptedException
    {
        // expand Visible columns dropdown
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:visibleColumns_label').trigger('mousedown')");

        for( String columnName : columnNames )
        {
            ((JavascriptExecutor) driver).executeScript("$('.ui-selectcheckboxmenu-items-wrapper ul li:contains(\"" + columnName + "\")').find(\"input\").click()");
            Thread.sleep(3_000);
        }

        // collapse Visible columns dropdown
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:visibleColumns_label').trigger('mousedown')");
        Thread.sleep(1_000);
    }
}
