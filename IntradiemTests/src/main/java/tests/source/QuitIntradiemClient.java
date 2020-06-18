package tests.source;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.windows.WindowsDriver;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.awt.*;
import java.awt.event.InputEvent;
import java.net.URL;

public class QuitIntradiemClient
{
    @Test
    public void quitIntradiemClient() throws InterruptedException
    {
        AppiumDriver desktopSession = null;

        try
        {
            // Creating a Desktop session
            DesiredCapabilities desktopCapabilities = new DesiredCapabilities();

            desktopCapabilities.setCapability("platformName", "Windows");
            desktopCapabilities.setCapability("app", "Root");
            desktopCapabilities.setCapability("deviceName", "WindowsPC");

            desktopSession = new WindowsDriver(new URL("http://127.0.0.1:4723/wd/hub"), desktopCapabilities);
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }

        // Click chevron (^) icon to show hidden icons in tray
        WebElement chevronIcon = desktopSession.findElementByAccessibilityId("1502");
        chevronIcon.click();

        // Move mouse over Intradiem icon in tray
        WebElement intradiemIconInTray = desktopSession.findElement(By.name("Intradiem"));
        new Actions(desktopSession).moveToElement(intradiemIconInTray).perform();

        // Right mouse button click on Intradiem icon in tray
        new Actions(desktopSession).contextClick(intradiemIconInTray).perform();

        Thread.sleep(1_000);

        Point p = MouseInfo.getPointerInfo().getLocation();

        try
        {
            Robot robot = new Robot();

            robot.mouseMove((int)(p.getX() + 10), (int)(p.getY() + 10)); // Place cursor over Quit context menu

            Thread.sleep(2_000);

            robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
            robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
        }
        catch (AWTException e)
        {
            e.printStackTrace();
        }

        IntradiemClientListener.getDriver().quit(); // Shut down driver

        System.out.println("IntradiemClientListener.getDriver().quit()");
        Thread.sleep(5_000); // Necessary timeout to launch new client and to make sure that new logs will not appear
    }
}
