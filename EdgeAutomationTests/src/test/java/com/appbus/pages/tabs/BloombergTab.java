package com.appbus.pages.tabs;

import com.appbus.pages.constants.Const;
import com.appbus.pages.constants.Context;
import com.appbus.pages.helpers.JSExecutor;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import tests.source.FunctionalTest;

public class BloombergTab
{
    public BloombergTab()
    {
        Assert.assertTrue( isInit() );
    }

    private boolean isInit()
    {
        try
        {
            Thread.sleep(5_000); // necessary timeout to fetch all available webviews
        } catch (InterruptedException e)
        {
            e.printStackTrace();
        }

        FunctionalTest.switchContextToWebViewByURL(Const.BLOOMBERG_WEBVIEW_URL);

        JSExecutor.injectJQuery();

        return ( JSExecutor.isVisibleViaJQuery("$('.navi-bar__logo--title')") &
                 JSExecutor.isVisibleViaJQuery("$('.navi-bar__button.navi-bar__button--menu')") );
    }


    public void visitSurveillancePage() throws InterruptedException
    {
        FunctionalTest.getDriver().executeScript("window.location.href = 'https://www.bloomberg.com/series/bloomberg-surveillance';");
        System.out.println("URL was changed to Surveillance...");

        FunctionalTest.switchContext(Context.NATIVE);

        System.out.println("Wait up to 50 sec. until Bloomberg Surveillance label is visible...");
        MobileElement bloombergSurveillanceLabel = (MobileElement) (new WebDriverWait(FunctionalTest.getDriver(), 50)).until(ExpectedConditions.visibilityOfElementLocated(By.name("Bloomberg Surveillance")));

        FunctionalTest.switchContextToWebViewByURL(Const.BLOOMBERG_WEBVIEW_URL);
    }
}
