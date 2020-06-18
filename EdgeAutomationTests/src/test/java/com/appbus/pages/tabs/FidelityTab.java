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

public class FidelityTab
{
    public FidelityTab()
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

        FunctionalTest.switchContextToWebViewByURL(Const.FIDELITY_WEBVIEW_URL);

        JSExecutor.injectJQuery();

        return ( JSExecutor.isVisibleViaJQuery("$('.pnld')") &
                 JSExecutor.isVisibleViaJQuery("$('#dropdown-526-75718')") );
    }

    public void visitCustomerService()
    {
        FunctionalTest.getDriver().executeScript("window.location.href = 'https://www.fidelity.com/customer-service/overview';");
        System.out.println("URL was changed to Customer Service...");

        FunctionalTest.switchContext(Context.NATIVE);

        System.out.println("Wait up to 50 sec. until Customer service label is visible...");
        MobileElement customerServiceLabel = (MobileElement) (new WebDriverWait(FunctionalTest.getDriver(), 50)).until(ExpectedConditions.visibilityOfElementLocated(By.name("Customer service")));

        FunctionalTest.switchContextToWebViewByURL("https://www.fidelity.com/customer-service/overview");
    }
}
