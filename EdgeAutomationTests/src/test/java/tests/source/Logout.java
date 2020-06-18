package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.LoginPage;
import com.appbus.pages.constants.Const;
import com.appbus.pages.menuItems.ServiceNavBar;
import org.junit.Test;

public class Logout
{
    /**
     * Simple logout and relogin test
     */
    @Test
    public void logout()
    {
        ServiceNavBar serviceNavBar = new ServiceNavBar(FunctionalTest.getDriver());

        LoginPage loginPage = serviceNavBar.clickHamburgerMenu().clickLogout();

        loginPage.enterUser(Const.LOGIN);
        loginPage.enterPassword(Const.PASSWORD);
        loginPage.enterDomain(Const.DOMAIN);
        loginPage.enterTfa(Const.TFA);

        ActiveHamburgerMenu mainPage = loginPage.logon();
    }
}
