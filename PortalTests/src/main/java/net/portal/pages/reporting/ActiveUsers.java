package net.portal.pages.reporting;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

public class ActiveUsers extends PageObject
{
    @FindBy(xpath = "//span[@class='ui-button-icon-left ui-icon ui-icon-calendar']")
    private WebElement calendarButton;

    @FindBy(id = "activeUser:filterApplyButton")
    private WebElement filterApplyButton;

    @FindBy(id = "activeUser:date_input")
    private WebElement dateInputField;

    @FindBy(id = "activeUser:dataTable_head")
    private WebElement headRowOfTable;

    @FindBy(xpath = "//th[contains(.,'UserFilter by User')]")
    private WebElement userFilterCell;

    @FindBy(xpath = "//span[@class='ui-column-title'][contains(.,'Application')]/..")
    private WebElement applFilterCell;

    @FindBy(xpath = "//img[@src='/edapt-admin/images/printer.gif']")
    private WebElement printerIcon;

    public ActiveUsers(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Reporting > Active Users") );
    }

    public void clickCSVIcon()
    {
        ((JavascriptExecutor) driver).executeScript("$('#activeUser\\\\:csvIcon').click()");

        System.out.println("CSV icon was clicked...");
    }

    public void clickCalendarButton()
    {
        calendarButton.click();
        System.out.println("ActiveUsers: Calendar button was clicked...");
    }

    public void clickApplyButton()
    {
        filterApplyButton.click();
        System.out.println("ActiveUsers: Apply button was clicked...");
    }

    public void setTime(String dateTime) throws InterruptedException
    {
        dateInputField.click();
        Thread.sleep(1_000);
        dateInputField.clear();
        Thread.sleep(1_000);
        dateInputField.sendKeys(dateTime);
        System.out.println("ActiveUsers: Data/Time was set...");
    }

    public String getRowText(String uniqueCellText) throws InterruptedException
    {
        String xP = "//td[contains(.,'" + uniqueCellText + "')]/../.."; //"//span[contains(.,'" + uniqueCellText + "')]/../..";
        WebElement tD = driver.findElement(By.xpath(xP));
        System.out.println("tD is :" + tD.getText());

        return tD.getText();
    }

    public String getTableText(String uniqueCellText) throws InterruptedException
    {
        String xP = "//td[contains(.,'" + uniqueCellText + "')]/../../.."; //span[contains(.,'" + uniqueCellText + "')]/../../..
        WebElement tB = driver.findElement(By.xpath(xP));
        System.out.println("-------------------------------------------------------");
        System.out.println("tB is :" + tB.getText());
        System.out.println("-------------------------------------------------------");

        return tB.getText();
    }

    public void nameFilter(String name) throws InterruptedException
    {
        userFilterCell.findElement(By.tagName("input")).click();
        //userFilterCell.click();
        Thread.sleep(1_000);
        //driver.switchTo().activeElement().sendKeys(Keys.TAB);
        //Thread.sleep(1_000);
        driver.switchTo().activeElement().clear(); //Time
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(name);
        System.out.println("just entered the following name to filter : " + name);

    }

    public void applicationFilter(String appName) throws InterruptedException
    {
        applFilterCell.findElement(By.tagName("input")).click();
        //applFilterCell.click();
        Thread.sleep(2_000);
        //driver.switchTo().activeElement().sendKeys(Keys.TAB);
        //Thread.sleep(1_000);
        driver.switchTo().activeElement().clear();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(appName);
        System.out.println("just entered the following application name to filter : " + appName);

    }

    public void clickPrinterIcon() throws InterruptedException
    {
        Thread.sleep(1_000);
        //printerIcon.click();
        dateInputField.click();
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.ENTER);
        Thread.sleep(1_000);
    }

}
