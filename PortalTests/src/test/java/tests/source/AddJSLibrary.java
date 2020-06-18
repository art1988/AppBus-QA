package tests.source;

import net.portal.constants.Const;
import net.portal.pages.HeaderMenu;
import net.portal.pages.service_management.ServiceCatalog;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.*;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.interactions.Actions;

import java.awt.*;
import java.awt.event.InputEvent;
import java.util.Set;
import java.util.WeakHashMap;

import static java.sql.DriverManager.println;
import static tests.source.FunctionalTest.driver;

public class AddJSLibrary
{
    @Test
    public void jsLibraryCheck() throws InterruptedException
    {
        System.out.println("--------- START OF AddJSLibrary ---------");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        ServiceCatalog serviceCatalogPage = headerMenu.clickServiceCatalog();
        Thread.sleep(6_000);

        serviceCatalogPage.selectProject("AT Proj 5");
        Thread.sleep(5_000);

        serviceCatalogPage.selectJSLibraries();
        Thread.sleep(5_000);

        serviceCatalogPage.clickCreateJSLibrary();

        Thread.sleep(10_000);

        serviceCatalogPage.setName("ex_1", "jsLibsEditor");
        serviceCatalogPage.setCode("_var h='Hello !'", "jsLibsEditor"); // expect error for this code

        serviceCatalogPage.clickTest();
        Thread.sleep(5_000);

        // Check the visibility of error icon in Ace editor...
        Assert.assertTrue( (boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $($('[id=\"jsLibsEditor\"]')[0].contentDocument).find(\".ace_gutter-cell.ace_error\").is(':visible')"));

        serviceCatalogPage.setName("ex_2", "jsLibsEditor");
        serviceCatalogPage.setCode("var h='Hello !'", "jsLibsEditor"); // correct code

        serviceCatalogPage.clickTest();
        Thread.sleep(2_000);

        // There should be no error icon in Ace editor...
        Assert.assertFalse( (boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $($('[id=\"jsLibsEditor\"]')[0].contentDocument).find(\".ace_gutter-cell.ace_error\").is(':visible')"));

        serviceCatalogPage.clickSave("jsLibsEditor");
        Thread.sleep(1_000);

        serviceCatalogPage.clickCloseEditor();
        Thread.sleep(5_000);

        serviceCatalogPage.editJSLibrary("ex_2");

        Assert.assertEquals("var h='Hello !'", serviceCatalogPage.getCode("jsLibsEditor"));

        WebElement iFrame = driver.findElement(By.id("jsLibsEditor"));
        //String wDimension = iFrame.getAttribute("Dimension");
        Dimension fPosition = iFrame.getSize();
        int w1Before = fPosition.getWidth();
        int h1Before = fPosition.getHeight();
        System.out.println("fPosition is : " + fPosition);
        Dimension wPosition = driver.manage().window().getSize();
        System.out.println(wPosition);


        serviceCatalogPage.clickDownload();
        Thread.sleep(3_000);

        //Click Save on bottom alert (start)

        Dimension fPosAfter = iFrame.getSize();
        int w1After = fPosAfter.getWidth();
        int h1After = fPosAfter.getHeight();
        System.out.println("fPosAfter is : " + fPosAfter);
        Dimension wPosAfter = driver.manage().window().getSize();
        System.out.println(wPosAfter);

        //Thread.sleep(1_000);
        //Set<String> winHandles = driver.getWindowHandles();
        //Thread.sleep(1_000);
        //String winHandle1 = winHandles.iterator().next();

        java.awt.Dimension sSize = Toolkit.getDefaultToolkit().getScreenSize();
        System.out.println("sSize : " + sSize);
        try {
            Robot bot = new Robot();
            int y = (int) sSize.getHeight() - h1Before + h1After - 24;
            System.out.println("y : " + y);
            System.out.println("h1After + (h1Before - h1After)/2 + 285 : " + (h1After + (h1Before - h1After)/2 + 285));
            bot.mouseMove(350, y); // x: 350, y: 955

            bot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
            bot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
        } catch (Exception e) {}

        //Click Save on bottom alert (end)

        serviceCatalogPage.clickUploadSourceCode(Const.JS_FILE_SAMPLE);
        Thread.sleep(3_000);



        String libraryName = "Upload_from_file";
        serviceCatalogPage.setName(libraryName, "jsLibsEditor");
        serviceCatalogPage.clickSave("jsLibsEditor");
        Thread.sleep(1_000);

        serviceCatalogPage.clickCloseEditor();
        Thread.sleep(5_000);

        serviceCatalogPage.editJSLibrary(libraryName);

        Assert.assertTrue(serviceCatalogPage.getCode("jsLibsEditor").startsWith("<!DOCTYPE html>"));

        serviceCatalogPage.clickAPIInformationTab();

        serviceCatalogPage.setDescription("Autotest JSLib description");

        serviceCatalogPage.clickEditTab();
        Thread.sleep(2_000);

        serviceCatalogPage.clickSave("jsLibsEditor");

        serviceCatalogPage.clickCloseEditor();
        Thread.sleep(5_000);

        System.out.println("--------- END OF AddJSLibrary ---------");
    }
}
