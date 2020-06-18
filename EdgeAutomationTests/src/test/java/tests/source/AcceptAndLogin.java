package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.LoginPage;
import com.appbus.pages.constants.Const;
import io.appium.java_client.MobileElement;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class AcceptAndLogin
{

    @Test
    public void acceptAndLogin()
    {
        MobileElement accept = (MobileElement)(new WebDriverWait(FunctionalTest.getDriver(), 5)).until(ExpectedConditions.presenceOfElementLocated(By.name("Accept")));

        accept.click();

        LoginPage loginPage = new LoginPage(FunctionalTest.getDriver());

        loginPage.enterUser(Const.LOGIN);
        loginPage.enterPassword(Const.PASSWORD);
        loginPage.enterDomain(Const.DOMAIN);
        loginPage.enterTfa(Const.TFA);

        ActiveHamburgerMenu mainPage = loginPage.logon();
    }
}
