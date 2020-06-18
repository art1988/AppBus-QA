package com.appbus.pages;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class SearchScreen extends PageObject
{
    @FindBy(name = "globalSearch")
    private MobileElement searchFiled;


    public SearchScreen(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( searchFiled.isDisplayed() );
    }

    public void setSearchFiled(String textToSearch)
    {
        searchFiled.sendKeys(textToSearch);
    }

    public void clickByFoundedElement(MobileElement foundElement)
    {
        foundElement.click();
        System.out.println("Was clicked by element : " + foundElement.getText());
    }
}
