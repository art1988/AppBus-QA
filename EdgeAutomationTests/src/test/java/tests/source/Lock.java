package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.LockPage;
import com.appbus.pages.constants.Const;
import org.junit.Assert;
import org.junit.Test;

public class Lock
{
    /**
     * Simple lock test
     */
    @Test
    public void lock()
    {
        ActiveHamburgerMenu activeSidebarMenu = new ActiveHamburgerMenu(FunctionalTest.getDriver());

        LockPage lockPage = activeSidebarMenu.clickLock();

        System.out.println("Trying to login with wrong password...");

        String wrongPass = "WrongPass321";

        lockPage.setPassword(wrongPass);
        ActiveHamburgerMenu menu = lockPage.clickUnlcok();

        Assert.assertEquals(null, menu);

        System.out.println("Trying to login with correct password...");

        lockPage.setPassword(Const.PASSWORD);
        menu = lockPage.clickUnlcok();
    }
}
