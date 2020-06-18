package tests.source;

import net.portal.pages.HeaderMenu;
import net.portal.pages.reporting.UserDetails;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

public class VisitUserDetails
{
    @Test
    public void visitUserDetails() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        UserDetails userDetailPage = headerMenu.clickUserDetails();

        userDetailPage.setUser("qadev");
        userDetailPage.setStartFilterDate("02/01/2019 00:00");
        userDetailPage.setEndFilterDate("06/27/2019 23:59");

        userDetailPage.clickApplyButton();
        Thread.sleep(2_000);

        Assert.assertEquals("5", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#dataTableForm\\\\:dataTable_data tr').length")));
    }
}
