package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

import java.util.List;

public class SureToDelete  extends PageObject
{
    @FindBy(xpath = "//span[contains(.,'Are you sure you want to delete?')]")
    private WebElement sureToDeleteLabel;

    @FindBy(id = "certificateRemoveConfirmDlg")
    private WebElement sureToDeleteCertDialogPop;

    @FindBy(id = "configRemoveConfirmDlg")
    private WebElement sureToDeleteConfDialogPop;

    @FindBy(id = "gatewayRemoveConfirmDlg")
    private WebElement sureToDeleteGateDialogPop;

    @FindBy(id = "serviceRemoveConfirmDlg")
    private WebElement sureToDeleteServDialogPop;


    public SureToDelete(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        if (sureToDeleteCertDialogPop.isDisplayed()) return ( sureToDeleteCertDialogPop.getText().contains("Are you sure you want to delete?") );
        if (sureToDeleteConfDialogPop.isDisplayed()) return ( sureToDeleteConfDialogPop.getText().contains("Are you sure you want to delete?") );
        if (sureToDeleteGateDialogPop.isDisplayed()) return ( sureToDeleteGateDialogPop.getText().contains("Are you sure you want to delete?") );
        if (sureToDeleteServDialogPop.isDisplayed()) return ( sureToDeleteServDialogPop.getText().contains("Are you sure you want to delete?") );
        return false;
    }

    public void clickYes() throws InterruptedException
    {
        sureToDeleteLabel.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        System.out.println("SureToDelete (Provision Config): Yes button was clicked");
    }

    public void clickYesCertByParent() throws InterruptedException
    {
        List<WebElement> buttons = sureToDeleteCertDialogPop.findElements(By.tagName("button"));
        if (buttons.get(0).getText().contains("Yes")) buttons.get(0).click();
        Thread.sleep(1_000);
        System.out.println("SureToDelete (Certificate) : Yes button's been found and clicked");
    }

    public void clickYesGateByParent() throws InterruptedException
    {
        List<WebElement> buttons = sureToDeleteGateDialogPop.findElements(By.tagName("button"));
        if (buttons.get(0).getText().contains("Yes")) buttons.get(0).click();
        Thread.sleep(1_000);
        System.out.println("SureToDelete (Certificate) : Yes button's been found and clicked");
    }

    public void clickYesServByParent() throws InterruptedException
    {
        List<WebElement> buttons = sureToDeleteServDialogPop.findElements(By.tagName("button"));
        if (buttons.get(0).getText().contains("Yes")) buttons.get(0).click();
        Thread.sleep(1_000);
        System.out.println("SureToDelete (Service) : Yes button's been found and clicked");
    }
}
