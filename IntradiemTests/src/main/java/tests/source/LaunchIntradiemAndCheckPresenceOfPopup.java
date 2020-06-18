package tests.source;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.windows.WindowsDriver;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.IOException;
import java.net.URL;

/**
 * Some tests are required launch of Intradiem client and checking presence of pop up at startup with message:
 * "The API is not responding. Please contact your system administrator."
 */
public class LaunchIntradiemAndCheckPresenceOfPopup
{
    private AppiumDriver driver;


    @Test
    public void launchIntradiemAndCheckPresenceOfPopup() throws InterruptedException, IOException
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


        // Looking for Intradiem main window
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

        // Looking for Api... pop up
        WebElement popup = new WebDriverWait(driver, 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.name("The API ...")));
        Assert.assertNotNull(popup);

        popup.click(); // Set focus on pop up
        // Click OK
        popup.sendKeys(Keys.TAB);
        popup.sendKeys(Keys.RETURN);

        Thread.sleep(2_000);

        // Kill Intradiem process... (since cannot locate Quit button via inspector)
        Runtime.getRuntime().exec("taskkill /f /im Intra*");

        System.out.println("Intradiem process was killed");

        driver.quit();
        Thread.sleep(5_000);
    }
}
