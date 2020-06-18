package tests.source.web_driver_setup;

import io.restassured.RestAssured;
import net.portal.constants.Const;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClientBuilder;
import org.json.simple.JSONObject;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeDriverService;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.remote.SessionId;
import tests.source.FunctionalTest;

import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeUnit;

public class ChromeHeadlessInternalQASetup extends FunctionalTest
{
    @BeforeClass
    public static void setup() throws IOException
    {
        // headless setup
        System.out.println("! Chrome headless internal QA setup...");

        ChromeDriverService chromeDriverSevice = new ChromeDriverService.Builder()
                .usingDriverExecutable(new File(Const.CHROME_DRIVER_PATH)).usingAnyFreePort()
                .build();
        chromeDriverSevice.start();

        Map<String, Object> prefs = new HashMap<String, Object>();

        ChromeOptions options = new ChromeOptions();

        //options.add_argument("--safebrowsing-disable-download-protection")
        //options.add_argument("--safebrowsing-disable-extension-blacklist")

        options.addArguments("--disable-extensions");
        options.addArguments("--headless");
        options.addArguments("--disable-gpu");
        options.addArguments("--safebrowsing-disable-download-protection");
        options.addArguments("--safebrowsing-disable-extension-blacklist");
        options.setExperimentalOption("prefs", prefs);

        driver = new ChromeDriver(chromeDriverSevice, options);
        Map<String, Object> commandParams = new HashMap<>();
        commandParams.put("cmd", "Page.setDownloadBehavior");
        Map<String, String> params = new HashMap<>();
        params.put("behavior", "allow");
        params.put("downloadPath", Const.DOWNLOAD_FOLDER);
        commandParams.put("params", params);
        JSONObject commandParamsObj = new JSONObject(commandParams);

        HttpClient httpClient = HttpClientBuilder.create().build();
        String payload = commandParamsObj.toString();

        SessionId session = ((ChromeDriver)driver).getSessionId();

        String u = chromeDriverSevice.getUrl().toString() + "/session/" + session + "/chromium/send_command";
        HttpPost request = new HttpPost(u);
        request.addHeader("content-type", "application/json");
        request.setEntity(new StringEntity(payload));
        httpClient.execute(request);

        driver.manage().timeouts().implicitlyWait(15, TimeUnit.SECONDS); // timeout for all elements

        driver.get(Const.QA_INTERNAL_LOGIN_PAGE);

        // Set base uri for qa for SchedulerTests
        RestAssured.baseURI = Const.BASE_URI_QA;

        return;


        // windowed setup
        /*
        System.out.println("! Chrome Windowed internal QA setup...");

        Map<String, Object> prefs = new HashMap<String, Object>();

        // preference for Chrome to download without prompt
        prefs.put("profile.default_content_setting_values.automatic_downloads", 1);

        //prefs.put("profile.default_content_settings.popups", 0);
        //prefs.put("download.prompt_for_download", "true");
        prefs.put("safebrowsing.enabled", "true");

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

        driver.get(Const.QA_INTERNAL_LOGIN_PAGE);

        // Set base uri for qa for SchedulerTests
        RestAssured.baseURI = Const.BASE_URI_QA;

        return;
        */
    }

    @AfterClass
    public static void end()
    {
        driver.quit();
    }
}
