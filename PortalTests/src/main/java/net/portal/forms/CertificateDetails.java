package net.portal.forms;

import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

public class CertificateDetails extends PageObject
{
    @FindBy(id = "certificateDlgForm:certficatesDlgCancelButton")
    private WebElement cancelButton;

    @FindBy(id = "certificateDlgForm:saveCertificateChanges")
    private WebElement saveButton;

    @FindBy(id = "certificateDlgForm:certificateDataChooseButton_input")
    private WebElement fileInput;

    @FindBy(id = "certificateDlgForm:dataUploadedTrue")
    private WebElement uploadedTrueIcon;

    @FindBy(id = "certificateDlgForm:dataUploadedFalse")
    private WebElement uploadedFalseIcon;

    @FindBy(id = "certificateDlgForm:certificateDlgName")
    private WebElement certificateNameField;

    @FindBy(id = "certificateDlgForm:certificateDlgTypeSelect_label")
    private WebElement certificateTypeField;

    @FindBy(id = "certificateDlgForm:certificateDlgPassword")
    private WebElement certPasswordField;

    public CertificateDetails(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( ((JavascriptExecutor) driver).executeScript("return $('#certificateDlg_title').text()").equals("Certificate details"));
    }

    public void clickSave() throws InterruptedException
    {
        saveButton.click();
        Thread.sleep(1_00);
        System.out.println("CertificateDetails : Save button was clicked");
    }

    public void clickCancel() throws InterruptedException
    {
        cancelButton.click();
        Thread.sleep(1_00);
        System.out.println("CertificateDetails : Cancel button was clicked");
    }

    public void sendFileToInput(String path) throws InterruptedException
    {
        fileInput.sendKeys(path);
        Thread.sleep(1_00);
        System.out.println("CertificateDetails : sendFileToInput() method finished its work");
    }

    public void setFocusToInput() throws InterruptedException
    {
        ((JavascriptExecutor) driver).executeScript("$('#certificateDlgForm\\\\:certificateDataChooseButton_input').parent().focus()");
        Thread.sleep(1_00);
        System.out.println("CertificateDetails : setFocusToInput() method finished its work");
    }

    public void clickUpload() throws InterruptedException
    {
        this.setFocusToInput();
        Thread.sleep(1_00);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_00);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        System.out.println("CertificateDetails : Upload button was clicked");
    }

    public void setCertificateName(String name) throws InterruptedException
    {
        certificateNameField.clear();
        Thread.sleep(1_00);
        certificateNameField.sendKeys(name);
        Thread.sleep(1_00);
        System.out.println("CertificateDetails : Certificate name was set");
    }

    public boolean ifUploadedIcon() throws InterruptedException
    {
        boolean uploaded = false;
        String txt = uploadedTrueIcon.getAttribute("id");
        System.out.println("is Data uploaded mark changed to Ok : " + txt);
        Thread.sleep(1_00);
        if(txt.contains("True")) uploaded = true;
        System.out.println("CertificateDetails : ifUploadedIcon(): " + uploaded);

        return uploaded;
    }

    public boolean ifNoUploadedIcon() throws InterruptedException
    {
        boolean noUploaded = false;
        String txt = uploadedFalseIcon.getAttribute("id");
        System.out.println("is Data uploaded mark changed to Ok : " + txt);
        Thread.sleep(1_00);
        if(txt.contains("False")) noUploaded = true;
        System.out.println("CertificateDetails : ifNoUploadedIcon(): " + noUploaded);

        return noUploaded;
    }

    public void setCertificateType(String type) throws InterruptedException
    {
        certificateTypeField.click();
        Thread.sleep(1_00);
        String xP = "//li[@data-label='" + type + "']";
        driver.findElement(By.xpath(xP)).click();
        System.out.println("CertificateDetails : the following Certificate Type field was selected: " + type);
    }

    public void setCertPassword(String pass) throws InterruptedException
    {
        certPasswordField.clear();
        Thread.sleep(1_00);
        certPasswordField.sendKeys(pass);
        Thread.sleep(1_00);
        System.out.println("CertificateDetails : the following Certificate Pass was set: " + pass);
    }

    public boolean ifCertPassFieldActive() throws InterruptedException
    {
        boolean ifActive = true;
        String ifDisabled = certPasswordField.getAttribute("aria-disabled");
        Thread.sleep(1_00);
        if (ifDisabled.contains("true")) ifActive = false;
        System.out.println("CertificateDetails : ifCertPassFieldActive(): " + ifActive);

        return ifActive;
    }

}
