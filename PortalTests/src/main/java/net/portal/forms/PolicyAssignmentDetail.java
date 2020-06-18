package net.portal.forms;

import net.portal.constants.Retries;
import net.portal.pages.DeleteConfirmPopup;
import net.portal.forms.*;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import net.portal.forms.PolicyAssDetailMultipleValues;

import javax.management.relation.Role;

public class PolicyAssignmentDetail extends PageObject

{
    @FindBy(id = "entity:dialogsForm:property-property_label")
    private WebElement policyField;

    @FindBy(id = "entity:dialogsForm:property-application-version")
    private WebElement appVerTextField;

    @FindBy(xpath = "//*[@label='ui-state-disabled' and text='Group']") //wrong xpath
    private WebElement groupRadio;

    @FindBy(id = "entity:dialogsForm:property-application_label")
    private WebElement appList;

    @FindBy(id = "entity:dialogsForm:property-user")
    private WebElement userField;

    @FindBy(id = "entity:dialogsForm:property-os-version")
    private WebElement osVersionField;

    @FindBy(id = "entity:dialogsForm:addEntity")
    private WebElement addEntityButton;

    @FindBy(id = "entity:dialogsForm:cancelEntity")
    private WebElement cancelEntityButton;

    private WebElement tempButton;
    private WebElement tempField;

    private int policyValueIndex;

    public void setPolicyName(String pName) throws InterruptedException
    {
        //((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:type .ui-icon-triangle-1-s').click()"); // expand dropdown
        policyField.click();
        Thread.sleep(2_000);
        policyField.findElement(By.xpath("//*[@role='option' and text()='" + pName + "']")).click();
        System.out.println("policyName has just been selected");
        //((JavascriptExecutor) driver).executeScript("$(\"#entity\\\\:dialogsForm\\\\:type_items li:contains('" + pName + "')\").click()");
    }

    public void setAppName(String aName) throws InterruptedException
    {
        //((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:type .ui-icon-triangle-1-s').click()"); // expand dropdown
        appList.click();
        Thread.sleep(2_000);
        appList.findElement(By.xpath("//*[@role='option' and text()='" + aName + "']")).click();
        System.out.println("Application Name has just been selected");
        //((JavascriptExecutor) driver).executeScript("$(\"#entity\\\\:dialogsForm\\\\:type_items li:contains('" + pName + "')\").click()");
    }


    public PolicyAssignmentDetail(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
        // TODO: if click edit of Policy Value -> then need to init policyValueIndex
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#entity\\\\:dialogsForm\\\\:entityDialog_title').text()").equals("Policy assignment detail") );
    }

    public void setOSversion(String name)
    {
        osVersionField.clear();
        osVersionField.sendKeys(name);
    }

    public void setUser(String description)
    {
        userField.clear();
        userField.sendKeys(description);
    }

    public void clickAppList(String description)
    {
        appList.click();
    }

    public void clickUserRadio() throws InterruptedException
    {
        appVerTextField.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.ARROW_RIGHT);
        driver.switchTo().activeElement().sendKeys(Keys.ARROW_LEFT);

        System.out.println("USER radio has just been clicked");
    }

    public void clickLDAPradio() throws InterruptedException

    {
        appVerTextField.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.ARROW_RIGHT);
        driver.switchTo().activeElement().sendKeys(Keys.ARROW_RIGHT);

        System.out.println("GROUP radio has just been clicked");
    }

    public void clickGroupRadio() throws InterruptedException
    {
        appVerTextField.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.ARROW_RIGHT);


        System.out.println("GROUP radio has just been clicked");
    }

    public void twiceClickPolicyField() throws InterruptedException //to send the focus
    {
        policyField.click();
        Thread.sleep(2_000);
        policyField.click();
        Thread.sleep(1_000);

    }

      public PolicyAssDetailMultipleValues editValuesIconClick() throws InterruptedException
      {
          driver.switchTo().activeElement().sendKeys(Keys.SPACE);
          Thread.sleep(2_000);
          System.out.println("PolicyAssDetailMultipleValues : Edit icon was clicked...");

          return new PolicyAssDetailMultipleValues(driver);
      }

    public void setPolicyValuesEditing(String[] args) throws InterruptedException
    {
        String classElem;
        if (args.length > 0)
        {
            this.twiceClickPolicyField();
            driver.switchTo().activeElement().sendKeys(Keys.TAB);

            classElem = driver.switchTo().activeElement().getAttribute("role");

            switch (classElem) {

                case "textbox": {
                    driver.switchTo().activeElement().sendKeys(args[0]);
                }
                case "button": {
                    //driver.switchTo().activeElement().sendKeys(Keys.TAB);
                    PolicyAssDetailMultipleValues multiValuPopUpPage = editValuesIconClick();
                    tempButton = multiValuPopUpPage.getAddValueButton();
                    for (int i=0; i < args.length; i++)
                    {
                        System.out.println("Going to click the Add button, iteration : " + i);
                        if (i == 0) {tempButton.click(); Thread.sleep(2_000);}
                        else driver.switchTo().activeElement().sendKeys(Keys.SPACE);
                        System.out.println("the Add button's just been clicked, iteration : " + i);
                    }
                    Thread.sleep(1_000);
                    multiValuPopUpPage.setFocuseOnFirstField();
                    Thread.sleep(2_000);
                    for (int i=0; i < args.length; i++)
                    {
                        tempField = driver.switchTo().activeElement();  //z
                        JavascriptExecutor executor = (JavascriptExecutor)driver; //z
                        executor.executeScript("arguments[0].click();", tempField); //z
                        executor.executeScript("arguments[0].setAttribute('text','{VAL01}');", tempField); //z
                        System.out.println("tempField class is " + tempField.getClass());
                        System.out.println("tempField is selected : " + tempField.isSelected());

                        //String sID = "#" + tempField.getAttribute("id");
                        //sID = sID.replaceAll("[:]","\\\\:");
                        String sID = tempField.getAttribute("id");
                        System.out.println("tempField ID : " + sID);
                        System.out.println("tempField ROLE : " + tempField.getAttribute("role"));
                        //((JavascriptExecutor) driver).executeScript("$(arguments[0]).attr(\"text\", \"myNewActionTarget.html\");", sID);
                        String tempS = args[i];
                        driver.findElement(By.id(sID)).sendKeys(tempS);
                        //driver.switchTo().activeElement().sendKeys(args[i]); Thread.sleep(2_000);
                        System.out.println("just sent the argument to the filed, argument #: " + i);
                        driver.switchTo().activeElement().sendKeys(Keys.TAB); Thread.sleep(2_000);
                        driver.switchTo().activeElement().sendKeys(Keys.TAB); Thread.sleep(2_000);
                    }
                        //click "Ok":
                    driver.switchTo().activeElement().sendKeys(Keys.TAB); Thread.sleep(2_000);
                    driver.switchTo().activeElement().sendKeys(Keys.SPACE); Thread.sleep(2_000);

                }
            }
            //((JavascriptExecutor) driver).executeScript("$('#entity\\\\:dialogsForm\\\\:provision span').click()");
            System.out.println("ValuesEditing : ValuesEditing method finished its work");
        }
        else

            {
                System.out.println("ValuesEditing : ValuesEditing method need args");
            }


    }

    public void clickAdd()
    {
        Retries.RETRY_10_TIMES.run(() -> addEntityButton.click()); //Retry
        System.out.println("PolicyAssignmentDetail : addEntityButton's been clicked");
    }

    public void clickCancel()
    {
        cancelEntityButton.click();
    }

}
