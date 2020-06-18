package tests.source.web_driver_setup;

import io.restassured.RestAssured;
import net.portal.constants.Const;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import tests.source.FunctionalTest;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;

public class ChromeWindowedExternalStageSetup extends FunctionalTest
{
    @BeforeClass
    public static void setup() throws IOException
    {
        System.out.println("! Chrome Windowed External Stage Setup...");

        Map<String, Object> prefs = new HashMap<String, Object>();

        // preference for Chrome to download without prompt
        prefs.put("profile.default_content_setting_values.automatic_downloads", 1);

        //prefs.put("profile.default_content_settings.popups", 0);
        //prefs.put("download.prompt_for_download", "true");
        prefs.put("safebrowsing.enabled", "true");
        prefs.put("download.default_directory", Const.DOWNLOAD_FOLDER);

        ChromeOptions options = new ChromeOptions();

        //options.add_argument("--safebrowsing-disable-download-protection")
        //options.add_argument("--safebrowsing-disable-extension-blacklist")

        options.addArguments("--disable-extensions");
        options.addArguments("--start-maximized");
        options.addArguments("--safebrowsing-disable-download-protection");
        options.addArguments("--safebrowsing-disable-extension-blacklist");
        options.setExperimentalOption("prefs", prefs);

        System.setProperty("webdriver.chrome.driver", Const.CHROME_DRIVER_PATH);

        driver = new ChromeDriver(options);
        driver.manage().timeouts().implicitlyWait(15, TimeUnit.SECONDS); // timeout for all elements

        driver.get(Const.STAGE_EXTERNAL_LOGIN_PAGE);

        // Set base uri for stage for SchedulerTests
        RestAssured.baseURI = Const.BASE_URI_STAGE;

        return;
    }

    @AfterClass
    public static void end()
    {
        driver.quit();
    }
}
