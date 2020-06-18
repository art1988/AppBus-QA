package com.appbus.pages;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import org.openqa.selenium.support.PageFactory;

import java.time.Duration;

// Root class for all page objects
public class PageObject
{
    protected AppiumDriver driver;


    public PageObject(AppiumDriver driver)
    {
        this.driver = driver;

        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(10)), this);
    }
}
