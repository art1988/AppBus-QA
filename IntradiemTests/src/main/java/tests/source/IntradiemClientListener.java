package tests.source;


import com.intradiem.MessageListener;
import com.intradiem.constants.Const;
import com.intradiem.helpers.Saver;
import com.intradiem.pages.ClientLoginWindow;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.windows.WindowsDriver;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.net.URL;

public class IntradiemClientListener
{
    private static AppiumDriver driver;
    private static boolean doNotStartMessageListener; // flag to indicate do not start MessageListener thread
    private static boolean oauthPopup; // flag to indicate that 'Username or Password is invalid' pop up will appear
    private static boolean apiErrorPopup; // flag to indicate that 'The API is not responding or an API error has occurred. Please contact your system administrator.' pop up will appear

    public static void doNotStartMessageListener()
    {
        doNotStartMessageListener = true;
        System.out.println("doNotStartMessageListener = true");
    }

    public static void setOAuthPopupOn()
    {
        oauthPopup = true;
        System.out.println("oauthPopup = true");
    }

    public static void setApiErrorPopup()
    {
        apiErrorPopup = true;
        System.out.println("apiErrorPopup = true");
    }

    @Before
    public void setup() throws InterruptedException
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

            //driver.manage().timeouts().implicitlyWait(20, TimeUnit.SECONDS);
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
    }

    @Test
    public void intradiemClientListener() throws InterruptedException
    {
        ClientLoginWindow intradiemLoginWindow = new ClientLoginWindow(driver);

        intradiemLoginWindow.setUsername(Const.INTRADIEM_CLIENT_USERNAME);
        intradiemLoginWindow.setPassword(Const.INTRADIEM_CLIENT_PASSWORD);

        intradiemLoginWindow.clickLogin();

        if( oauthPopup == true || apiErrorPopup == true )
        {
            assertPopup();

            return;
        }
        else if( doNotStartMessageListener == true )
        {
            doNotStartMessageListener = false;
            return;
        }
        else
        {
            MessageListener messageListener = new MessageListener(Saver.getDesirableMessages());
            messageListener.start(); // start MessageListener thread
            messageListener.join(); // wait until MessageListener thread is finished...
        }
    }

    public static AppiumDriver getDriver()
    {
        return driver;
    }

    private void assertPopup()
    {
        WebElement popup = null;

        // Check presence of popup after clicking of LOGIN  button
        if( oauthPopup == true )
        {
            // Get pop up 'Username or Password is invalid'
            popup = new WebDriverWait(driver, 10_000).until(ExpectedConditions.visibilityOfElementLocated(By.name("Username or ...")));
            oauthPopup = false; // set default value back
        }

        if( apiErrorPopup == true )
        {
            // Get pop up 'The API is not responding or an API error has occurred. Please contact your system administrator.'
            popup = new WebDriverWait(driver, 10_000).until(ExpectedConditions.visibilityOfElementLocated(By.name("The API ...")));
            apiErrorPopup = false; // set default value back
        }

        Assert.assertNotNull(popup);
        popup.click(); // set focus on popup

        // Click OK
        popup.sendKeys(Keys.TAB);
        popup.sendKeys(Keys.RETURN);

        WebElement quitButton = new WebDriverWait(driver, 10_000).until(ExpectedConditions.visibilityOfElementLocated(By.name("Quit")));
        quitButton.click();

        driver.quit();
    }
}
