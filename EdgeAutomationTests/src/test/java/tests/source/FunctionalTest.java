package tests.source;

import com.appbus.pages.constants.Context;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.ios.IOSDriver;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.Set;
import java.util.concurrent.TimeUnit;
import java.util.stream.Collectors;

// Root class for suite
public class FunctionalTest
{
    protected static AppiumDriver driver;

    private static Context currentContext;


    public static AppiumDriver getDriver()
    {
        return driver;
    }

    public static Context getCurrentContext()
    {
        return currentContext;
    }

    /**
     * Switch context between native and webview (in case if there is only _ONE_ webview available)
     * @param contextName
     */
    public static void switchContext(Context contextName)
    {
        Set<String> availableContexts = driver.getContextHandles();
        availableContexts.stream()
                .filter(context -> context.contains(contextName.name()))
                .forEach(newcontext -> driver.context(newcontext));

        System.out.println("Context was switched to " + contextName);
        currentContext = contextName;
    }

    /**
     * Switch to only one WEBVIEW context based on URL (in case if there are _MANY_ webview's available)
     * @param specificURL
     */
    public static void switchContextToWebViewByURL(String specificURL)
    {
        Set<String> availableContexts = driver.getContextHandles();

        Set<String> onlyWebviews = availableContexts.stream()
                .filter(context -> context.contains(Context.WEBVIEW.name()))
                .collect(Collectors.toSet());

        for( String webview : onlyWebviews )
        {
            driver.context(webview);

            String url = String.valueOf(driver.executeScript("return document.URL;"));

            if( url.contains(specificURL) )
            {
                System.out.println("Context was switched to " + webview);
                currentContext = Context.WEBVIEW;

                return;
            }
        }

        System.err.println("Unable to find WEBVIEW context with URL = " + specificURL);
    }

    @BeforeClass
    public static void setup() throws MalformedURLException
    {
        // Get platform name from command line argument
        String platform = System.getProperty("platform");

        DesiredCapabilities cap = new DesiredCapabilities();

        switch (platform)
        {
            case "ios":
                cap.setCapability("platformName", "iOS");
                cap.setCapability("platformVersion", "11.2");
                cap.setCapability("deviceName", "iPad Air 2");
                cap.setCapability("app", "com.51-maps.edge");
                cap.setCapability("realDeviceLogger", "/usr/local/lib/node_modules/deviceconsole");
                cap.setCapability("automationName", "XCUITest");
                cap.setCapability("waitForQuiescence", "false");

                driver = new IOSDriver(new URL("http://127.0.0.1:4723/wd/hub"), cap);
                break;

            case "android":
                //TODO: add cap

                cap.setCapability("platformName", "Android");


                //driver = new AndroidDriver();
                break;
        }

        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);

        System.out.println("Func test: driver for platform " + platform + " was created");
    }

    @AfterClass
    public static void end()
    {
        driver.quit();
    }
}
