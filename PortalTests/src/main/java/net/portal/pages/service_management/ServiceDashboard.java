package net.portal.pages.service_management;

import net.portal.forms.DownloadServiceClientLibrary;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.FindBy;

import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.util.List;

//import static com.sun.org.apache.xml.internal.serialize.LineSeparator.Windows;

    public class ServiceDashboard  extends PageObject
    {
        static final SimpleDateFormat sdf = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss");
        Timestamp timestp = new Timestamp(System.currentTimeMillis());
        String tmstp = sdf.format(timestp);
        String time = tmstp.substring(5).replaceAll("[-+.^:,]","");



        @FindBy(id = "serviceDashboard:filterPanel")
        private WebElement topPanel;

        @FindBy(xpath = "//span[@class='ui-icon ui-icon-grip-dotted-vertical']")
        private WebElement projectLabelofField;

        @FindBy(xpath = "//span[contains(.,'Apply')]")
        private WebElement applyButton;

        @FindBy(xpath = "//span[@class='ui-button-text ui-c'][contains(.,'All services')]")
        private WebElement AllServicesButton;

        @FindBy(xpath = "//span[@class='ui-column-title'][contains(.,'Name')]")
        private WebElement nameColumnTitle;

        @FindBy(xpath = "//input[contains(@name,'editableInput')][@value='*']")
        private WebElement serviceNameField;

        @FindBy(xpath = "//span[@class='ui-panel-title'][contains(.,'Service Management > Service Dashboard')]")
        private WebElement pageLabel;

        @FindBy(id = "serviceDashboard:closeSwaggerButton")
        private WebElement closeOpenAPISpecificationButton;



        public ServiceDashboard(WebDriver driver)
        {
            super(driver);
            Assert.assertTrue(isInit());
        }

        private boolean isInit()
        {
            return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Service Management > Service Dashboard") );
        }

        public WebElement getTopPanel() throws InterruptedException
        {
            WebElement currentTopPanel  = driver.switchTo().activeElement().findElement(By.id("serviceDashboard:filterPanel"));
            Thread.sleep(1_000);
            return currentTopPanel;
        }

        public void setProjectName(String projectName) throws InterruptedException
        {
            Thread.sleep(3_000);
            pageLabel.click();
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);

            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.SPACE);
            Thread.sleep(2_000);
            String xP = "//li[contains(.,'" + projectName + "')]"; //li[contains(.,'autoPRG03004525')]
            Thread.sleep(2_000);
            driver.findElement(By.xpath(xP)).click();
        }

        public boolean checkServiceList(String[] serviseLIst) throws InterruptedException
        {
            Thread.sleep(1_000);
            List<WebElement> rows = driver.findElements(By.xpath("//tbody[@id='serviceDashboard:serviceDashboardTable_data']/tr"));
            Thread.sleep(1_000);
            boolean success = false;
            int s = 0; //number of equals
            String classE = "";

            for (int i=0; i < rows.size(); i++)
            {
                String displayedServName = driver.findElement(By.xpath("//tbody[@id='serviceDashboard:serviceDashboardTable_data']/tr[@data-ri='" + i + "']/td[1]")).getText();
                System.out.println(displayedServName);
                boolean ifItemExists = false;
                for (int j=0; j < serviseLIst.length; j++)
                if (serviseLIst[j].equals(displayedServName)) { s++; ifItemExists = true; serviseLIst[j] = ""; break;}
                if (!ifItemExists) {success = false; System.out.println("Got error - There is additional ServiceName that haven't been created by user :" + driver.switchTo().activeElement().getText()); break; } //return success;
                Thread.sleep(1_000);
            }
            if (s == serviseLIst.length) success = true;
            System.out.println("checkServiceList.success is " + success);

            return success;
        }

        public boolean chooseANDcheckService(String srvName) throws InterruptedException
        {
            boolean success = false;

            Thread.sleep(1_000);
            serviceNameField.click();
            Thread.sleep(1_000);
            serviceNameField.clear();
            Thread.sleep(1_000);
            serviceNameField.sendKeys(srvName);
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            this.clickApplyButton();
            Thread.sleep(2_000);
            nameColumnTitle.click();
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            String displayedServName = driver.switchTo().activeElement().getText();
            System.out.println(displayedServName);

            if (srvName.equals(displayedServName)) {success = true; }
            System.out.println("chooseANDcheckService.success is " + success);

            return success;
        }

        public boolean chooseANDcheckServiceDetails(String srvName, String userName, String domainName, String url) throws InterruptedException
        {
            boolean success = false;

            Thread.sleep(1_000);
            //input[contains(@name,'editableInput')][@value='*']
            String xP = "//input[contains(@name,'editableInput')][@value='" + srvName + "']";
            WebElement field = driver.findElement(By.xpath(xP));
            field.click();
            field.clear();

            Thread.sleep(1_000);
            field.sendKeys(srvName);
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            this.clickApplyButton();
            Thread.sleep(1_000);
            nameColumnTitle.click();
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            String displayedServName = driver.switchTo().activeElement().getText();
            System.out.println(displayedServName);

            if (srvName.equals(displayedServName)) { driver.switchTo().activeElement().click(); }

            xP = "//td[contains(.,'" + url + "')]";
            String actURL = driver.findElement(By.xpath(xP)).getText();
            System.out.println("chooseANDcheckService.actURL is " + actURL);

            xP = "//td[contains(.,'" + userName + "@" + domainName + "')]";
            String actUserName = driver.findElement(By.xpath(xP)).getText();
            System.out.println("chooseANDcheckService.actUserName is " + actUserName);

            if (actUserName.equals(userName + "@" + domainName) && actURL.equals(url)) success = true;
            System.out.println("chooseANDcheckService.success is " + success);

            AllServicesButton.click();

            return success;
        }

        public void clickApplyButton() throws InterruptedException
        {
            applyButton.click();
            Thread.sleep(1_000);
        }

        public void clickAllServices()
        {
            AllServicesButton.click();
            System.out.println("ServiceDashboard : All services button was clicked");
        }

        /**
         * Click by serviceName
         * @param serviceName may be JS Service or REST service
         */
        public void clickByService(String serviceName)
        {
            ((JavascriptExecutor) driver).executeScript("$('#serviceDashboard\\\\:serviceDashboardTable_data td:contains(\"" + serviceName + "\")').find(\"a\").click()");
            System.out.println("ServiceDashboard: was clicked by " + serviceName);
        }

        /**
         * Click Open OpenAPI Specification button for previously selected service
         */
        public void openAPISpecification()
        {
            ((JavascriptExecutor) driver).executeScript("$('#serviceDashboard\\\\:serviceDashboardInstancesTable_data td:nth(4)').find(\"button\")[0].click()");
            System.out.println("Open OpenAPI Specification was clicked");
        }

        public DownloadServiceClientLibrary clickDownloadServiceClientLibrary()
        {
            ((JavascriptExecutor) driver).executeScript("$('#serviceDashboard\\\\:serviceDashboardInstancesTable_data td:nth(4)').find(\"button\")[1].click()");
            System.out.println("Download service client library was clicked");

            return new DownloadServiceClientLibrary(driver);
        }

        public void clickCloseOpenAPISpecification()
        {
            closeOpenAPISpecificationButton.click();
            System.out.println("ServiceDashboard : CloseOpenAPISpecification button was clicked");
        }
}
