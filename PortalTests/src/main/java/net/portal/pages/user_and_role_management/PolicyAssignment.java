
package net.portal.pages.user_and_role_management;

        import net.portal.forms.*;
        import net.portal.pages.PageObject;
        import org.junit.Assert;
        import org.openqa.selenium.*;
        import org.openqa.selenium.support.FindBy;

public class PolicyAssignment extends PageObject
{

    @FindBy(id = "table:tableForm:buttonTopPanel:tableButtonAddNewTop")
    private WebElement addNewButton;

    @FindBy(xpath = "//*[text()='Policy Name']")
    private WebElement PolicyNameColHead;

    @FindBy(xpath = "//*[@class='ui-panel-title']")
    private WebElement HeadOfPage;

    @FindBy(xpath = "//*[text()='Following items will be deleted']")
    private WebElement HeadOfDelPopUp;

    public PolicyAssignment(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("User & Role Management > Policy Assignment") );
    }

    public PolicyAssignmentDetail addPolicyAssignment()
    {
        addNewButton.click();
        System.out.println("PolicyAssignment : Add New button was clicked...");

        return new PolicyAssignmentDetail(driver);
    }

    public void setFocusOnPolicyNameField() throws InterruptedException
    {
        PolicyNameColHead.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        System.out.println("PolicyAssignment : Focus is on Policy Name field");

    }

    public void filterPolicyByName(String policyName) throws InterruptedException
    {
        this.setFocusOnPolicyNameField();
        driver.switchTo().activeElement().sendKeys(policyName);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        System.out.println("PolicyAssignment : Policy Name is entered ");

    }

    public void selectPolicyByName(String polName) throws InterruptedException
    {

        String xPath1 = "//*[@title='" + polName + "' and text()='" + polName + "']"; // //*[@title='tstPLCauto_01' and text()='tstPLCmanual_01']
        System.out.println("xPath1 : " + xPath1);
        driver.findElement(By.xpath(xPath1)).click();
        //driver.findElement(By.ByXPath())

        Thread.sleep(1_000);
        System.out.println("PolicyAssignment : Policy Name is clicked ");

    }

    public void setFocuseOnDeleteButton() throws InterruptedException
    {
        HeadOfPage.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        System.out.println("PolicyAssignment : Focus is on DeleteButton");
    }

    public void clickDeleteButton() throws InterruptedException
    {
        this.setFocuseOnDeleteButton();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        System.out.println("PolicyAssignment : Focus is on DeleteButton");
    }

    public void clickDeleteOnPopUp() throws InterruptedException
    {
        HeadOfDelPopUp.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);
        System.out.println("PolicyAssignment : DeleteButton on pop up window accepted click operation");
    }




}
