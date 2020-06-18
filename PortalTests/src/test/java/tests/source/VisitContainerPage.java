package tests.source;

import net.portal.pages.HeaderMenu;
import net.portal.pages.audit.Container;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

public class VisitContainerPage
{
    @Test
    public void visitContainerPage() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());
        Container containerPage = headerMenu.clickContainer();

        System.out.println("Make sure that we see 'Time interval:' label and table...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('.ui-toolbar-group-left').text().startsWith('Time interval:')"));
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#dataTableForm\\\\:logsTable').is(':visible')"));

        containerPage.setStartFilterDate("05/20/2019 12:22");
        containerPage.setEndFilterDate("05/22/2019 16:10");

        containerPage.filterByUser("qadev");
        containerPage.clickApply();

        Thread.sleep(4_000);

        System.out.println("Making sure that filter by username works...");
        Assert.assertTrue((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#dataTableForm\\\\:logsTable_data td:nth-child(4)').toArray().every(function (node) { return node.textContent === 'qadev' })"));
        Assert.assertEquals("6", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#dataTableForm\\\\:logsTable_data tr').length")));

        containerPage.clickReset();

        Thread.sleep(4_000);

        Assert.assertFalse((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#dataTableForm\\\\:logsTable_data td:nth-child(4)').toArray().every(function (node) { return node.textContent === 'qadev' })"));
    }
}
