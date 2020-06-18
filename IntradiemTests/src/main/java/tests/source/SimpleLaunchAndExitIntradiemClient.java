package tests.source;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.windows.WindowsDriver;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.io.IOException;
import java.net.URL;

/**
 * Some tests are required just simple launch and exit actions to check presence/absence of rule in log file
 */
public class SimpleLaunchAndExitIntradiemClient
{
    private AppiumDriver driver;
    private static boolean killProcess; // flag to indicate to kill process (in case is Quit button is not available or Intradiem window is not displayed)


    public static void forceQuitByKillingProcess()
    {
        killProcess = true;
        System.out.println("forceQuitByKillingProcess = true");
    }

    @Test
    public void simpleRunAndQuitIntradiemClient() throws InterruptedException, IOException
    {
        try
        {
            DesiredCapabilities capabilities = new DesiredCapabilities();

            capabilities.setCapability("app", "C:\\ProgramData\\AppBus\\AppBus\\AppBus.exe");
            capabilities.setCapability("appArguments", "proxy \"C:\\Program Files (x86)\\Intradiem\\Intradiem Desktop Experience\\IntradiemDesktopExperience.exe\"");
            capabilities.setCapability("platformName", "Windows");
            capabilities.setCapability("deviceName", "C:\\ProgramData\\AppBus\\AppBus\\AppBus.exe");
            capabilities.setCapability("appWorkingDir", "C:\\ProgramData\\AppBus\\AppBus");

            driver = new WindowsDriver(new URL("http://127.0.0.1:4723/wd/hub"), capabilities);
        }
        catch(Exception e)
        {
            System.out.println("waiting 15 sec...");
            Thread.sleep(15_000);
        }

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


        if( killProcess == true )
        {
            Runtime.getRuntime().exec("taskkill /f /im Intra*");

            System.out.println("Intradiem process was killed");

            desktopSession.quit();

            killProcess = false; // Set default value back

            Thread.sleep(5_000);
            return;
        }

        // Looking for Intradiem main window (in case if killProcess was set as false => window should appear)
        WebElement intradiemWindow = desktopSession.findElement(By.name("Intradiem"));
        Assert.assertNotNull(intradiemWindow);

        try
        {
            // Since Intradiem launches via AppBus, need to attach to existing Intradiem window
            String intradiemWindowHandle = intradiemWindow.getAttribute("NativeWindowHandle");
            intradiemWindowHandle = Integer.toHexString(Integer.parseInt(intradiemWindowHandle));

            DesiredCapabilities appCapabilities = new DesiredCapabilities();

            appCapabilities.setCapability("deviceName", "WindowsPC");
            appCapabilities.setCapability("appTopLevelWindow", intradiemWindowHandle);

            driver = new WindowsDriver(new URL("http://127.0.0.1:4723/wd/hub"), appCapabilities);
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }

        Thread.sleep(5_000); // sleep 5 sec and close window

        WebElement quitButton = driver.findElement(By.name("Quit"));
        quitButton.click();

        System.out.println("Quit button was clicked");

        driver.quit();

        Thread.sleep(5_000);
    }
}
