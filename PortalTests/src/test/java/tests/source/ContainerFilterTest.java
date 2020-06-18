package tests.source;

import net.portal.pages.HeaderMenu;
import net.portal.pages.audit.Container;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

public class ContainerFilterTest
{
    @Test
    public void containerFilterTest() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());
        Container containerPage = headerMenu.clickContainer();

        System.out.println("First, Reset filter...");
        containerPage.clickReset();
        Thread.sleep(3_000);

        Assert.assertEquals("Start DateFirst nameLast nameUserSession IDDevice TypeContextMessage",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#dataTableForm\\\\:logsTable_head th .ui-column-title').text()")));

        System.out.println("Hide the following columns: First name, Last name, Session ID and Context...");
        System.out.println("Show Type column...");
        containerPage.visibleColumns(new String[]{"First name", "Last name", "Session ID", "Type", "Context"});

        System.out.println("Assert the remaining columns...");
        Assert.assertEquals("Start DateUserTypeDevice TypeMessage",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#dataTableForm\\\\:logsTable_head th .ui-column-title').text()")));

        containerPage.setStartFilterDate("06/02/2019 16:13");
        containerPage.setEndFilterDate("06/03/2019 16:13");
        containerPage.setSeverity("WARN"); // Check WARN checkbox

        containerPage.clickApply();
        Thread.sleep(4_000);

        System.out.println("Checking that there are only 2 rows with WARN severity...");
        Assert.assertEquals("2", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#dataTableForm\\\\:logsTable_data tr').length")));

        containerPage.setSeverity("WARN"); // Uncheck WARN checkbox
        containerPage.setSeverity("ERROR"); // Check ERROR checkbox

        containerPage.clickApply();
        Thread.sleep(4_000);

        Assert.assertEquals("No records found.", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#dataTableForm\\\\:logsTable_data').text()")));

        System.out.println("Hide 'Start date' column and show 'Tags' column...");
        containerPage.visibleColumns(new String[]{"Start date", "Tags"});

        System.out.println("Assert the remaining columns...");
        Assert.assertEquals("UserTypeTagsDevice TypeMessage",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#dataTableForm\\\\:logsTable_head th .ui-column-title').text()")));

        // Final Reset
        containerPage.clickReset();
        Thread.sleep(4_000);

        Assert.assertEquals("Start DateFirst nameLast nameUserSession IDDevice TypeContextMessage",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#dataTableForm\\\\:logsTable_head th .ui-column-title').text()")));
    }
}
