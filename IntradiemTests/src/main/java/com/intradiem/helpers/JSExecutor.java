package com.intradiem.helpers;

import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;

public class JSExecutor
{
    public static void injectJQuery(WebDriver driver)
    {
        StringBuffer jsCode = new StringBuffer("var addscript = window.document.createElement('script'); ");
        jsCode.append("addscript.type = 'text/javascript'; ");
        jsCode.append("addscript.src = 'https://code.jquery.com/jquery-3.3.1.min.js'; ");
        jsCode.append("document.body.appendChild(addscript); ");

        ((JavascriptExecutor) driver).executeScript(jsCode.toString());

        try
        {
            Thread.sleep(5_000); // Wait until file is download
        }
        catch (InterruptedException e)
        {
            e.printStackTrace();
        }

        System.out.println("JQuery was injected.");
    }
}
