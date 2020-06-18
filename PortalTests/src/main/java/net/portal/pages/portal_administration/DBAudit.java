package net.portal.pages.portal_administration;

import net.portal.forms.TableModificationDetails;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;

public class DBAudit extends PageObject
{
    public DBAudit(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Portal administration > DB Audit") );
    }

    /**
     * Get all values of Username column as single string
     * @return
     */
    public String getUsernameColumn()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#form\\\\:tableModificationsTable_data tr td:nth-child(2)').text()"));
    }

    public String getTypeColumn()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#form\\\\:tableModificationsTable_data tr td:nth-child(3)').text()"));
    }

    public String getObjectColumn()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#form\\\\:tableModificationsTable_data tr td:nth-child(4)').text()"));
    }

    public String getDateColumn()
    {
        return String.valueOf(((JavascriptExecutor) driver).executeScript("return $('#form\\\\:tableModificationsTable_data tr td:nth-child(5)').text()"));
    }

    /**
     * Click View button by rowNum
     * @param rowNum starts from 0 (first row)
     * @return
     */
    public TableModificationDetails clickView(int rowNum)
    {
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:tableModificationsTable_data tr td:nth-child(6)').find(\"button\").get(" + rowNum + ").click()");
        System.out.println("Row num " + rowNum + " was clicked");

        return new TableModificationDetails(driver);
    }
}
