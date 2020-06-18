package net.portal.pages.device_management;

import net.portal.constants.Const;
import net.portal.forms.*;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

import java.io.File;
import java.util.List;

import static java.lang.Integer.valueOf;

public class ProvisioningConfig extends PageObject
{
    JavascriptExecutor js = (JavascriptExecutor)driver;

    @FindBy(id = "ui-datepicker-div")
    private WebElement calendar;

    @FindBy(xpath = "//a[@class='ui-state-default'][contains(.,'1')]")
    private WebElement theFirstDateButton;

    @FindBy(xpath = "//span[contains(.,'You have expired config. Delete it or make upcoming?')]")
    private WebElement expiredConfigFlag;

    @FindBy(id = "form:errorPanel")
    private WebElement errorPanel;

    @FindBy(id = "form:turnExpiredToUpcoming")
    private WebElement makeUpcomingButton;

    @FindBy(id = "form:jsonUpload")
    private WebElement formJSONupload;

    @FindBy(id = "form:configsSelect_label")
    private WebElement selectConfigurationField;

    @FindBy(id = "form:certificatesTable:addCertificate")
    private WebElement addCertButton;

    @FindBy(id = "form:downloadConfigButton")
    private WebElement downloadConfigButton;

    @FindBy(id = "form:copyConfigButton")
    private WebElement copyConfButton;

    @FindBy(id = "form:configsSelect_items")
    private WebElement configItemsList;

    @FindBy(id = "form:addConfigButton")
    private WebElement addConfigButton;

    @FindBy(id = "form:servicesTable:addService")
    private WebElement addServiceButton;

    @FindBy(xpath = "//button[@id='form:gatewaysTable:addGateway']") //@FindBy(id = "form:gatewaysTable:addGateway")
    private WebElement addGatewayButton;

    @FindBy(id = "form:gatewaysTable:0:editGateway")
    private WebElement editTheFirstGatewayBut;

    @FindBy(id = "form:certificatesTable:0:editCertificate")
    private WebElement editTheFirstCertifiBut;

    @FindBy(id = "form:certificatesTable:0:certificateName")
    private WebElement theFirstCertNameField;

    @FindBy(id = "form:certificatesTable:0:downloadCertificate")
    private WebElement theFirstCertDownloadButton;

    @FindBy(id = "form:certificatesTable:1:editCertificate")
    private WebElement editTheSecondCertifiBut;

    @FindBy(id = "form:gatewaysTable:1:editGateway")
    private WebElement editTheSecondGatewayBut;

    @FindBy(id = "form:saveConfigButton")
    private WebElement applyButton;

    @FindBy(id = "form:revertConfigButton")
    private WebElement revertChangesButton;

    @FindBy(xpath = "//li[@data-label='Upcoming config']")
    private WebElement upcomingConfigItem;

    @FindBy(xpath = "//li[@data-label='Current config']")
    private WebElement currentConfigItem;

    @FindBy(id = "form:deleteConfigButton")
    private WebElement deleteConfigButton;

    @FindBy(id = "form:configStartTime_input")
    private WebElement startTimeFiled;

    @FindBy(id = "form:certificatesTable")
    private WebElement certTable;

    @FindBy(id = "form:gatewaysTable_data")
    private WebElement gatewaysTable;

    @FindBy(id = "form:servicesTable_data")
    private WebElement serviceTable;

    @FindBy(id = "form:jsonUpload_input")
    private WebElement uploadInput;

    @FindBy(id = "form:uploadConfigButton")
    private WebElement uploadConfigButton;

    @FindBy(id = "form:deleteExpiredConfig")
    private WebElement delExpiredConfButton;

    public ProvisioningConfig(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Device management > Provisioning Config") );
    }

    public boolean isErrorPanelVisible() throws InterruptedException
    {
        boolean ep = errorPanel.isDisplayed();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : isErrorPanelVisible: " + ep);
        return ep;
    }

    public void deleteExpiredConfig() throws InterruptedException
    {
        boolean ep = false;
        try {
            ep = errorPanel.isDisplayed();
        } catch (Exception e) {}

        Thread.sleep(1_000);
        if(ep) delExpiredConfButton.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Delete Expired Config was clicked, true/false : " + ep);
    }

    public AddNewProvConfig makeUpcomingConfig() throws InterruptedException
    {
        makeUpcomingButton.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Make Upcoming was clicked");

        return new AddNewProvConfig(driver);
    }

    public String getCertTableContent() throws InterruptedException
    {
        String tb = certTable.getAttribute("innerHTML");
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : certTable.getAttribute(\"innerHTML\"): " + tb);
        return tb;
    }

    public String getErrorMessage() throws InterruptedException
    {
        String em = errorPanel.getText();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : errorPanel.getText(): " + em);
        return em;
    }

    public String getCertTableText() throws InterruptedException
    {
        //String tb = ((JavascriptExecutor) driver).executeScript("$('#form\\\\:certificatesTable').text()").toString();
        String tb = js.executeScript("return $('#form\\\\:certificatesTable').text()").toString();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : certTable.getText(): " + tb);
        return tb;
    }

    public String getCertTableRowText(String Cname) throws InterruptedException
    {
        //String tb = ((JavascriptExecutor) driver).executeScript("$('#form\\\\:certificatesTable').text()").toString();
        List<WebElement> tds = driver.findElements(By.xpath("//tbody[@id='form:certificatesTable_data']/tr"));
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : got list of Sertificate tb rows, tds.size(): " + tds.size());
        String resultROW = "empty";
        for (int i=0; i < tds.size(); i++)
        {
            String row = tds.get(i).getAttribute("outerHTML");
            if (row.contains(Cname)) resultROW = row;
        }

        return resultROW;
    }

    public String getGatewaysTableContent() throws InterruptedException
    {
        String tb = gatewaysTable.getAttribute("innerHTML");
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : gatewaysTable.getAttribute(\"innerHTML\"): " + tb);
        return tb;
    }

    public String getGatewaysTableText() throws InterruptedException
    {
        //String tb = gatewaysTable.getText();
        String tb = js.executeScript("return $('#form\\\\:gatewaysTable_data').text()").toString();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : gatewaysTable.getText(): " + tb);
        return tb;
    }

    public String getGatewayTableRowText(String Gname) throws InterruptedException
    {

        List<WebElement> tds = driver.findElements(By.xpath("//tbody[@id='form:gatewaysTable_data']/tr"));
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : got list of Gateways tb rows, tds.size(): " + tds.size());
        String resultROW = "empty";
        for (int i=0; i < tds.size(); i++)
        {
            String row = tds.get(i).getAttribute("outerHTML");
            if (row.contains(Gname)) resultROW = row;
        }

        return resultROW;
    }

    public String getServiceTableContent() throws InterruptedException
    {
        String tb = serviceTable.getAttribute("innerHTML");
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : serviceTable.getAttribute(\"innerHTML\"): " + tb);
        return tb;
    }

    public String getServiceTableText() throws InterruptedException
    {
        //String tb = serviceTable.getText();
        String tb = js.executeScript("return $('#form\\\\:servicesTable_data').text()").toString();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : serviceTable.getText(): " + tb);
        return tb;
    }

    public String getServiceTableRowText(String Sname) throws InterruptedException
    {

        List<WebElement> tds = driver.findElements(By.xpath("//tbody[@id='form:servicesTable_data']/tr"));
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : got list of Services tb rows, tds.size(): " + tds.size());
        String resultROW = "empty";
        for (int i=0; i < tds.size(); i++)
        {
            String row = tds.get(i).getAttribute("outerHTML");
            if (row.contains(Sname)) resultROW = row;
        }

        return resultROW;
    }

    public AddNewProvConfig clickAddConfig() throws InterruptedException
    {
        addConfigButton.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Add Config button was clicked...");

        return new AddNewProvConfig(driver);
    }

    public ServiceDetails clickAddService() throws InterruptedException
    {
        addServiceButton.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Add Service button was clicked...");

        return new ServiceDetails(driver);
    }

    public GatewayDetails clickAddGateway() throws InterruptedException
    {
        addGatewayButton.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Add Gateway button was clicked...");

        return new GatewayDetails(driver);
    }

    public GatewayDetails clickEditTheFirstGateway() throws InterruptedException
    {
        editTheFirstGatewayBut.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Edit Gateway button (the first one) was clicked...");

        return new GatewayDetails(driver);
    }

    public CertificateDetails clickEditTheFirstCertifi() throws InterruptedException
    {
        editTheFirstCertifiBut.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Edit Certificate button (the first one) was clicked...");

        return new CertificateDetails(driver);
    }

    public CertificateDetails clickEditTheSecondCertifi() throws InterruptedException
    {
        editTheSecondCertifiBut.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Edit Certificate button (the second one) was clicked...");

        return new CertificateDetails(driver);
    }

    public String downloadTheFirstCert() throws InterruptedException
    {
        String fName = theFirstCertNameField.getText();
        Thread.sleep(1_000);
        theFirstCertDownloadButton.click();
        System.out.println("ProvisioningConfig : Download Certificate button (the first one) was clicked...");

        return fName;
    }

    public GatewayDetails clickEditTheSecondGateway() throws InterruptedException
    {
        editTheSecondGatewayBut.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Edit Gateway button (the second one) was clicked...");

        return new GatewayDetails(driver);
    }

    public boolean ifAddConfigEnabled() throws InterruptedException
    {
        boolean enabled = addConfigButton.isEnabled();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Add Config button is enabled : " + enabled);

        return enabled;
    }

    public void clickRevertChanges() throws InterruptedException
    {
        revertChangesButton.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Revert Changes button was clicked...");
    }

    public void setStartTime(String date) throws InterruptedException
    {
        startTimeFiled.click();
        Thread.sleep(1_000);
        startTimeFiled.clear();
        Thread.sleep(1_000);
        startTimeFiled.sendKeys(date);
        Thread.sleep(1_000);
        startTimeFiled.sendKeys(Keys.ENTER);
        System.out.println("ProvisioningConfig : Start time was set...");
    }

    public void clickDownloadConfigButton() throws InterruptedException
    {
        downloadConfigButton.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Download Config button was clicked...");
    }

    public void clickApply() throws InterruptedException
    {
        System.out.println("ProvisioningConfig : Going to click Apply Changes button...");
        ((JavascriptExecutor) driver).executeScript("$('#form\\\\:saveConfigButton').click()");
        //applyButton.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Apply Changes button was clicked...");
    }

    public AddNewProvConfig clickCopyConfig() throws InterruptedException
    {
        copyConfButton.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Copy Provisioning Config button was clicked...");
        return new AddNewProvConfig(driver);
    }

    public CertificateDetails clickAddCertificate() throws InterruptedException
    {
        addCertButton.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Add Certificate button was clicked");

        return new CertificateDetails(driver);
    }

    public String getStartTimeValue() throws InterruptedException
    {
        String date = startTimeFiled.getText();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Start Time field value is gotten");

        return date;
    }

    public SureToDelete clickDeleteConfig() throws InterruptedException
    {
        deleteConfigButton.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Delete Config button was clicked...");

        return new SureToDelete(driver);
    }

    public void clickSelectConfiguration() throws InterruptedException
    {
        //f selectConfigurationField.click(); //f
        ((JavascriptExecutor)driver).executeScript("$('#form\\\\:configsSelect_label').click()"); //p
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Select Configuration was clicked...");
    }

    public void clickUpcomingConfig() throws InterruptedException
    {
        upcomingConfigItem.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Upload Config item was clicked...");
    }

    public void clickCurrentConfig() throws InterruptedException
    {
        currentConfigItem.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Current Config item was clicked...");
    }

    public void uploadConfig(String path) throws InterruptedException
    {

        System.out.println("Checking that config file exists...");
        File configFile = new File(path);
        Assert.assertTrue(configFile.exists());

        System.out.println("ProvisioningConfig : Going to send file to uploadInput...");

        uploadInput.sendKeys(path);
        System.out.println("ProvisioningConfig : Going to click Upload Config button...");
        Thread.sleep(1_000);
        uploadConfigButton.click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Upload Config was performed...");
    }

    public String getConfigItemsList() throws InterruptedException
    {
        this.clickSelectConfiguration();
        Thread.sleep(1_000);
        String fullText = configItemsList.getText();
        System.out.println("ProvisioningConfig : getConfigItemsList method is copleted...");
        this.clickSelectConfiguration();

        return fullText;
    }

    public SureToDelete deleteCertificateByName(String name) throws InterruptedException
    {
        //((JavascriptExecutor) driver).executeScript("return $('#setStartTimeForNewConfigDlg_title').text()");
        String xP = "//span[contains(.,'" + name + "')]/../..";
        WebElement row = driver.findElement(By.xpath(xP));
        String rowNumber = row.getAttribute("data-ri");
        String removeButtonID = "form:certificatesTable:" + rowNumber + ":removeCertificate";
        Thread.sleep(1_000);
        driver.findElement(By.id(removeButtonID)).click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Remove Certificate Button # " + rowNumber + "was clicked...");

        return new SureToDelete(driver);
    }

    public SureToDelete deleteGatewayByName(String name) throws InterruptedException
    {
        String xP = "//span[contains(.,'" + name + "')]/../..";
        WebElement row = driver.findElement(By.xpath(xP));
        String rowNumber = row.getAttribute("data-ri");
        String removeButtonID = "form:gatewaysTable:" + rowNumber + ":removeGateway";
        Thread.sleep(1_000);
        driver.findElement(By.id(removeButtonID)).click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Remove Gateway Button # " + rowNumber + "was clicked...");

        return new SureToDelete(driver);
    }

    public SureToDelete deleteServiceByName(String name) throws InterruptedException
    {
        String xP = "//td[contains(.,'" + name + "')]/..";
        WebElement row = driver.findElement(By.xpath(xP));
        String rowNumber = row.getAttribute("data-ri");
        String removeButtonID = "form:servicesTable:" + rowNumber + ":removeService";
        Thread.sleep(1_000);
        driver.findElement(By.id(removeButtonID)).click();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : Remove Service Button # " + rowNumber + "was clicked...");

        return new SureToDelete(driver);
    }

    public int getServicesNumber() throws InterruptedException
    {
        //WebElement servDataTable = driver.findElement(By.xpath("//*[@id='form:servicesTable_data']"));
        String xP = "//tbody[@id='form:servicesTable_data']/tr[@role='row']";
        List<WebElement> rows = driver.findElements(By.xpath(xP));
        int rowsNumber = rows.size();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : serviceTable.rows.size() is : " + rowsNumber);

        return rowsNumber;
    }

    public int getGatewaysNumber() throws InterruptedException
    {
        String xP = "//tbody[@id='form:gatewaysTable_data']/tr[@role='row']";
        List<WebElement> rows = driver.findElements(By.xpath(xP));
        int rowsNumber = rows.size();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : gatewaysTable.rows.size() is : " + rowsNumber);

        return rowsNumber;
    }

    public int getCertificNumber() throws InterruptedException
    {
        String xP = "//tbody[@id='form:certificatesTable_data']/tr[@role='row']";
        List<WebElement> rows = driver.findElements(By.xpath(xP));
        int rowsNumber = rows.size();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : certificatesTable_data.rows.size() is : " + rowsNumber);

        return rowsNumber;
    }

    public List<WebElement> getServicesRows() throws InterruptedException
    {
        String xP = "//tbody[@id='form:servicesTable_data']/tr[@role='row']";
        List<WebElement> rows = driver.findElements(By.xpath(xP));
        int rowsNumber = rows.size();
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : going to return List<WebElement>, serviceTable.rows.size() is : " + rowsNumber);

        return rows;
    }

    public int getServiceIndex(String sName) throws InterruptedException
    {
        String xP = "//tbody[@id='form:servicesTable_data']/tr[@role='row']";
        List<WebElement> rows = driver.findElements(By.xpath(xP));
        int rowsNumber = rows.size();
        int rowN = 999;
        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : going to use List<WebElement>, serviceTable.rows.size() is : " + rowsNumber);
        for (int j=0; j < rows.size(); j++)
        {
            String rText = rows.get(j).getAttribute("outerHTML");
            String nText = rows.get(j).getAttribute("data-ri");
            if (rText.contains(sName)) { rowN = valueOf(nText); break; }
        }
        System.out.println("ProvisioningConfig : going to return rowN : " + rowN + " ...it's row of " + sName + " Service name.");
        return rowN;
    }

    public String getGatewayRowText(int rowNm) throws InterruptedException
    {
        String xP = "//tbody[@id='form:gatewaysTable_data']/tr[@role='row'][@data-ri='" + rowNm + "']";
        WebElement row = driver.findElement(By.xpath(xP));
        String rowText = row.getText();

        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : going to return GatewayRowText, rowText is : " + rowText);

        return rowText;
    }

    public String getCertifiRowText(int rowNm) throws InterruptedException
    {
        String xP = "//tbody[@id='form:certificatesTable_data']/tr[@role='row'][@data-ri='" + rowNm + "']";
        WebElement row = driver.findElement(By.xpath(xP));
        String rowText = row.getText();

        Thread.sleep(1_000);
        System.out.println("ProvisioningConfig : going to return CertificateRowText, rowText is : " + rowText);

        return rowText;
    }

    public boolean clickYesterday() throws InterruptedException
    {
        boolean done = false;
        int itemNumber = 100;
        List<WebElement> items = calendar.findElements(By.xpath("//td[@data-handler='selectDay']"));
        Thread.sleep(1_000);
        System.out.println("AddNewProvConfig : items.size() is : " + items.size());
        for(int i=0; i < items.size(); i++)
        {
            String selected = items.get(i).getAttribute("class");
            if (selected.contains("ui-datepicker-today"))
            {
                itemNumber = i;
                System.out.println("AddNewProvConfig : detected day is : " + items.get(i).getText());
                System.out.println("AddNewProvConfig : detected day is : " + items.get(i).findElement(By.xpath("//td/a[@href='#']")).getAttribute("outerHTML").toString());
                System.out.println("AddNewProvConfig : detected day is : " + items.get(i).getAttribute("class").toString());
            }

        }
        Thread.sleep(1_000);
        if (itemNumber > 1)
        {
            itemNumber--; items.get(itemNumber).click(); done = true;
        }
        else
        {
            //previosMonthTriangle.click();
            List<WebElement> Titems = calendar.findElements(By.xpath("//span[@class='ui-icon ui-icon-circle-triangle-w']"));
            System.out.println("Titems.size(): " + Titems.size());
            Titems.get(0).click();
            Thread.sleep(1_000);
            theFirstDateButton.click();
            done = true;
        }
        Thread.sleep(1_000);
        System.out.println("AddNewProvConfig : clickYesterday : if operation is done : " + done);
        return done;
    }

}
