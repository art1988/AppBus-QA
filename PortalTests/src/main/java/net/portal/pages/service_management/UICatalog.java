package net.portal.pages.service_management;

import com.sun.jdi.Type;
import net.portal.constants.Notifications;
import net.portal.forms.*;

import java.lang.String;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import net.portal.pages.PageObject;
import org.junit.Assert;
import org.openqa.selenium.*;
import org.openqa.selenium.support.ByIdOrName;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.awt.*;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.StringSelection;
import java.awt.event.KeyEvent;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.util.Set;

import static junit.framework.Assert.assertNotSame;

//import static com.sun.org.apache.xml.internal.serialize.LineSeparator.Windows;

public class UICatalog  extends PageObject
{
    static final SimpleDateFormat sdf = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss");
    Timestamp timestp = new Timestamp(System.currentTimeMillis());
    String tmstp = sdf.format(timestp);
    String time = tmstp.substring(5).replaceAll("[-+.^:,]","");

    @FindBy(id = "uiCatalogForm:addUiButton")
    private WebElement createUIButton;

    @FindBy(id = "uiCatalogForm:uiCatalogTable:0:deleteAppButton")
    private WebElement theFirstDeleteButton;

    @FindBy(id = "//span[contains(@class,'ui-button-text ui-c')][contains(.,'Refresh')]")
    private WebElement refreshButton;

    @FindBy(xpath = "//span[contains(.,'Service Management > UI Catalog')]") //you can click uiPanelTitle, then "TAB" to get "Close editor" button
    private WebElement uiPanelTitle;

    @FindBy(xpath = "//a[contains(.,'Create Script')]")
    private WebElement createScriptButton;

    @FindBy(id = "uiCatalogForm:closeEditorButton") //button[contains(@id,'uiCatalogForm:closeEditorButton')][contains(.,'Close editor')]
    private WebElement closeEditorButton;

    @FindBy(xpath = "//*[@class='ui-toolbar-group-right']")
    private WebElement filterLabel; //you can click this, then key TAB - active element is filter filed

    @FindBy(xpath = "//*[text()='Apply']")
    private WebElement applyButton;

    @FindBy(xpath = "//span[@class='project-tree-item-name'][contains(.,'Custom components')]")
    private WebElement customComponentsItem;

    @FindBy(className = "laucnher-logo")
    private WebElement launcherLogo;

    @FindBy(xpath = "//div[contains(@class,'qq-upload-button btn btn-primary btn-block')][contains(.,'Select files...')]")
    private WebElement frameSelectFilesButton;

    @FindBy(xpath = "//a[contains(@data-tiggzi-action,'changeFavicon')]")
    private WebElement frameChangeIconButton;

    @FindBy(xpath = "//a[contains(@data-tiggzi-action,'toggleUploadPanel')]")
    private WebElement frameUploadFileButton;

    @FindBy(xpath = "//a[contains(@class,'btn btn-primary')][contains(.,'Back to images list')]")
    private WebElement frameBackImageListButton;

    @FindBy(xpath = "//h3[contains(.,'Media Manager')]")
    private WebElement frameMediaManagerHead;

    @FindBy(xpath = "//a[contains(@data-tiggzi-action,'select')][contains(.,'Apply')]")
    private WebElement frameApplyButton;

    @FindBy(xpath = "//span[contains(@id,'faviconTxt')][contains(.,'Name:')]")
    private WebElement frameIconNameLabel;

    @FindBy(xpath = "//a[contains(@id,'btn-create-new')][contains(.,'Create New')]")
    private WebElement frameCreteNewElemButton;

    @FindBy(xpath = "//a[contains(@class,'cnb-item')][contains(.,'TypeScript')]")
    private WebElement frameTypeScriptItemOfCrNew;

    @FindBy(xpath = "//a[contains(@class,'cnb-item')][contains(.,'Enter name:')]")
    private WebElement frameEnterNameLabelOfCrNewDialog;

    @FindBy(xpath = "//a[contains(@data-affect,'create-screen')][contains(.,'Create Dialog')]")
    private WebElement frameCreateDialogButton;

    @FindBy(xpath = "//a[contains(.,'Save')]") //a[contains(@data-tiggzi-action,'save')][contains(.,'Saving...')]
    private WebElement frameSaveUIButton;

    @FindBy(xpath = "//div[contains(@id,'addAppDlg')]")
    private WebElement createUIpopDialog;

    @FindBy(xpath = "//a[contains(@class,'ui-dialog-titlebar-icon ui-dialog-titlebar-close ui-corner-all')]")
    private WebElement closeUIpopDialogButton;

    @FindBy(xpath = "//input[@placeholder='type the js name here']")
    private WebElement scriptNameInput;

    public UICatalog(WebDriver driver)
    {
        super(driver);
        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( driver.findElement(By.className("ui-panel-title")).getText().equals("Service Management > UI Catalog") );
    }

    public void createNewEmptyUI(String uiName) throws InterruptedException
    {
        clickCreateUI();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().clear();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(uiName);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(3_000);
        //WebDriverWait wait_iframe = new WebDriverWait(driver, 40);
        //wait_iframe.until(ExpectedConditions.elementToBeClickable(frameCreteNewElemButton));

        uiPanelTitle.click();
        //closeEditorButton.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(3_000);

    }

    public void clickCreateUI()
    {
        createUIButton.click();
        System.out.println("ServiceCatalog : Create UI button was clicked");
    }

    public void setScriptName(String scriptName) throws InterruptedException
    {
        scriptNameInput.clear();
        Thread.sleep(1_000);
        scriptNameInput.sendKeys(scriptName);
        Thread.sleep(1_000);
        System.out.println("ServiceCatalog : scriptName was set");
    }

    public DeleteUI clickFirstDeleButton()
    {
        theFirstDeleteButton.click();
        System.out.println("ServiceCatalog : Delete UI button was clicked");

        return new DeleteUI(driver);
    }

    public void clickRefreshUIlist() throws InterruptedException
    {
        //refreshButton.submit();
        Thread.sleep(3_000);
        uiPanelTitle.click();
        System.out.println("ServiceCatalog : uiPanelTitle's just been clicked");
        //closeEditorButton.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);
        System.out.println("ServiceCatalog : Refresh UI list button was clicked");
    }

    public void checkCreateExistUI(String uiName) throws InterruptedException
    {
        clickCreateUI();
        Thread.sleep(1_000);
        WebElement uiNameField = createUIpopDialog.findElement(By.xpath("//input[contains(@type,'text')]"));
        Thread.sleep(1_000);
        //uiNameField.click();
        driver.switchTo().activeElement().clear();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(uiName);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);

        WebElement notificationPopup = (new WebDriverWait(driver, 2)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.UI_TITLE_ALREADY_EXISTS.getNotificationText(), notificationPopup.getText());

        Thread.sleep(5_000);
        //closeUIpopDialogButton.click();
        WebElement uiCloseButton = createUIpopDialog.findElement(By.xpath("//a[contains(@class,'ui-dialog-titlebar-icon ui-dialog-titlebar-close ui-corner-all')]"));
        uiCloseButton.submit();
    }

    public void filterUIname(String uiName) throws InterruptedException
    {

        filterLabel.findElement(By.xpath("//*[@class='ui-toolbar-group-right']/input[@type='text']")).clear();
        //filterLabel.findElement(By.xpath("//*[@class='ui-toolbar-group-right']/input[@type='text']")).click();
        Thread.sleep(1_000);
        //driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(uiName);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        applyButton.click();
        Thread.sleep(1_000);
        System.out.println("UICatalog : just filtered the following UI:" + uiName);
    }

    public void clickCreateScript() throws InterruptedException
    {
        createScriptButton.click();
        Thread.sleep(1_000);
        System.out.println("UICatalog : Create Script button was clicked");
    }

    public void clickEditUIname(String uiName) throws InterruptedException
    {
        filterUIname(uiName);
        Thread.sleep(1_000);
        driver.findElement(By.xpath("//*[text()='" + uiName + "']")).click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        boolean rightIcon = driver.switchTo().activeElement().getText().contains("Open UI editor");
        if (rightIcon) {
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.SPACE);
            System.out.println("UICatalog.clickEditUIname(): just clicked the Edit button");
            Thread.sleep(3_000);
        }

    }

    public void getFileTypeElement() throws InterruptedException
    {
        for (int i=0; i < 30; i++) {
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            String type = driver.switchTo().activeElement().getAttribute("Type");
            System.out.println("type = " + type);

            if (type.equals("file")) { System.out.println("type at break = " + type); break; }

        }
    }

    public String[] editUIbyFrame(boolean uploadIcon) throws InterruptedException
    {
        String IconFile = "";
        String dialogName = "tstDialog";
        dialogName = dialogName + time;

        System.out.println("createUIbyFrame: I started my work");
        JavascriptExecutor js = (JavascriptExecutor)driver;

        WebDriverWait wait_iframe = new WebDriverWait(driver, 40);
        //wait_iframe.until(ExpectedConditions.visibilityOfElementLocated((By.xpath("//span[contains(@data-sat-asset-name,'JavaScript')]"))));
        wait_iframe.until(ExpectedConditions.elementToBeClickable(By.id("uiEditor")));

        System.out.println("createUIbyFrame: I got the uiEditor");
        Thread.sleep(3_000);
        //wait_iframe.until(ExpectedConditions.elementToBeClickable(By.xpath("//span[contains(@data-sat-asset-name,'Project')]")));

        //driver.switchTo().frame("uiEditor").switchTo().activeElement().isEnabled();


        for (int i=0; i < 50; ) {
            try {
                WebElement leftCol = driver.findElement(By.id("project-inspector"));
                leftCol.findElement(By.xpath("//span[contains(@data-sat-asset-name,'Project')]")).click(); //button[contains(.,'Project')]
                i = 500;
                System.out.println("i from the first try = " + i);
                break;
            } catch (Exception e) { i++; System.out.println("i from the first Exception = " + i); } //e.printStackTrace();

            try {
                driver.switchTo().frame("uiEditor").findElement(By.xpath("//span[contains(@data-sat-asset-name,'Project')]")).click();
                i = 500;
                System.out.println("i from the second try = " + i);
                break;
            } catch (Exception e) { i++; System.out.println("i from the second Exception = " + i); } //e.printStackTrace();
        }

        if(uploadIcon) {
            driver.findElement(By.xpath("//span[contains(@data-sat-asset-name,'App settings')]")).click();
            frameChangeIconButton.click();
            //driver.findElement(By.xpath("//a[contains(@data-tiggzi-action,'changeFavicon')]")).click();
            Thread.sleep(1_000);
            frameUploadFileButton.click();
            //driver.findElement(By.xpath("//a[contains(@data-tiggzi-action,'toggleUploadPanel')]")).click();
            Thread.sleep(1_000);
            frameSelectFilesButton.click();


            try {

                StringSelection path = new StringSelection("C:\\Windows\\Web\\Screen");
                Toolkit tol = Toolkit.getDefaultToolkit();
                Clipboard c = tol.getSystemClipboard();
                // copy the path into mouse
                c.setContents(path, null);
                // create a object of robot class
                Robot robot = new Robot();
                System.out.println("UICatalog: Robot's just been initialized");
                robot.delay(5_000);
                robot.keyPress(KeyEvent.VK_CONTROL);
                robot.delay(50);
                robot.keyPress(KeyEvent.VK_V);
                robot.delay(50);
                robot.keyRelease(KeyEvent.VK_CONTROL);
                robot.delay(50);
                robot.keyRelease(KeyEvent.VK_V);
                System.out.println("UICatalog: Robot just put the file path ");
                robot.delay(50);
                robot.keyPress(KeyEvent.VK_ENTER);
                robot.delay(50);
                robot.keyRelease(KeyEvent.VK_ENTER);
                robot.delay(500);
                robot.keyPress(KeyEvent.VK_SHIFT);
                robot.delay(50);
                robot.keyPress(KeyEvent.VK_TAB);
                robot.delay(50);
                robot.keyRelease(KeyEvent.VK_TAB);
                robot.delay(50);
                robot.keyRelease(KeyEvent.VK_SHIFT);
                robot.delay(500);
                robot.keyPress(KeyEvent.VK_SPACE);
                robot.delay(50);
                robot.keyRelease(KeyEvent.VK_SPACE);
                robot.delay(50);
                //robot.keyPress(KeyEvent.VK_TAB);
                robot.delay(50);
                //robot.keyRelease(KeyEvent.VK_TAB);
                robot.delay(50);
                //robot.keyPress(KeyEvent.VK_TAB);
                robot.delay(50);
                //robot.keyRelease(KeyEvent.VK_TAB);
                robot.delay(50);
                //robot.keyPress(KeyEvent.VK_TAB);
                robot.delay(50);
                //robot.keyRelease(KeyEvent.VK_TAB);
                robot.delay(500);

                String pict = driver.switchTo().activeElement().getAttribute("Type");
                System.out.println("pict = " + pict);

                if (!pict.equals("file")) getFileTypeElement();

                robot.keyPress(KeyEvent.VK_SPACE);
                robot.keyRelease(KeyEvent.VK_SPACE);

                robot.delay(1000);
                robot.keyPress(KeyEvent.VK_ENTER);
                robot.delay(500);
                robot.keyRelease(KeyEvent.VK_ENTER);
                robot.delay(2000);


            } catch (AWTException e) {
                e.printStackTrace();
            }

            Thread.sleep(1_000);
            try {
                wait_iframe.until(ExpectedConditions.elementToBeClickable(By.xpath("//span[contains(@class,'qq-upload-fail label label-success')][contains(.,'completed')]")));
            } catch (Exception e) {Thread.sleep(10_000); System.out.println("Wait_iframe.until doesn't work !");}

            frameBackImageListButton.click();
            Thread.sleep(1_000);
            frameMediaManagerHead.click();
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);

            driver.switchTo().activeElement().sendKeys(Keys.TAB);
            Thread.sleep(1_000);
            driver.switchTo().activeElement().sendKeys(Keys.SPACE);
            Thread.sleep(1_000);
            driver.switchTo().activeElement().click();
            Thread.sleep(5_000);
            wait_iframe.until(ExpectedConditions.elementToBeClickable(frameApplyButton));
            frameApplyButton.click();

//end of adding icon to UI app
//Start adding autoSCRIPT to UI app

            Thread.sleep(1_000);
            wait_iframe.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//span[contains(@id,'faviconTxt')][contains(.,'Name:')]")));
            IconFile = frameIconNameLabel.getText();
            IconFile = IconFile.substring(6);
            System.out.println("IconFile name is " + IconFile);
        }
        Thread.sleep(1_000);
        frameCreteNewElemButton.click();
        Thread.sleep(1_000);
        frameTypeScriptItemOfCrNew.click();
        Thread.sleep(1_000);
        setScriptName("autoSCRIPT");
        Thread.sleep(1_000);
        createScriptButton.click();
        Thread.sleep(2_000);

        try {
            driver.findElement(By.xpath("//button[contains(.,'Ok')]")).click();
            System.out.println("Error of SCRIPT creating");
        }
        catch (Exception e) {}

        Thread.sleep(2_000);
        driver.findElement(By.xpath("//span[contains(@data-sat-asset-name,'autoSCRIPT')]")).click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        System.out.println("Going to type a comment...");
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys("\n");
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys("//edited script");
        Thread.sleep(1_000);
//end of creating autoSCRIPT page

        Thread.sleep(1_000);
        frameSaveUIButton.click();
        Thread.sleep(2_000);

        try {
            driver.findElement(By.xpath("//button[contains(.,'Ok')]")).click();
            System.out.println("Error of SCRIPT creating");
        }
        catch (Exception e) {}
        Thread.sleep(2_000);

        driver.findElement(By.xpath("//span[contains(@data-sat-asset-name,'Model')]")).click();
        Thread.sleep(1_000);
        driver.findElement(By.xpath("//span[contains(@data-sat-asset-name,'autoSCRIPT')]")).click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        System.out.println("Going to type one more comment...");
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.BACK_SPACE);
        Thread.sleep(1_000);
        driver.findElement(By.xpath("//span[contains(@data-sat-asset-name,'Model')]")).click();
        Thread.sleep(1_000);

        Thread.sleep(1_000);
        frameSaveUIButton.click();
        Thread.sleep(2_000);

        try {
            driver.findElement(By.xpath("//button[contains(.,'Ok')]")).click();
            System.out.println("Error of SCRIPT creating");
        }
        catch (Exception e) {}
        Thread.sleep(2_000);

        System.out.println("frame handler finished its work");

//switch from frame to window back

        String window1 = driver.getWindowHandle(); // driver.switch_to.window(driver.window_handles[1])
        Thread.sleep(1_000);
        System.out.println("windowCurrent is " + window1);
        Thread.sleep(1_000);
        Set<String> winHandles = driver.getWindowHandles();
        Thread.sleep(1_000);
        String winHandle1 = winHandles.iterator().next();
        Thread.sleep(1_000);
        Object[] winHandleObj = winHandles.toArray();
        Thread.sleep(1_000);
        String winHandle2 = winHandleObj[0].toString();
        Thread.sleep(1_000);
        driver.switchTo().window(winHandle1);
        Thread.sleep(1_000);
        System.out.println("winHandleObj.length is " + winHandleObj.length);

//end of switch
        System.out.println("Window " + window1 + " : I'm back to WebDriver control");



        //uiPanelTitle.click();
        ((JavascriptExecutor) driver).executeScript("$($('#uiCatalogForm\\\\:actionsPanel')).find(\"#uiCatalogForm\\\\:closeEditorButton\").click()");
        //(JavascriptExecutor) FunctionalTest.getDriver()).executeScript("$('.closeEditorButton').click()");
        Thread.sleep(1_000);
        //driver.switchTo().activeElement().sendKeys(Keys.TAB);
        //Thread.sleep(1_000);
        //driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);


        Thread.sleep(3_000);

        String[] rtns = {dialogName,IconFile};

        return (rtns);

        /*

        System.out.println("_______________________________________________________________________________________________________________________________________");
        String aFrame1 = driver.switchTo().frame(0).getPageSource().toString();
        System.out.println(aFrame1);
        System.out.println("_______________________________________________________________________________________________________________________________________");
        String aFrame2 = driver.switchTo().activeElement().getText();
        System.out.println(aFrame2);
        System.out.println("_______________________________________________________________________________________________________________________________________");
        String aFrame0 = driver.switchTo().frame("uiEditor").getPageSource().toString();
        System.out.println(aFrame0);
        */

    }

    public boolean checkUIbyFrame(String dialogName, String IconFile, boolean checkIconName) throws InterruptedException
    {
        String IconFileNameAfter = "";
        boolean testPass = true;

        System.out.println("checkUIbyFrame started its work");
        //JavascriptExecutor js = (JavascriptExecutor)driver;

        WebDriverWait wait_iframe = new WebDriverWait(driver, 40);
        //wait_iframe.until(ExpectedConditions.visibilityOfElementLocated((By.xpath("//span[contains(@data-sat-asset-name,'JavaScript')]"))));
        wait_iframe.until(ExpectedConditions.elementToBeClickable(By.id("uiEditor")));

        System.out.println("checkUIbyFrame got the uiEditor frame");
        Thread.sleep(3_000);
        driver.switchTo().frame("uiEditor").findElement(By.xpath("//span[contains(@data-sat-asset-name,'Project')]")).click();
        Thread.sleep(1_000);
        driver.findElement(By.xpath("//span[contains(@data-sat-asset-name,'Project')]")).click();
        Thread.sleep(1_000);
        driver.findElement(By.xpath("//span[contains(@data-sat-asset-name,'App settings')]")).click();
        Thread.sleep(1_000);

//switch from frame to window back

        String window0 = driver.getWindowHandle(); // driver.switch_to.window(driver.window_handles[1])
        Thread.sleep(1_000);
        System.out.println("windowCurrent is " + window0);
        Thread.sleep(1_000);
        Set<String> winHandles0 = driver.getWindowHandles();
        Thread.sleep(1_000);
        String winHandle2 = winHandles0.iterator().next();
        Thread.sleep(1_000);
        Object[] winHandleObj0 = winHandles0.toArray();
        Thread.sleep(1_000);
        driver.switchTo().window(winHandle2);
        Thread.sleep(1_000);
        System.out.println("winHandleObj.length is " + winHandleObj0.length);
//end of switch
        System.out.println("Window " + window0+ " : I'm back to WebDriver control");

        JavascriptExecutor js = (JavascriptExecutor)driver;
        //! ((JavascriptExecutor)driver).executeScript("$($('[id=\"uiEditor\"]')[0].contentDocument).find(\"a:contains('Resources')\")[0].click()"); //!
        js.executeScript("$($('[id=\"uiEditor\"]')[0].contentDocument).find(\"a:contains('Resources')\")[0].click()"); //!
        //! driver.findElement(By.xpath("//a[@data-tab-name='resources']")).click(); //!
        Thread.sleep(1_000);
        driver.switchTo().frame("uiEditor").findElement(By.xpath("//option[contains(.,'Ionic (4.0)')]")).click();
        //driver.findElement(By.xpath("//option[contains(.,'Ionic (4.0)')]")).click();
        System.out.println("Good! Ionic 4.0 has been found'");
        Thread.sleep(1_000);
        driver.findElement(By.xpath("//span[contains(@data-sat-asset-name,'Project')]")).click();
        Thread.sleep(1_000);
        driver.findElement(By.xpath("//span[contains(@data-sat-asset-name,'autoSCRIPT')]")).click();
        Thread.sleep(1_000);
        String edS = driver.findElement(By.xpath("//div[contains(@class,'ace_layer ace_text-layer')]")).getAttribute("innerHTML");
        Thread.sleep(1_000);
        //!        if (!edS.contains("AutoSCRIPT")) //!
        if (!edS.contains("AutoSCRIPT") || !edS.contains("//edited script")) //!
        {
            testPass = false; System.out.println("testPass = false, I haven't found \"//edited script\" row");
        }
        Thread.sleep(1_000);
        driver.findElement(By.xpath("//span[contains(@data-sat-asset-name,'Project')]")).click();
        Thread.sleep(1_000);
        driver.findElement(By.xpath("//span[contains(@data-sat-asset-name,'App settings')]")).click();
        Thread.sleep(1_000);


        if(checkIconName) {
//            wait_iframe.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//span[contains(@data-sat-asset-name,'App settings')]")));
            driver.findElement(By.xpath("//span[contains(@data-sat-asset-name,'App settings')]")).click();

            //getting IconFileName

            Thread.sleep(1_000);
            wait_iframe.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//span[contains(@id,'faviconTxt')][contains(.,'Name:')]")));
            IconFileNameAfter = frameIconNameLabel.getText();
            IconFileNameAfter = IconFileNameAfter.substring(6);
            System.out.println("IconFileNameAfter name is " + IconFileNameAfter);

            if (!IconFileNameAfter.equals(IconFile) && checkIconName) {testPass = false;}
        }

        driver.findElement(By.xpath("//button[@data-target='#sources_tree']")).click();
        Thread.sleep(1_000);
        driver.findElement(By.xpath("//span[@class='project-tree-item-name'][contains(.,'IONIC')]")).click();
        Thread.sleep(2_000);
        driver.findElement(By.xpath("//span[@class='project-tree-item-name'][contains(.,'package.json')]")).click();
        Thread.sleep(2_000);
        String packageJSON = driver.findElement(By.xpath("//div/div/span[contains(.,'\"@ionic/angular\"')]/..")).getAttribute("outerHTML");
        Thread.sleep(1_000);

        System.out.println("__________________________________");
        System.out.println(packageJSON);
        System.out.println("__________________________________");

        if (!packageJSON.contains("@ionic/angular") || !packageJSON.contains("^4.0.0"))
        {
            testPass = false; System.out.println("testPass = false, I haven't found \"@ionic/angular\": \"^4.0.0\" row");
        }

//switch from frame to window back

        String window1 = driver.getWindowHandle(); // driver.switch_to.window(driver.window_handles[1])
        Thread.sleep(1_000);
        System.out.println("windowCurrent is " + window1);
        Thread.sleep(1_000);
        Set<String> winHandles = driver.getWindowHandles();
        Thread.sleep(1_000);
        String winHandle1 = winHandles.iterator().next();
        Thread.sleep(1_000);
        Object[] winHandleObj = winHandles.toArray();
        Thread.sleep(1_000);
        driver.switchTo().window(winHandle1);
        Thread.sleep(1_000);
        System.out.println("winHandleObj.length is " + winHandleObj.length);
        //end of switch
        System.out.println("Window " + window1 + " : I'm back to WebDriver control");

        uiPanelTitle.click();
        //closeEditorButton.click();
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.TAB);
        Thread.sleep(1_000);
        driver.switchTo().activeElement().sendKeys(Keys.SPACE);
        Thread.sleep(1_000);

        return (testPass);

    }

}
