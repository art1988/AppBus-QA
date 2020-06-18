package tests.source;

import com.appbus.pages.SearchScreen;
import com.appbus.pages.menuItems.ServiceNavBar;
import com.appbus.pages.tabs.ChartsTab;
import com.appbus.pages.tabs.ContactsTab;
import com.appbus.pages.tabs.DocumentsTab;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;

public class Search
{
    @Test
    public void search() throws InterruptedException
    {
        ServiceNavBar navBar = new ServiceNavBar(FunctionalTest.getDriver());

        // Re-login to reset previous selected tabs
        navBar.clickHamburgerMenu().clickLogout().logon();

        // Search by "Doc" name
        SearchScreen searchScreen = navBar.clickSearch();
        searchScreen.setSearchFiled("Doc");
        Thread.sleep(5000);

        MobileElement foundElement = (MobileElement) FunctionalTest.getDriver().findElement(By.xpath("(//XCUIElementTypeStaticText[@name='Documents'])[2]"));
        Assert.assertNotNull(foundElement);

        searchScreen.clickByFoundedElement(foundElement);
        Thread.sleep(8000);

        DocumentsTab documentsTab = new DocumentsTab(FunctionalTest.getDriver());
        Thread.sleep(2000);

        // Search by "Char" name
        searchScreen = navBar.clickSearch();
        searchScreen.setSearchFiled("Char");
        Thread.sleep(1000);

        foundElement = (MobileElement) FunctionalTest.getDriver().findElement(By.name("Charts"));
        Assert.assertNotNull(foundElement);

        searchScreen.clickByFoundedElement(foundElement);
        Thread.sleep(4000);

        ChartsTab chartsTab = new ChartsTab();
        Thread.sleep(1000);

        // Search by "Conta" name
        searchScreen = navBar.clickSearch();
        searchScreen.setSearchFiled("Conta");
        Thread.sleep(4000);

        foundElement = (MobileElement) FunctionalTest.getDriver().findElement(By.name("Contacts"));
        Assert.assertNotNull(foundElement);

        searchScreen.clickByFoundedElement(foundElement);
        Thread.sleep(4000);

        ContactsTab contactsTab = new ContactsTab(FunctionalTest.getDriver());

        // Search by "Acce" name
        searchScreen = navBar.clickSearch();
        searchScreen.setSearchFiled("Acce");
        Thread.sleep(1000);

        foundElement = (MobileElement) FunctionalTest.getDriver().findElement(By.name("Accenture Portal"));
        Assert.assertNotNull(foundElement);

        searchScreen.clickByFoundedElement(foundElement);
        Thread.sleep(4000);
    }
}
