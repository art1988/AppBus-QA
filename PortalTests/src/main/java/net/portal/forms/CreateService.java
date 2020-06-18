package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class CreateService extends PageObject
{
    @FindBy(id = "addServiceForm:addServiceNextButton")
    private WebElement nextButton;


    public CreateService(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#addServiceDlg_title').text()").equals("Create service") );
    }

    /**
     * Select Type by exact name
     * @param type
     */
    public void selectType(String type)
    {
        ((JavascriptExecutor) driver).executeScript("$('#addServiceForm\\\\:addServiceType span').click()"); // Expand dropdown

        ((JavascriptExecutor) driver).executeScript("$('#addServiceForm\\\\:addServiceType_items li').filter(function() { return $(this).text() === '" + type + "'; }).click()"); // Select type (exact name)

        System.out.println(type + " was selected...");
    }

    public void clickNext() throws InterruptedException
    {
        Thread.sleep(4_000);
        nextButton.click();
        System.out.println("CreateService : Next button was clicked");
    }

}
