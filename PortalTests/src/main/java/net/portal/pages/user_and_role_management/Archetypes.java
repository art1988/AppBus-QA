package net.portal.pages.user_and_role_management;

import net.portal.forms.ArchetypesDetails;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class Archetypes extends PageObject
{
    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonAddNewBottom")
    private WebElement addNewButton;

    @FindBy(id = "table:tableForm:buttonBottomPanel:tableButtonDeleteBottom")
    private WebElement deleteButton;


    public Archetypes(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("User & Role Management > Archetypes") );
    }

    public ArchetypesDetails addNewArchetype()
    {
        addNewButton.click();
        System.out.println("Archetypes : Add New button was clicked");

        return new ArchetypesDetails(driver);
    }

    public void selectArchetype(String archetypeName)
    {
        ((JavascriptExecutor) driver).executeScript("$('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + archetypeName + "\")').parent().prev().find('span')[0].click()");
        System.out.println("Archetype with name = " + archetypeName + " was selected...");
    }

    public FollowingItemsWillBeDeleted deleteArchetype()
    {
        deleteButton.click();
        System.out.println("Archetypes : Delete button was clicked");

        return new FollowingItemsWillBeDeleted(driver);
    }
}
