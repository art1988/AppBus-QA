package tests.source;

import com.intradiem.constants.Const;
import com.intradiem.helpers.JSExecutor;
import com.intradiem.helpers.Saver;
import com.intradiem.pages.AdminLoginPage;
import com.intradiem.pages.UsersPage;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.Alert;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class IntradiemMessageSender
{
    private WebDriver chromeDriver;

    @Before
    public void setup() throws InterruptedException
    {
        Thread.sleep(60_000); // Wait until IntradiemClientListener is fully loaded and logged in

        ChromeOptions options = new ChromeOptions();

        System.setProperty("webdriver.chrome.driver", Const.CHROME_DRIVER_PATH);

        chromeDriver = new ChromeDriver(options);

        chromeDriver.get(Const.URL_ADMIN);
    }

    @Test
    public void intradiemMessageSender() throws InterruptedException
    {
        AdminLoginPage adminLoginPage = new AdminLoginPage(chromeDriver);

        adminLoginPage.setUsername(Const.INTRADIEM_ADMIN_USERNAME);
        adminLoginPage.setPassword(Const.INTRADIEM_ADMIN_PASSWORD);

        UsersPage usersPage = adminLoginPage.logon();

        // Click OK button of browser popup
        Alert alert = chromeDriver.switchTo().alert();
        alert.accept();

        Thread.sleep(4_000);

        JSExecutor.injectJQuery(chromeDriver);

        usersPage.selectCheckBoxNearUser(Const.INTRADIEM_CLIENT_USERNAME);

        Thread.sleep(2_000);

        while( Saver.getDesirableMessages().isEmpty() == false )
        {
            usersPage.sendMessage("Subject", Saver.getDesirableMessages().remove()); // Subject is always the same
            Thread.sleep(17_000);
        }

        Thread.sleep(2_000);
    }

    @After
    public void end()
    {
        chromeDriver.quit();
    }
}
