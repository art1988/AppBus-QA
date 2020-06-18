package tests.source;

import io.appium.java_client.MobileElement;
import io.appium.java_client.ios.IOSDriver;
import org.junit.*;
import org.openqa.selenium.By;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.html5.Location;


// Specific for iOS pre-setup
public class SetDeveloperModeAndLocation
{

    private static IOSDriver driver;

    @BeforeClass
    public static void setup() throws MalformedURLException
    {
        DesiredCapabilities cap = new DesiredCapabilities();

        cap.setCapability("platformName", "iOS");
        cap.setCapability("platformVersion", "10.3");
        cap.setCapability("deviceName", "iPad Air 2");
        cap.setCapability("app", "settings");
        cap.setCapability("realDeviceLogger", "/usr/local/lib/node_modules/deviceconsole");
        cap.setCapability("automationName", "XCUITest");

        driver = new IOSDriver(new URL("http://127.0.0.1:4723/wd/hub"), cap);
    }

    @Test
    public void setDeveloperMode()
    {
        MobileElement appBus = (MobileElement) driver.findElement(By.xpath("//XCUIElementTypeStaticText[@name='AppBus']"));
        appBus.click();

        MobileElement envLabel = (MobileElement) driver.findElement(By.xpath("//XCUIElementTypeStaticText[@name='Operating Environment']"));
        envLabel.click();

        MobileElement devOption = (MobileElement) driver.findElement(By.xpath("//XCUIElementTypeStaticText[@name='Development']"));
        devOption.click();
    }

    @Test
    public void setLocation()
    {
        driver.setLocation(new Location(12, 33, 10));
    }

    @AfterClass
    public static void end() throws InterruptedException
    {
        driver.quit();
    }

}
