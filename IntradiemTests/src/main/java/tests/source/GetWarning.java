package tests.source;

import io.appium.java_client.AppiumDriver;
import io.appium.java_client.windows.WindowsDriver;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.net.URL;
import java.util.concurrent.TimeUnit;

public class GetWarning
{
    @Test
    public void getIntradiemWarning() throws InterruptedException
    {
        AppiumDriver driver = null;

        try
        {
            DesiredCapabilities capabilities = new DesiredCapabilities();

            capabilities.setCapability("app", "C:\\ProgramData\\AppBus\\AppBus\\AppBus.exe");
            capabilities.setCapability("appArguments", "proxy \"C:\\Program Files (x86)\\Intradiem\\Intradiem Desktop Experience\\IntradiemDesktopExperience.exe\"");
            capabilities.setCapability("platformName", "Windows");
            capabilities.setCapability("deviceName", "C:\\ProgramData\\AppBus\\AppBus\\AppBus.exe");
            capabilities.setCapability("appWorkingDir", "C:\\ProgramData\\AppBus\\AppBus");

            driver = new WindowsDriver(new URL("http://127.0.0.1:4723/wd/hub"), capabilities);

            driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        }
        catch(Exception e)
        {

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

        Thread.sleep(15000);

        WebElement warningWindow = desktopSession.findElement(By.name("Warning"));

        Assert.assertNotNull(warningWindow);

        WebElement warnText = desktopSession.findElement(By.name("It appears the host site is not responding. Please contact your system administrator."));

        Assert.assertEquals("It appears the host site is not responding. Please contact your system administrator.", warnText.getText());

        Thread.sleep(2000);

        // Click by icon in task bar
        // AutomationId:	"{7C5A40EF-A0FB-4BFC-874A-C0F2E0B9FA8E}\Intradiem\Intradiem Desktop Experience\IntradiemDesktopExperience.exe"
        WebElement iconInTaskBar = desktopSession.findElementByAccessibilityId("{7C5A40EF-A0FB-4BFC-874A-C0F2E0B9FA8E}\\Intradiem\\Intradiem Desktop Experience\\IntradiemDesktopExperience.exe");
        iconInTaskBar.click();

        Thread.sleep(1000);

        // Click OK to close warning window
        WebElement okButton = desktopSession.findElement(By.name("OK Enter"));
        okButton.click();

        Thread.sleep(1000);

        desktopSession.quit();
    }
}
