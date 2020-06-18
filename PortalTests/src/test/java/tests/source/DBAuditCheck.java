package tests.source;

import net.portal.forms.TableModificationDetails;
import net.portal.pages.HeaderMenu;
import net.portal.pages.portal_administration.DBAudit;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

import java.text.SimpleDateFormat;
import java.util.Date;

public class DBAuditCheck
{
    // !!!
    // Note: this test implies that nobody interfere until this point i.e. only one user: edapt-setup did actions on portal.
    // In this case all requests should be in correct order.
    @Test
    public void dbAuditCheck() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        // Default page pagination is 50
        DBAudit dbAuditPage = headerMenu.clickDBAudit();

        System.out.println("Assert that username column has edapt-setup...");
        Assert.assertTrue(dbAuditPage.getUsernameColumn().startsWith("edapt-setupedapt-setupedapt-setupedapt-setupedapt-setupedapt-setupedapt"));

        System.out.println("Assert type column...");
        Assert.assertTrue(dbAuditPage.getTypeColumn().startsWith("DELETEDELETEUPDATECREATECREATEDELETEDELETECREATECREATEDELETE"));

        System.out.println("Assert object column...");
         Assert.assertTrue(dbAuditPage.getObjectColumn().startsWith("RoleRoleAssignmentRoleRoleAssignmentRoleRoleRole"));

        System.out.println("Assert date column...");
         Assert.assertTrue(dbAuditPage.getDateColumn().startsWith(new SimpleDateFormat("MM/dd/yyyy").format(new Date())));


        // Save values of the first fow
        String id = String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:tableModificationsTable_data tr td:nth-child(1)').find(\"span\").eq(0).text()")),
               username = String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:tableModificationsTable_data tr td:nth-child(2)').find(\"span\").eq(0).text()")),
               type = String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:tableModificationsTable_data tr td:nth-child(3)').find(\"span\").eq(0).text()")),
               object = String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:tableModificationsTable_data tr td:nth-child(4)').find(\"span\").eq(0).text()")),
               date = String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#form\\\\:tableModificationsTable_data tr td:nth-child(5)').eq(0).text()"));

        // Open first row
        TableModificationDetails tableModificationDetails_firstRow = dbAuditPage.clickView(0);
        Thread.sleep(1_000);

        Assert.assertEquals(id, tableModificationDetails_firstRow.getId());
        Assert.assertEquals(username, tableModificationDetails_firstRow.getUsername());
        Assert.assertEquals(type, tableModificationDetails_firstRow.getType());
        Assert.assertEquals(object, tableModificationDetails_firstRow.getObject());
        Assert.assertEquals(date, tableModificationDetails_firstRow.getDate());

        tableModificationDetails_firstRow.clickOk();

        Thread.sleep(2_000);
    }
}
