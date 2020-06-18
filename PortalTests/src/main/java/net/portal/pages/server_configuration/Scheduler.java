package net.portal.pages.server_configuration;

import net.portal.forms.AddJob;
import net.portal.forms.AddTrigger;
import net.portal.pages.DeleteJob;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Scheduler extends PageObject
{
    @FindBy(id = "schedulerForm:addJobButton")
    private WebElement addJobButton;

    @FindBy(id = "schedulerForm:refreshButton")
    private WebElement refreshButton;



    public Scheduler(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Server Configuration > Scheduler") );
    }

    public AddJob addJob()
    {
        addJobButton.click();
        System.out.println("Scheduler : Add job button was clicked");

        return new AddJob(driver);
    }

    public void clickRefresh()
    {
        refreshButton.click();
        System.out.println("Scheduler : Refresh button was clicked");
    }

    /**
     * Edit job by job name
     * @param jobName
     * @return
     */
    public AddJob editJob(String jobName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#schedulerForm\\\\:jobsTable_data tr td:contains(\"" + jobName + "\")').next().next().next().find(\"button\")[1].click()");
        System.out.println("Edit job: " + jobName);

        return new AddJob(driver);
    }

    /**
     * Add trigger for job by job name
     * @param jobName
     * @return
     */
    public AddTrigger addTrigger(String jobName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#schedulerForm\\\\:jobsTable_data tr td:contains(\"" + jobName + "\")').next().next().next().find(\"button\")[0].click()");
        System.out.println("Add trigger for job = " + jobName + " was clicked");

        return new AddTrigger(driver);
    }

    /**
     * View triggers for job by job name
     * @param jobName
     */
    public void viewTriggers(String jobName) throws InterruptedException
    {
        ((JavascriptExecutor) driver).executeScript("$('#schedulerForm\\\\:jobsTable_data tr td:contains(\"" + jobName + "\")').prev().find(\"div\").click()");
        System.out.println("View trigger for job = " + jobName + " was clicked");

        Thread.sleep(1_000);
    }

    /**
     * Delete job by job name
     * @param jobName
     * @return
     */
    public DeleteJob deleteJob(String jobName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#schedulerForm\\\\:jobsTable_data tr td:contains(\"" + jobName + "\")').next().next().next().find(\"button\")[2].click()");
        System.out.println("Delete job: " + jobName);

        return new DeleteJob(driver);
    }
}
