package net.portal.pages.user_and_role_management;

import net.portal.forms.ApplicationDetail;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Application extends PageObject
{
    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonAddNewTop")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonDeleteTop")
    private WebElement deleteButton;

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonReloadTop")
    private WebElement refreshButton;


    public Application(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("User & Role Management > Application") );
    }

    public ApplicationDetail addNewApplication()
    {
        addNewButton.click();

        return new ApplicationDetail(driver);
    }

    /**
     * Find application by applicationName and set new name as newName
     * @param applicationName
     * @param newName
     * @throws InterruptedException
     */
    public void editApplication(String applicationName, String newName) throws InterruptedException
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data tr td span:contains(\"" + applicationName + "\")').parent().next().find(\"button\").click()"); // click edit button
        Thread.sleep(1_000);
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data input:text').val(\"" + newName + "\")"); // set text into input
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data input:text').parent().next().find(\"button\")[0].click()"); // click accept
    }

    public FollowingItemsWillBeDeleted deleteApplication(String applicationName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data tr td span:contains(\"" + applicationName + "\")').parent().prev().find(\"input\").click()");
        deleteButton.click();

        return new FollowingItemsWillBeDeleted(driver);
    }

    public void clickRefresh()
    {
        refreshButton.click();
    }
}
