package tests.source;

import net.portal.constants.Const;
import net.portal.constants.Notifications;
import net.portal.forms.DeleteUI;
import net.portal.pages.HeaderMenu;
import net.portal.pages.service_management.ServiceCatalog;
import net.portal.pages.service_management.UICatalog;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

import java.sql.Timestamp;
import java.io.*;
import java.text.SimpleDateFormat;

import static tests.source.FunctionalTest.driver;

public class TestUICatalog {

    static final SimpleDateFormat df = new SimpleDateFormat("MM.dd.HH.mm.ss");
    Timestamp timeMDHMS = new Timestamp(System.currentTimeMillis());
    String mdhms = df.format(timeMDHMS);
    String tmpstp = mdhms.substring(2).replaceAll("[-+.^:,]","");

    String tstUIname = "aUIapp" + tmpstp;

    boolean uploadUI = false; //true means including upload UI icon from PC - it need windows operations (not only Chrome actions), you should not operate anything on PC in case of "true"

    @Test
    public void TestUICatalog() throws InterruptedException {

        System.out.println("tstUIname = " + tstUIname);

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());
        driver.navigate().refresh();
        Thread.sleep(5_000);
        UICatalog uiCtlgPage = headerMenu.clickUICatalog();

        Thread.sleep(1_000);
        uiCtlgPage.createNewEmptyUI(tstUIname);
        uiCtlgPage.clickRefreshUIlist();
        Thread.sleep(2_000);
        headerMenu.clickCloseMenu();
        Thread.sleep(2_000);

        uiCtlgPage.clickEditUIname(tstUIname);

        String[] temps = uiCtlgPage.editUIbyFrame(uploadUI); //true means including upload UI icon from PC - it need windows operations (not only Chrome actions), you should not operate anything on PC in case of "true"
        String dialogNameBefore = temps[0];
        String iconFileNameBefore = temps[1];

        uiCtlgPage.clickEditUIname(tstUIname);
        boolean success = uiCtlgPage.checkUIbyFrame(dialogNameBefore, iconFileNameBefore, uploadUI); //true means checking (uploaded from PC) UI icon name
        Assert.assertEquals(true,success);

        headerMenu.clickCloseMenu();
        Thread.sleep(2_000);

        uiCtlgPage.checkCreateExistUI(tstUIname);

        Thread.sleep(5_000);
        uiCtlgPage.filterUIname(tstUIname);
        Thread.sleep(1_000);
        DeleteUI popDel = uiCtlgPage.clickFirstDeleButton();
        Thread.sleep(2_000);
        popDel.clickYesButton();
        Thread.sleep(3_000);
    }
}
