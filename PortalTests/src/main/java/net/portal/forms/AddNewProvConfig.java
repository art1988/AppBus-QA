package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

import java.util.List;

public class AddNewProvConfig extends PageObject
{
    @FindBy(id = "setStartTimeForNewConfigForm:setStartTimeForNewConfigCalendar_input")
    private WebElement startTimeInput;

    @FindBy(id = "setStartTimeForNewConfigForm:setStartTimeForNewConfigButton")
    private WebElement okButton;

    @FindBy(id = "setNewStartTimeForExpiredConfigForm:updateExpiredConfig")
    private WebElement okTurningButton;

    @FindBy(xpath = "//a[contains(@class,'ui-state-default ui-state-highlight')]")
    private WebElement currentDateButton;

    @FindBy(xpath = "//a[@class='ui-state-default'][contains(.,'1')]")
    private WebElement theFirstDateButton;

    @FindBy(xpath = "//span[@class='ui-icon ui-icon-circle-triangle-e'][contains(.,'Next')]/..")
    private WebElement nextMonthTriangle;

    @FindBy(id = "ui-datepicker-div")
    private WebElement calendar;


    public AddNewProvConfig(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return (
                ((JavascriptExecutor) driver).executeScript("return $('#setStartTimeForNewConfigDlg_title').text()").equals("Add new config")
                        ||
                        ((JavascriptExecutor) driver).executeScript("return $('#setStartTimeForNewConfigDlg_title').text()").equals("Turn to upcoming"));
    }

    public void setStartTime(String date) throws InterruptedException
    {
        startTimeInput.click();
        Thread.sleep(1_000);
        startTimeInput.clear();
        Thread.sleep(1_000);
        startTimeInput.sendKeys(date);
        System.out.println("AddNewProvConfig : setStartTime : date was set... : " + date);
    }

    public void clickStartTime() throws InterruptedException
    {
        startTimeInput.click();
        Thread.sleep(1_000);
        System.out.println("AddNewProvConfig : clickStartTime : Start Time input was clicked... : ");
    }

    public void clickOk() throws InterruptedException
    {
        okButton.click();
        Thread.sleep(1_000);
        System.out.println("AddNewProvConfig : clickOk : Ok button was clicked");
    }

    public void clickOkTurning() throws InterruptedException
    {
        okTurningButton.click();
        Thread.sleep(1_000);
        System.out.println("AddNewProvConfig : clickOkTurning : Ok button was clicked");
    }

    public void clickCurrentDate() throws InterruptedException
    {
        currentDateButton.click();
        Thread.sleep(1_000);
        System.out.println("AddNewProvConfig : clickCurrentDate : Current Date button was clicked");
    }

    public String getStartTimeValue() throws InterruptedException
    {
        String date = startTimeInput.getText();
        Thread.sleep(1_000);
        System.out.println("AddNewProvConfig : getStartTimeValue : Date value is gotten");

        return date;
    }

    public boolean clickTomorrowDay() throws InterruptedException
    {
        boolean done = false;
        int itemNumber = 100;
        List<WebElement> items = calendar.findElements(By.xpath("//td[@data-handler='selectDay']"));
        Thread.sleep(1_000);
        System.out.println("AddNewProvConfig : items.size() is : " + items.size());
        for(int i=0; i < items.size(); i++)
        {
            String selected = items.get(i).getAttribute("class");
            if (selected.contains("ui-datepicker-today"))
            {
                itemNumber = i;
                System.out.println("AddNewProvConfig : detected day is : " + items.get(i).getText());
                System.out.println("AddNewProvConfig : detected day is : " + items.get(i).findElement(By.xpath("//td/a[@href='#']")).getAttribute("outerHTML").toString());
                System.out.println("AddNewProvConfig : detected day is : " + items.get(i).getAttribute("class").toString());
            }

        }
        Thread.sleep(1_000);
        if (itemNumber < items.size() - 1)
        {
            itemNumber++; items.get(itemNumber).click(); done = true;
        }
        else
            {
                //nextMonthTriangle.click();
                List<WebElement> Titems = calendar.findElements(By.xpath("//span[@class='ui-icon ui-icon-circle-triangle-e']"));
                System.out.println("Titems.size(): " + Titems.size());
                Titems.get(0).click();
                Thread.sleep(1_000);
                theFirstDateButton.click();
                done = true;
            }
        Thread.sleep(1_000);
        System.out.println("AddNewProvConfig : clickTomorrowDay : if operation is done : " + done);
        return done;
    }

    public boolean clickTomorrowDayPlus1() throws InterruptedException
    {
        boolean done = false;
        int itemNumber = 100;
        List<WebElement> items = calendar.findElements(By.xpath("//td[@data-handler='selectDay']"));
        Thread.sleep(1_000);
        System.out.println("clickTomorrowDayPlus1 : items.size() is : " + items.size());
        for(int i=0; i < items.size(); i++)
        {
            String selected = items.get(i).getAttribute("class");
            if (selected.contains("ui-datepicker-today"))
            {
                itemNumber = i;
                System.out.println("clickTomorrowDayPlus1 : detected day is : " + items.get(i).getText());
                System.out.println("clickTomorrowDayPlus1 : detected day is : " + items.get(i).findElement(By.xpath("//td/a[@href='#']")).getAttribute("outerHTML").toString());
                System.out.println("clickTomorrowDayPlus1 : detected day is : " + items.get(i).getAttribute("class").toString());
            }

        }
        Thread.sleep(1_000);
        if (itemNumber < items.size() - 2)
        {
            itemNumber++; itemNumber++; items.get(itemNumber).click(); done = true;
        }
        else
        {
            //nextMonthTriangle.click();
            List<WebElement> Titems = calendar.findElements(By.xpath("//span[@class='ui-icon ui-icon-circle-triangle-e']"));
            System.out.println("Titems.size(): " + Titems.size());
            Titems.get(0).click();
            Thread.sleep(1_000);
            theFirstDateButton.click();
            done = true;
        }
        Thread.sleep(1_000);
        System.out.println("AddNewProvConfig : clickTomorrowDayPlus1 : if operation is done : " + done);
        return done;
    }

    public boolean clickYesterday() throws InterruptedException
    {
        boolean done = false;
        int itemNumber = 100;
        List<WebElement> items = calendar.findElements(By.xpath("//td[@data-handler='selectDay']"));
        Thread.sleep(1_000);
        System.out.println("AddNewProvConfig : items.size() is : " + items.size());
        for(int i=0; i < items.size(); i++)
        {
            String selected = items.get(i).getAttribute("class");
            if (selected.contains("ui-datepicker-today"))
            {
                itemNumber = i;
                System.out.println("AddNewProvConfig : detected day is : " + items.get(i).getText());
                System.out.println("AddNewProvConfig : detected day is : " + items.get(i).findElement(By.xpath("//td/a[@href='#']")).getAttribute("outerHTML").toString());
                System.out.println("AddNewProvConfig : detected day is : " + items.get(i).getAttribute("class").toString());
            }

        }
        Thread.sleep(1_000);
        if (itemNumber > 1)
        {
            itemNumber--; items.get(itemNumber).click(); done = true;
        }
        else
        {
            //previosMonthTriangle.click();
            List<WebElement> Titems = calendar.findElements(By.xpath("//span[@class='ui-icon ui-icon-circle-triangle-w']"));
            System.out.println("Titems.size(): " + Titems.size());
            Titems.get(0).click();
            Thread.sleep(1_000);
            theFirstDateButton.click();
            done = true;
        }
        Thread.sleep(1_000);
        System.out.println("AddNewProvConfig : clickYesterday : if operation is done : " + done);
        return done;
    }

    public void clickNextMonthFirstDay() throws InterruptedException
    {

        List<WebElement> Titems = calendar.findElements(By.xpath("//span[@class='ui-icon ui-icon-circle-triangle-e']"));
        System.out.println("Titems.size(): " + Titems.size());
        Titems.get(0).click();
        Thread.sleep(1_000);
        theFirstDateButton.click();
        Thread.sleep(1_000);
        System.out.println("AddNewProvConfig : clickNextMonthFirstDay() : the first day is set");

    }
}
