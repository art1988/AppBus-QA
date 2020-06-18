package net.portal.pages.user_and_role_management;

import net.portal.forms.*;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

public class Profiles extends PageObject {

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonAddNewTop")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonReloadTop")
    private WebElement refreshProfilesButton;

    public Profiles(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("User & Role Management > Profiles") );
    }

    public ProfileDetail addProfile()
    {
        addNewButton.click();
        System.out.println("Profiles : Add New button was clicked");

        return new ProfileDetail(driver);
    }

    public void refreshProfile()
    {
        refreshProfilesButton.click();
        System.out.println("Profiles : Refresh button was clicked");
    }

    /**
     * Delete profile by profile name
     * @param profileName name of profile to delete
     * @return
     */
    public DeleteWithAssignments clickDelete(String profileName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + profileName + "\")').parent().next().next().next().find(\"button\").click()");
        System.out.println("The following profile will be deleted : " + profileName);

        return new DeleteWithAssignments(driver);
    }

    public DeleteWithAssignments clickDeleteIcon(String propertyName) throws InterruptedException
    {
        boolean clicked = false;
        driver.navigate().refresh();
        Thread.sleep(5_000);

        System.out.println("Going to click the following text, then click Delete : " + propertyName);
        String xP = "//span[contains(.,'" + propertyName + "')]";
        driver.findElement(By.xpath(xP)).click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        System.out.println("getText = " + driver.switchTo().activeElement().getText());
        if (driver.switchTo().activeElement().getText().contains("Delete with assignments")) { driver.switchTo().activeElement().click(); clicked = true; }
        else {
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            if (driver.switchTo().activeElement().getText().contains("Delete with assignments")) { driver.switchTo().activeElement().click(); clicked = true; }
            else {
                Thread.sleep(1_000);
                driver.switchTo().activeElement().sendKeys(Keys.TAB);
                Thread.sleep(1_000);
                if (driver.switchTo().activeElement().getText().contains("Delete with assignments")) { driver.switchTo().activeElement().click(); clicked = true; }
            }
        }

        if (clicked) System.out.println("Just clicked Delete for property : " + propertyName);
        else System.out.println("Can't click Delete for property : " + propertyName);

        return new DeleteWithAssignments(driver);
    }

}
