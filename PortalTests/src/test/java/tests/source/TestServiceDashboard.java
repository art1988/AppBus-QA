package tests.source;

import net.portal.forms.*;
import org.openqa.selenium.*;
import net.portal.constants.Notifications;
import net.portal.pages.HeaderMenu;
import net.portal.pages.portal_administration.Users;
import net.portal.pages.service_management.ServiceCatalog;
import net.portal.pages.service_management.ServiceDashboard;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.sql.Timestamp;
import java.text.SimpleDateFormat;

import static tests.source.FunctionalTest.driver;


public class TestServiceDashboard  {

    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");
    Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
    String mdhms = df.format(timeMDHMS);
    String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

    String projectName = "autoPRG" + tmpstp;
    String jsSrvcName1 = "JSsrv1AUTO" + tmpstp.substring(3);
    String jsSrvcName2 = "JSsrv2AUTO" + tmpstp.substring(3);
    String jsSrvcName3 = "EXres3AUTO" + tmpstp.substring(3);
    String[] jsSrvcName = {jsSrvcName1,jsSrvcName2,jsSrvcName3};
    //z String[] jsSrvcName = {"JSsrv2AUTO04717","EXres3AUTO04717","JSsrv1AUTO04717"};


    String[] tempX = {"//input[contains(@value,'Last name of the autoUser1')]","//input[contains(@value,'Last name of the autoUser2')]","//input[contains(@value,'Last name of the autoUser3')]"};

    @Test
    public void TestServiceDashboard() throws InterruptedException {

        //z String projectName = "autoPRG03104717";
        System.out.println("projectName = " + projectName);
        System.out.println("jsSrvcName1 = " + jsSrvcName1);
        System.out.println("jsSrvcName2 = " + jsSrvcName2);
        System.out.println("jsSrvcName3 = " + jsSrvcName3);

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());
        driver.navigate().refresh();
        Thread.sleep(5_000);
//Create unique name User, without UG (start)

        Users usersPage = headerMenu.clickUsers();

// Add 3 new users
        for(int i = 1; i < 4; i++)
        {
            UserDetail userDetailForm = usersPage.addNewUser();

            Thread.sleep(2_000);

            String temp = "autoUser" + i + tmpstp.substring(4);

            userDetailForm.setUserName("autoUser" + i + tmpstp.substring(4));
            userDetailForm.setFirstName("First name of the " + temp);
            userDetailForm.setLastName("Last name of the autoUser" + i);

            userDetailForm.clickAdd();

            Thread.sleep(6_000);

            usersPage.searchForUserNameByXpath(temp); //you can use searchForUserName() after fixing of the ED-3965
            Thread.sleep(1_000);

            usersPage = headerMenu.clickUsers();
            Thread.sleep(3_000);
            usersPage.searchForUserName(temp);
            Thread.sleep(1_000);


            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            usersPage.editUserButton();
            //System.out.println("Users : just clicked the EDIT button");
            Thread.sleep(1_000);

            usersPage.clickElementByXpath((String)tempX[i-1]); //input[contains(@value,'Last name of the autoUser1')]"

            Thread.sleep(2_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(2_000);
            driver.switchTo().activeElement().sendKeys(Keys.ENTER);
            Thread.sleep(1_000);

            Thread.sleep(1_000);

            System.out.println("Users : going to enter User groups...");
            Thread.sleep(2_000);
            usersPage.clickUniqueNameItem(); //9
            Thread.sleep(2_000);
            usersPage.clickElementByXpath((String)tempX[i-1]); //input[contains(@value,'Last name of the autoUser1')]"
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.SPACE);
            Thread.sleep(1_000);
        }


//Create unique name User, without UG (finish)

//Create a Project (start)
        ServiceCatalog serviceCtlgPage = headerMenu.clickServiceCatalog();

        CreateProject createPrjctPop = serviceCtlgPage.clickCreateProject();
        Thread.sleep(3_000);

        createPrjctPop.setName(projectName);
        createPrjctPop.clickSave();
        Thread.sleep(3_000);
        serviceCtlgPage = headerMenu.clickServiceCatalog();
        Thread.sleep(1_000);
        serviceCtlgPage.selectProject(projectName);
        Thread.sleep(1_000);
//Create a Project (finish)

        serviceCtlgPage.selectServices();
        Thread.sleep(1_000);

 //Create Service #1 (start)

        CreateService createService = serviceCtlgPage.clickCreateService();
        Thread.sleep(2_000);

        createService.selectType("JS service");
        createService.clickNext();

        //switch to frame, then to window back (start)
        String wndw = driver.getWindowHandle();

        WebDriverWait wait_iframe = new WebDriverWait(driver, 30);
        //wait_iframe.until(ExpectedConditions.visibilityOfElementLocated((By.xpath("//span[contains(@data-sat-asset-name,'JavaScript')]"))));
        wait_iframe.until(ExpectedConditions.elementToBeClickable(By.id("serverCodeScriptEditor")));

        for (int i=0; i<50;) {
            try {
                driver.switchTo().frame("serverCodeScriptEditor").findElement(By.xpath("//span[contains(@class,'ace_fold-widget ace_start ace')]")).click();
                System.out.println("editor is working on A try №" + i);
                Thread.sleep(1_000);
                driver.findElement(By.xpath("//span[contains(@class,'ace_fold-widget ace_start ace')]")).click();
                System.out.println("editor is working on B try №" + i);
                break;
            } catch (Exception e) { System.out.println("editor is NO working on try №" + i);
                i++;
            }
        }
        driver.switchTo().window(wndw);
        //switch to frame, then to window back (finish)
        Thread.sleep(1_000);

        driver.switchTo().frame("serverCodeScriptEditor").findElement(By.xpath("//input[@name='scriptName']")).sendKeys(jsSrvcName1);
        Thread.sleep(1_000);

        //serviceCtlgPage.setName(jsSrvcName1, "serverCodeScriptEditor");

        Thread.sleep(1_000);
        //serviceCtlgPage.clickScriptParametersTab();
        driver.findElement(By.xpath("//a[contains(.,'Script parameters')]")).click();

        Thread.sleep(1_000);
        driver.findElement(By.xpath("//span[@class='selecter-selected'][contains(.,'POST')]")).click();

        Thread.sleep(1_000);
        driver.findElement(By.xpath("//span[@data-value='GET']")).click();
        Thread.sleep(1_000);
        //String temp = driver.switchTo().activeElement().getText();
        //System.out.println("Selected script method is " + temp);

        //serviceCtlgPage.setRequestMethod("GET");

        Thread.sleep(1_000);
        driver.findElement(By.xpath("//input[@name='paramName']")).sendKeys("devName");
        //serviceCtlgPage.setParamName("devName");
        Thread.sleep(1_000);

        Thread.sleep(1_000);
        driver.findElement(By.xpath("//button[@id='add']")).click();
        //serviceCtlgPage.clickAddParamButton();
        Thread.sleep(1_000);

        Thread.sleep(1_000);
        driver.findElement(By.xpath("//input[@data-param-type='value']")).sendKeys("AUTO" + tmpstp.substring(6));
        //serviceCtlgPage.setParamValue("devName", "AUTO" + tmpstp.substring(6));
        Thread.sleep(1_000);

        driver.findElement(By.xpath("//a[contains(.,'Run')]")).click();
        String temp = driver.switchTo().activeElement().getText();
        System.out.println("Current active element is " + temp);
        //serviceCtlgPage.clickRunTab();

        //Thread.sleep(1_000);
        //driver.findElement(By.xpath("(//button[contains(.,'Save')])[1]")).click();
        //serviceCtlgPage.clickSave("serverCodeScriptEditor"); // Need to Save first because hitting by 'Save and Run' doesn't work (Appery issue)
        //Thread.sleep(2_000);

        driver.findElement(By.xpath("//button[@type='button'][contains(.,'Save and run')]")).click();
        //serviceCtlgPage.clickSaveAndRunButton();
        Thread.sleep(5_000);

        driver.switchTo().window(wndw);
        Thread.sleep(1_000);

        serviceCtlgPage.clickCloseEditor();
        Thread.sleep(5_000);

        System.out.println("Edit just created JS Service...");

        //Create service #1 (finish)
        //Create Service #2 (start):

        createService = serviceCtlgPage.clickCreateService();
        Thread.sleep(2_000);

        createService.selectType("JS service");
        Thread.sleep(2_000);
        createService.clickNext();
        Thread.sleep(1_000);

        //switch to frame, then to window back (start)
        wndw = driver.getWindowHandle();

        wait_iframe = new WebDriverWait(driver, 30);
        //wait_iframe.until(ExpectedConditions.visibilityOfElementLocated((By.xpath("//span[contains(@data-sat-asset-name,'JavaScript')]"))));
        wait_iframe.until(ExpectedConditions.elementToBeClickable(By.id("serverCodeScriptEditor")));

        for (int i=0; i<50;) {
            try {
                driver.switchTo().frame("serverCodeScriptEditor").findElement(By.xpath("//span[contains(@class,'ace_fold-widget ace_start ace')]")).click();
                System.out.println("editor is working on A try №" + i);
                Thread.sleep(1_000);
                driver.findElement(By.xpath("//span[contains(@class,'ace_fold-widget ace_start ace')]")).click();
                System.out.println("editor is working on B try №" + i);
                break;
            } catch (Exception e) { System.out.println("editor is NO working on try №" + i);
                i++;
            }
        }
        driver.switchTo().window(wndw);
        //switch to frame, then to window back (finish)
        //Thread.sleep(20_000);

        driver.switchTo().frame("serverCodeScriptEditor").findElement(By.xpath("//input[@name='scriptName']")).sendKeys(jsSrvcName2);
        //serviceCtlgPage.setName(jsSrvcName2, "serverCodeScriptEditor");
        Thread.sleep(1_000);


        //serviceCtlgPage.clickScriptParametersTab();
        driver.findElement(By.xpath("//a[contains(.,'Script parameters')]")).click();
        Thread.sleep(1_000);

        //serviceCtlgPage.setRequestMethod("POST");
        Thread.sleep(1_000);
        driver.findElement(By.xpath("//span[@class='selecter-selected'][contains(.,'POST')]")).click();
        Thread.sleep(1_000);
        driver.findElement(By.xpath("//span[@data-value='GET']")).click();
        Thread.sleep(1_000);

        temp = driver.findElement(By.xpath("//span[@class='selecter-selected']")).getText();
        System.out.println("Selected script method is " + temp);

        Thread.sleep(1_000);
        driver.findElement(By.xpath("//input[@name='paramName']")).sendKeys("mobile");
        //serviceCtlgPage.setParamName("mobile");
        Thread.sleep(1_000);

        //serviceCtlgPage.clickAddParamButton();
        driver.findElement(By.xpath("//button[@id='add']")).click();
        Thread.sleep(1_000);

        Thread.sleep(1_000);
        //serviceCtlgPage.setParamValue("mobile", "AUTO2" + tmpstp.substring(6));
        driver.findElement(By.xpath("//input[@data-param-type='value']")).sendKeys("AUTO2" + tmpstp.substring(6));
        Thread.sleep(1_000);

        //serviceCtlgPage.clickRunTab();
        driver.findElement(By.xpath("//a[contains(.,'Run')]")).click();

        driver.findElement(By.xpath("//button[@type='button'][contains(.,'Save and run')]")).click();
        //serviceCtlgPage.clickSaveAndRunButton();
        Thread.sleep(5_000);

        driver.switchTo().window(wndw);
        Thread.sleep(1_000);

        serviceCtlgPage.clickCloseEditor();
        Thread.sleep(5_000);

        System.out.println("Edit just created JS Service #2...");

//Create Service #2 (finish)

//Create Service #3 (start):

        createService = serviceCtlgPage.clickCreateService();
        Thread.sleep(1_000);

        createService.selectType("Existing REST service");
        //createService.clickNext();
        Thread.sleep(4_000);

        driver.findElement(By.xpath("//label[contains(.,'Existing REST service')]")).click();
        Thread.sleep(2_000);
        //driver.findElement(By.xpath("//label[contains(.,'Existing REST service')]")).click();
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        //driver.switchTo().activeElement().sendKeys(jsSrvcName3);
        //Thread.sleep(1_000);
        //driver.switchTo().activeElement().sendKeys(Keys.TAB);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);

        RegisterExistingService crSrNext = new RegisterExistingService(driver);

        //driver.switchTo().activeElement().sendKeys("start");
        crSrNext.setName(jsSrvcName3);
        Thread.sleep(1_000);
        crSrNext.setTriggerName("start");
        Thread.sleep(1_000);
        crSrNext.setDescription("this service is connected to unique User name");
        Thread.sleep(1_000);
        crSrNext.setGETmethod();
        Thread.sleep(1_000);
        crSrNext.clickAddInstance();
        Thread.sleep(2_000);
        crSrNext.setURLfirstField("https://demo.e-dapt.net:4440/");
        Thread.sleep(1_000);
        crSrNext.clickCheckOfTheFirstRow();
        Thread.sleep(2_000);
        crSrNext.setTheFirstUsernameField("autoUser3", "botf03.net");
        Thread.sleep(1_000);
        crSrNext.setConsumes("audio/basic");
        Thread.sleep(1_000);
        crSrNext.setOneProduces("HTML");
        Thread.sleep(1_000);

        crSrNext.setOneResponsesCode("200");
        Thread.sleep(1_000);

        crSrNext.clickSaveButton();
        Thread.sleep(2_000);

//Create Service #3 (finish)


        ServiceDashboard uiCtlgPage = headerMenu.clickServiceDashboard();
        Thread.sleep(1_000);
        uiCtlgPage.setProjectName(projectName);
        Thread.sleep(1_000);
        uiCtlgPage.clickApplyButton();
        boolean success = uiCtlgPage.checkServiceList(jsSrvcName);
        Assert.assertEquals(true,success);

        Thread.sleep(1_000);
        //z jsSrvcName3 = "EXres3AUTO04717";
        success = uiCtlgPage.chooseANDcheckService(jsSrvcName3);
        Assert.assertEquals(true,success);
        Thread.sleep(1_000);

        success = uiCtlgPage.chooseANDcheckServiceDetails(jsSrvcName3, "autoUser3", "botf03.net", "https://demo.e-dapt.net:4440/");
        Assert.assertEquals(true,success);
        Thread.sleep(1_000);

        //Delete the Project (start)

        serviceCtlgPage = headerMenu.clickServiceCatalog();
        Thread.sleep(1_000);
        serviceCtlgPage.selectProject(projectName);
        Thread.sleep(1_000);
        RemoveProject removeProjectPopup = serviceCtlgPage.clickRemoveProject();
        Thread.sleep(3_000);
        removeProjectPopup.clickYes();
        Thread.sleep(1_000);

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.PROJECT_WAS_REMOVED.getNotificationText(), notificationPopup.getText());

//Delete the Project (finish)

//Delete Users (start)

        usersPage = headerMenu.clickUsers();
        usersPage.searchForUserNameByXpath("autoUser"); //you can use searchForUserName() after fixing of the ED-3965
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        usersPage.selectkAllItems();

        Thread.sleep(1_000);
        driver.findElement(By.xpath("(//span[contains(.,'Delete')])[1]")).click();
        Thread.sleep(2_000);
        driver.findElement(By.xpath("//span[contains(.,'Delete Following Users')]")).click();
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);

        notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_DELETED.getNotificationText(), notificationPopup.getText());

        usersPage = headerMenu.clickUsers();
        Thread.sleep(5_000);

//Delete Users (finish)

    }
}
