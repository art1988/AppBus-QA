package tests.source;

import net.portal.constants.Const;
import net.portal.pages.LoginPage;
import org.junit.Test;

public class Login
{
    @Test
    public void login() throws InterruptedException
    {
        LoginPage loginPage = new LoginPage(FunctionalTest.getDriver());

        loginPage.enterUserName(Const.USER_EDAPT);
        loginPage.enterPassword(Const.PASSWORD);

        System.out.println("[Revision]: \n" + loginPage.getRevision());
        loginPage.clickLogin();
    }
}
