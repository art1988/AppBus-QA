package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.constants.Context;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.helpers.Scroller;
import com.appbus.pages.menuItems.InternetMenuItems;
import com.appbus.pages.menuItems.ServiceNavBar;
import com.appbus.pages.tabs.FidelityTab;
import org.junit.Assert;
import org.junit.Test;

public class Home
{
    @Test
    public void home() throws InterruptedException
    {
        ServiceNavBar serviceNavBar = new ServiceNavBar(FunctionalTest.getDriver());

        ActiveHamburgerMenu activeHamburgerMenu = serviceNavBar.clickHamburgerMenu();

        InternetMenuItems internetMenuItems = activeHamburgerMenu.clickInternet();

        Scroller.scrollRight("Fidelity");

        FidelityTab fidelityTab = internetMenuItems.clickFidelity();

        Assert.assertEquals("https://www.fidelity.com/viewpoints/overview", FunctionalTest.getDriver().executeScript("return document.URL"));

        fidelityTab.visitCustomerService();

        JSExecutor.injectJQuery();

        Assert.assertTrue(FunctionalTest.getDriver().executeScript("return document.URL").toString().contains("fidelity.com/customer-service/overview"));
        Thread.sleep(4_000);
        Assert.assertEquals("Top tasks", FunctionalTest.getDriver().executeScript("return $('.scl-flexible-images-with-column--group-headline').children().text()"));

        FunctionalTest.switchContext(Context.NATIVE);
        Thread.sleep(4_000);

        serviceNavBar.clickAction().clickHome();
        Thread.sleep(5_000);

        fidelityTab = new FidelityTab();

        Assert.assertEquals("https://www.fidelity.com/viewpoints/overview", FunctionalTest.getDriver().executeScript("return document.URL"));

        FunctionalTest.switchContext(Context.NATIVE);
    }
}
