package com.appbus.pages.tabs;

import com.appbus.pages.constants.Const;
import com.appbus.pages.constants.Context;
import com.appbus.pages.helpers.JSExecutor;
import org.junit.Assert;
import tests.source.FunctionalTest;

public class ChartsTab
{
    /*
     * Non-native elements
     */
    private static String id_ChartImage      = "UpperChartContainer",
                          id_SaveChartButton = "saveChartBtn";


    public ChartsTab()
    {
        Assert.assertTrue( isInit() );

        FunctionalTest.switchContext(Context.NATIVE);
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

        FunctionalTest.switchContextToWebViewByURL(Const.UBS_WEBVIEW_URL);

        JSExecutor.injectJQuery();

        return ( isChartVisible() & isSaveChartButtonVisible() );
    }

    private boolean isChartVisible()
    {
        boolean isChartVisible = JSExecutor.isVisibleViaJQuery("$('#" + id_ChartImage + "')");

        System.out.println("isChartVisible = " + isChartVisible);

        return isChartVisible;
    }

    private boolean isSaveChartButtonVisible()
    {
        boolean isSaveChartButtonVisible = JSExecutor.isVisibleViaJQuery("$('#" + id_SaveChartButton + "')");

        System.out.println("isSaveChartButtonVisible = " + isSaveChartButtonVisible);

        return isSaveChartButtonVisible;
    }
}
