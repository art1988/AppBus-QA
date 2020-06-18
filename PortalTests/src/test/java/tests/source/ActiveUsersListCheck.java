package tests.source;

import net.portal.constants.Const;
import net.portal.constants.Notifications;
import net.portal.pages.HeaderMenu;
import net.portal.pages.reporting.ActiveUsers;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;

import java.security.Timestamp;
import java.sql.*;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.*;
import java.util.Date;
import java.util.Set;
import java.util.TimeZone;

import static java.sql.Time.valueOf;
import static okhttp3.internal.Util.UTC;
import static org.apache.http.client.utils.DateUtils.GMT;
import static tests.source.FunctionalTest.driver;

public class ActiveUsersListCheck
{
    static final SimpleDateFormat df = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss zzz");
    static final SimpleDateFormat gf = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss zzz");
    static final SimpleDateFormat pitField = new SimpleDateFormat("MM/dd/yyyy HH:mm");

    @Test
    public void ActiveUsersListCheck() throws InterruptedException, ParseException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());
        driver.navigate().refresh();
        Thread.sleep(5_000);
        ActiveUsers actvUsrsPage = headerMenu.clickActiveUsers();

        //gf.setTimeZone(TimeZone.getTimeZone("YEKT"));
        TimeZone tzDFLT = TimeZone.getDefault();
        df.setTimeZone(tzDFLT); //GMT, UTC
        pitField.setTimeZone(tzDFLT); //GMT, UTC
        System.out.println("tz = " + tzDFLT);
        Date pit1 = gf.parse("2019.04.25.18.07.00 YEKT");
        String pit1DF = df.format(pit1);
        String pit1GF = gf.format(pit1);
        String pit1FF = pitField.format(pit1);
        String pit1Hour = pit1FF.substring(11,13);
        System.out.println("pit1Hour = " + pit1Hour);

        String shouldBe5 = "qadev qadev 13445af7-99b6-46c7-b855-bb2f7a4d8eda 25.04.2019 " + pit1Hour +":06:38 5:0 edge\n" +
                "Terminate session\n" +
                "qadev qadev 13445af7-99b6-46c7-b855-bb2f7a4d8eda 25.04.2019 " + pit1Hour + ":05:57 5:0 edge\n" +
                "Terminate session\n" +
                "qadev qadev 13445af7-99b6-46c7-b855-bb2f7a4d8eda 25.04.2019 " + pit1Hour + ":05:15 5:0 edge\n" +
                "Terminate session\n" +
                "dsmirnov dsmirnov 13445af7-99b6-46c7-b855-bb2f7a4d8eda 25.04.2019 " + pit1Hour + ":04:32 5:0 edge\n" +
                "Terminate session\n" +
                "dsmirnov dsmirnov 13445af7-99b6-46c7-b855-bb2f7a4d8eda 25.04.2019 " + pit1Hour + ":03:20 5:0 edge\n" +
                "Terminate session";
        String shouldBe1 = "qadev qadev 13445af7-99b6-46c7-b855-bb2f7a4d8eda 25.04.2019 " + pit1Hour + ":06:38 5:0 edge";
        String shouldBe2 = "dsmirnov dsmirnov 13445af7-99b6-46c7-b855-bb2f7a4d8eda 25.04.2019 " + pit1Hour + ":04:32 5:0 edge\n" +
                "Terminate session\n" +
                "dsmirnov dsmirnov 13445af7-99b6-46c7-b855-bb2f7a4d8eda 25.04.2019 " + pit1Hour + ":03:20 5:0 edge\n" +
                "Terminate session";

        System.out.println("pit1DF: -" + pit1DF + "-");
        System.out.println("pit1GF: -" + pit1GF + "-");
        System.out.println("pit1FF: -" + pit1FF + "-");

        Date pit2 = gf.parse("2019.04.25.18.11.00 YEKT");
        String pit2FF = pitField.format(pit2);


        //Set PIT#1 in Calendar filed (start)
        actvUsrsPage.clickCalendarButton();
        Thread.sleep(2_000);
        actvUsrsPage.clickCalendarButton();
        Thread.sleep(1_000);
        actvUsrsPage.clickApplyButton();
        Thread.sleep(2_000);
        actvUsrsPage.setTime(pit1FF);
        Thread.sleep(2_000);
        actvUsrsPage.clickApplyButton();

        WebElement notificationPopup = (new WebDriverWait(driver, 2)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.WERE_LOAD_5_RECORDS.getNotificationText(), notificationPopup.getText());

        Thread.sleep(2_000);
        //Set PIT#1 in Calendar filed (finish)

        //Check filters with PIT#1 (start)
        String tableBefore = actvUsrsPage.getTableText(":06:38");
        Thread.sleep(2_000);
        actvUsrsPage.applicationFilter("edge");
        Thread.sleep(2_000);
        actvUsrsPage.clickApplyButton();
        Thread.sleep(2_000);
        String tableAfter = actvUsrsPage.getTableText(":04:32");
        Assert.assertEquals(true, tableBefore.equals(tableAfter));
        actvUsrsPage.nameFilter("");
        Thread.sleep(2_000);
        actvUsrsPage.clickApplyButton();
        Thread.sleep(8_000);
        actvUsrsPage.nameFilter("dsmirnov");
        Thread.sleep(2_000);
        actvUsrsPage.clickApplyButton();
        Thread.sleep(8_000);
        String tableAfterFilter = actvUsrsPage.getTableText(":04:32");

        Assert.assertEquals(true, tableBefore.equals(tableAfter) && tableBefore.contains(shouldBe2));
        Assert.assertEquals(true, !(tableAfterFilter.contains("qadev")) && tableAfterFilter.contains(shouldBe2));
        //Check filters with PIT#1 (finish)

        //Click Printer and switch to windows #2 (browser sheet #2) start
        String window1 = driver.getWindowHandle(); // driver.switch_to.window(driver.window_handles[1])
        Thread.sleep(1_000);
        System.out.println("windowCurrent is " + window1);
        //System.out.println("going to long pause... ");
        Thread.sleep(1_000);
        actvUsrsPage.clickPrinterIcon();
        Thread.sleep(2_000);
        Set<String> winHandles = driver.getWindowHandles();
        Thread.sleep(1_000);
        String winHandle1 = winHandles.iterator().next();
        Thread.sleep(1_000);
        Object[] winHandleObj = winHandles.toArray();
        Thread.sleep(1_000);
        String winHandle2 = winHandleObj[1].toString();
        Thread.sleep(1_000);
        //driver.switchTo().window(winHandle1);
        Thread.sleep(1_000);
        System.out.println("winHandle1 is " + winHandle1);
        System.out.println("winHandle2 is " + winHandle2);

        driver.switchTo().window(winHandle2);
        //Click Printer and switch to windows #2 (browser sheet #2) finish

        //Check jsf sheet (start)
        String xP = "//h2[contains(.,'Statistics about active users')]";
        driver.findElement(By.xpath(xP)).click();

        //Check jsf sheet (finish)

        //Close windows #2 (browser sheet #2) and switch to windows #1 back (start)
        String window2 = driver.getWindowHandle();
        Thread.sleep(1_000);
        System.out.println("windowCurrent is " + window2);
        Thread.sleep(1_000);
        Assert.assertEquals(true, driver.switchTo().window(window2).getCurrentUrl().contains(".jsf"));
        driver.switchTo().window(window2).close();
        Thread.sleep(1_000);
        driver.switchTo().window(window1);
        Thread.sleep(1_000);
        //Close windows #2 (browser sheet #2) and switch to windows #1 back (finish)

  //ED-3933
        //Set PIT#2 in Calendar filed (start)
        actvUsrsPage.nameFilter("");
        Thread.sleep(2_000);
        actvUsrsPage.clickApplyButton();
        Thread.sleep(2_000);
        actvUsrsPage.clickCalendarButton();
        Thread.sleep(2_000);
        actvUsrsPage.clickCalendarButton();
        Thread.sleep(1_000);
        actvUsrsPage.clickApplyButton();
        Thread.sleep(2_000);
        actvUsrsPage.setTime(pit2FF);
        Thread.sleep(2_000);
        actvUsrsPage.clickApplyButton();
        Thread.sleep(2_000);
        //Set PIT#2 in Calendar filed (finish)

        //Check filters with PIT#2 (start)
        String rowBefore = actvUsrsPage.getRowText(":06:38");
        Thread.sleep(2_000);
        actvUsrsPage.nameFilter("qadev");
        Thread.sleep(2_000);
        actvUsrsPage.clickApplyButton();
        Thread.sleep(2_000);
        String rowAfter = actvUsrsPage.getRowText(":06:38");
        Assert.assertEquals(true, rowBefore.equals(rowAfter));
        actvUsrsPage.nameFilter("");
        Thread.sleep(2_000);
        actvUsrsPage.clickApplyButton();
        Thread.sleep(8_000);
        actvUsrsPage.applicationFilter("edge");
        Thread.sleep(2_000);
        actvUsrsPage.clickApplyButton();
        Thread.sleep(8_000);
        rowAfter = actvUsrsPage.getRowText(":06:38");
        Assert.assertEquals(true, rowBefore.equals(rowAfter) && tableBefore.contains(shouldBe1));
        actvUsrsPage.applicationFilter("");
        //Check filters with PIT#2 (finish)
  //ED-3933
    }
}
