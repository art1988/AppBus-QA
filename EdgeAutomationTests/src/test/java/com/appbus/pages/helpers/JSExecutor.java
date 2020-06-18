package com.appbus.pages.helpers;

import tests.source.FunctionalTest;

public class JSExecutor
{
    /**
     * Execute JS code to find necessary element by id ( < input > or < textarea > filed ) and set value = text.
     * Works only in WEBVIEW context.
     * @param id
     * @param text
     * */
    public static void setTextForField(String id, String text)
    {
        /*
                var input = ...;
                var lastValue = input.value;

                input.focus();
                input.value = 'some value';

                var event = new Event('input', { bubbles: true });
                var tracker = input._valueTracker;

                if (tracker) {
                  tracker.setValue(lastValue);
                }

                input.dispatchEvent(event);
                input.blur();
         */

        StringBuffer jsCode = new StringBuffer("var input = document.getElementById('" + id + "'); ");
        jsCode.append("var lastValue = input.value; ");
        jsCode.append("input.focus(); ");
        jsCode.append("input.value = '" + text + "'; ");
        jsCode.append("var event = new Event('input', { bubbles: true }); ");
        jsCode.append("var tracker = input._valueTracker; ");
        jsCode.append("if (tracker) { tracker.setValue(lastValue); } ");
        jsCode.append("input.dispatchEvent(event); ");
        jsCode.append("input.blur(); ");

        FunctionalTest.getDriver().executeScript(jsCode.toString());
    }

    /**
     * Execute JS code to get text from ( < input > filed ) by id.
     * Works only in WEBVIEW context.
     * @param id
     * @return
     */
    public static String getTextFromFiled(String id)
    {
        return String.valueOf(FunctionalTest.getDriver().executeScript("return document.getElementById('" + id + "').value; "));
    }

    /**
     * Execute JS code to find necessary element by class ( < input > filed ) and set value = text.
     * Works only in WEBVIEW context.
     * @param className
     * @param text
     */
    public static void setTextForFieldByClassName(String className, String text)
    {
        StringBuffer jsCode = new StringBuffer("var input = document.getElementsByClassName('" + className + "')[0]; ");
        jsCode.append("var lastValue = input.value; ");
        jsCode.append("input.focus(); ");
        jsCode.append("input.value = '" + text + "'; ");
        jsCode.append("var event = new Event('input', { bubbles: true }); ");
        jsCode.append("var tracker = input._valueTracker; ");
        jsCode.append("if (tracker) { tracker.setValue(lastValue); } ");
        jsCode.append("input.dispatchEvent(event); ");
        jsCode.append("input.blur(); ");

        FunctionalTest.getDriver().executeScript(jsCode.toString());
    }

    /**
     * Execute JS code to find necessary element by id ( < select > filed ) and set value = text.
     * Works only in WEBVIEW context.
     * @param id
     * @param text
     */
    public static void setTextForSelect(String id, String text)
    {
        StringBuffer jsCode = new StringBuffer("var select = document.getElementById('" + id + "'); ");
        jsCode.append("var lastValue = select.value; ");
        jsCode.append("select.focus(); ");
        jsCode.append("select.value = '" + text + "'; ");
        jsCode.append("var event = new Event('change', { bubbles: true }); ");
        jsCode.append("var tracker = select._valueTracker; ");
        jsCode.append("if (tracker) { tracker.setValue(lastValue); } ");
        jsCode.append("select.dispatchEvent(event); ");
        jsCode.append("select.blur(); ");

        FunctionalTest.getDriver().executeScript(jsCode.toString());
    }

    /**
     * Execute JS code to find necessary element by class ( < select > filed ) and set value = text.
     * Works only in WEBVIEW context.
     * @param className
     * @param text
     */
    public static void setTextForSelectByClassName(String className, String text)
    {
        StringBuffer jsCode = new StringBuffer("var select = document.getElementsByClassName('" + className + "')[0]; ");
        jsCode.append("var lastValue = select.value; ");
        jsCode.append("select.focus(); ");
        jsCode.append("select.value = '" + text + "'; ");
        jsCode.append("var event = new Event('change', { bubbles: true }); ");
        jsCode.append("var tracker = select._valueTracker; ");
        jsCode.append("if (tracker) { tracker.setValue(lastValue); } ");
        jsCode.append("select.dispatchEvent(event); ");
        jsCode.append("select.blur();");

        FunctionalTest.getDriver().executeScript(jsCode.toString());
    }

    /**
     * Execute JS code: get value from < select > field by id.
     * Works only in WEBVIEW context.
     * @param id
     * @return
     */
    public static String getTextFromSelect(String id)
    {
        StringBuffer jsCode = new StringBuffer("var select = document.getElementById('" + id + "'); ");
        jsCode.append("return select.value; ");

        return String.valueOf(FunctionalTest.getDriver().executeScript(jsCode.toString()));
    }

    /**
     * Execute JS code: click by element by id.
     * Works only in WEBVIEW context.
     * @param id
     */
    public static void clickByElement(String id)
    {
        StringBuffer jsCode = new StringBuffer("var element = document.getElementById('" + id + "'); ");
        jsCode.append("element.click(); ");

        FunctionalTest.getDriver().executeScript(jsCode.toString());
    }

    /**
     * Execute JS code: click by element with index [0] by class.
     * Works only in WEBVIEW context.
     * @param className
     */
    public static void clickByElementByClassName(String className)
    {
        clickByElementByClassName(className, 0);
    }

    /**
     * Execute JS code: click by element with index [index] by class.
     * Works only in WEBVIEW context.
     * @param className
     * @param index
     */
    public static void clickByElementByClassName(String className, int index)
    {
        StringBuffer jsCode = new StringBuffer("var element = document.getElementsByClassName('" + className + "')" + "[" + index + "]; ");
        jsCode.append("element.click(); ");

        FunctionalTest.getDriver().executeScript(jsCode.toString());
    }

    /**
     * Execute JS code: get textContent from element by class name.
     * In case if element is undefined then returns 0.
     * Works only in WEBVIEW context.
     * @return textContent from element by class name. If element is undefined then returns 0.
     */
    public static String getTextByClassName(String className)
    {
        StringBuffer jsCode = new StringBuffer("var elements = document.getElementsByClassName('" + className + "'); ");
        jsCode.append("if(elements[0]) { return elements[0].textContent; } else { return 0; }");

        return String.valueOf(FunctionalTest.getDriver().executeScript(jsCode.toString()));
    }

    /**
     * Method to inject JQuery into DOM
     * Works only in WEBVIEW context.
     */
    public static void injectJQuery()
    {
        StringBuffer jsCode = new StringBuffer("var addscript = window.document.createElement('script'); ");
        jsCode.append("addscript.type = 'text/javascript'; ");
        jsCode.append("addscript.src = 'https://code.jquery.com/jquery-3.3.1.min.js'; ");
        jsCode.append("document.body.appendChild(addscript); ");

        FunctionalTest.getDriver().executeScript(jsCode.toString());

        try
        {
            Thread.sleep(5000); // Wait until file is download
        }
        catch (InterruptedException e)
        {
            e.printStackTrace();
        }

        System.out.println("JQuery was injected.");
    }

    /**
     * Click by element using JQuery
     * Works only in WEBVIEW context.
     * @param jqueryStatement
     */
    public static void clickViaJQuery(String jqueryStatement)
    {
        FunctionalTest.getDriver().executeScript(jqueryStatement + ".click()");
    }

    /**
     * Get text from element using JQuery
     * Works only in WEBVIEW context.
     * @param jqueryStatement
     * @return
     */
    public static String getTextViaJQuery(String jqueryStatement)
    {
        return String.valueOf(FunctionalTest.getDriver().executeScript("return " + jqueryStatement + ".text()"));
    }

    /**
     * Get text from < input > element using JQuery
     * Works only in WEBVIEW context.
     * @param jqueryStatement
     * @return
     */
    public static String getTextViaJQueryFromInput(String jqueryStatement)
    {
        return String.valueOf(FunctionalTest.getDriver().executeScript("return " + jqueryStatement + ".val()"));
    }

    /**
     * Check visibility property of element
     * Works only in WEBVIEW context.
     * @param jqueryStatement
     * @return
     */
    public static boolean isVisibleViaJQuery(String jqueryStatement)
    {
        if( String.valueOf(FunctionalTest.getDriver().executeScript("return " + jqueryStatement + ".is(':visible')")).equals("true") )
        {
            return true;
        }

        return false;
    }

}
