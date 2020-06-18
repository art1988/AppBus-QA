package net.portal.pages.user_and_role_management;

import net.portal.constants.Retries;
import net.portal.forms.PolicyDetail;
import net.portal.forms.UploadPolicy;
import net.portal.pages.DeletePolicyConfirmation;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

public class Policies extends PageObject
{
    @FindBy(id = "uploadPolicy")
    private WebElement uploadPolicyButton;

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonAddNewTop")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonReloadTop")
    private WebElement refreshButton;

    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonDeleteBottom")
    private WebElement deleteButton;

    @FindBy(id = "filterForm:nameFilter")
    private WebElement nameSearchField;

    @FindBy(xpath = "//td[contains(.,'Name:')]")
    private WebElement nameLabel;

    @FindBy(id = "table:tableForm:entityTable:j_idt93:filter")
    private WebElement descriptionSearchField;

    @FindBy(xpath = "//span[@class='ui-column-title'][contains(.,'Provision')]")
    private WebElement provisionLabel;

    @FindBy(id = "filterForm:applyFilterButton")
    private WebElement applyFilterButton;

    @FindBy(xpath = "//span[contains(.,'Apply filter')]")
    private WebElement applyFilterButtonXpath;

    @FindBy(id = "filterForm:resetFilterButton")
    private WebElement resetFilterButton;



    public Policies(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("User & Role Management > Policies") );
    }

    public PolicyDetail addPolicy()
    {
        addNewButton.click();
        System.out.println("Policies : Add New button was clicked");

        return new PolicyDetail(driver);
    }

    public PolicyDetail refreshPolicy()
    {
        refreshButton.click(); //Time
        System.out.println("Policies : Refresh button was clicked");

        return new PolicyDetail(driver);
    }

    public DeletePolicyConfirmation clickFirstDeleteIcon() throws InterruptedException
    {
        Thread.sleep(2_000);

        int i = 0;
        try {
                while (driver.findElement(By.id("ajaxLoadingBar_modal")).isDisplayed()) {
                    Thread.sleep(2_000);
                    i++;
                    System.out.println("i from while is : " + i);
                    if ( i == 5 ) {driver.navigate().refresh(); Thread.sleep(5_000); break;}
                }
            } catch (Exception e) {System.out.println("i from catch is : " + i);}

        Thread.sleep(2_000);

        Retries.RETRY_10_TIMES.run(     () -> provisionLabel.click()); //Retry
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);

        System.out.println("Policies : Delete icon was clicked");

        return new DeletePolicyConfirmation(driver);
    }

    public void searchForName(String propertyName)
    {
        nameSearchField.clear();
        nameSearchField.sendKeys(propertyName);
    }

    public void searchForDescription(String description)
    {
        descriptionSearchField.sendKeys(description);
    }

    public void clickApplyFilter()
    {
        applyFilterButton.click();
        System.out.println("Policies : Apply filter button was clicked");
    }

    public void clickResetFilter()
    {
        resetFilterButton.click();
        System.out.println("Policies : Reset filter button was clicked");
    }

    /**
     * Click Edit button for property by name
     * @param policyName
     * @return
     */
    public PolicyDetail clickEdit(String policyName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + policyName + "\")').parent().next().next().next().next().next().next().next().next().find(\"button\").click()");
        System.out.println("Click Edit for property : " + policyName);

        return new PolicyDetail(driver);
    }

    /**
     * Delete policy by policy name
     * @param policyName name of policy to delete
     * @return
     */
    public DeletePolicyConfirmation deletePolicy(String policyName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + policyName + "\")').parent().next().next().next().next().next().next().next().find(\"button\")[0].click()");

        return new DeletePolicyConfirmation(driver);
    }

    public void downloadPolicy(String policyName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + policyName + "\")').parent().next().next().next().next().next().next().next().find(\"button\")[1].click()");
        System.out.println(policyName + " will be downloaded...");
    }

    public UploadPolicy uploadPolicy()
    {
        uploadPolicyButton.click();
        System.out.println("Policies : Upload Policy button was clicked...");

        return new UploadPolicy(driver);
    }
}
