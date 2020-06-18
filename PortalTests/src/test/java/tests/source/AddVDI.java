package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.FollowingItemsWillBeDeleted;
import net.portal.forms.RdpDetails;
import net.portal.pages.HeaderMenu;
import net.portal.pages.pool_management.VDIs;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class AddVDI
{
    @Test
    public void addVDI() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        VDIs vdisPage = headerMenu.clickVDIs();

        String[] ips   = {"127.0.0.1", "rdp-kr-dev", "192.168.0.110", "some_ip"},
                 names = {"localhost", "rdp-exa1-dev", "rdp-exa2-dev", "rdp-exa3-dev"},
                 users = {"system", "exadel1", "exadel2", "exadel3"};

        RdpDetails rdpDetails;
        for( int i = 0; i < ips.length; i++ )
        {
            rdpDetails = vdisPage.addVDI();
            Thread.sleep(3_000);

            rdpDetails.setComputerIP(ips[i]);
            rdpDetails.setComputerName(names[i]);
            rdpDetails.setComputerPort("3389");
            rdpDetails.setComputerDomain("botf03.net");
            rdpDetails.setUsername(users[i]);

            rdpDetails.clickAdd();
            Thread.sleep(4_000);
        }

        vdisPage.clickRefresh(); // Click Refresh to make sure that rows were sorted correctly

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.SUCCESSFULLY_RELOADED.getNotificationText(), notificationPopup.getText());
        Thread.sleep(3_000);

        // Assert by columns:
        // check Computer IP column
        Assert.assertEquals("rdp-kr-dev192.168.0.110some_ip127.0.0.1",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(2)').text()")));
        // check Computer name column
        Assert.assertEquals("rdp-exa1-devrdp-exa2-devrdp-exa3-devlocalhost",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(3)').text()")));
        // check Computer port column
        Assert.assertEquals("3389338933893389",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(4)').text()")));
        // check Computer domain column
        Assert.assertEquals("botf03.netbotf03.netbotf03.netbotf03.net",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(5)').text()")));
        // check Username column
        Assert.assertEquals("exadel1exadel2exadel3system",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(6)').text()")));

        // Change one param for each record
        rdpDetails = vdisPage.editVDI("localhost");
        Thread.sleep(3_000);
        rdpDetails.setUsername("ABC");
        rdpDetails.clickSave();
        Thread.sleep(3_000);

        rdpDetails = vdisPage.editVDI("rdp-exa1-dev");
        Thread.sleep(3_000);
        rdpDetails.setComputerDomain("nasa.gov");
        rdpDetails.clickSave();
        Thread.sleep(3_000);

        rdpDetails = vdisPage.editVDI("rdp-exa2-dev");
        Thread.sleep(3_000);
        rdpDetails.setComputerPort("443");
        rdpDetails.clickSave();
        Thread.sleep(3_000);

        rdpDetails = vdisPage.editVDI("rdp-exa3-dev");
        Thread.sleep(3_000);
        rdpDetails.setComputerIP("88.88.188.10");
        rdpDetails.clickSave();
        Thread.sleep(3_000);

        Thread.sleep(3_000);
        vdisPage.clickRefresh(); // Refresh again and make sure that edited items were correct
        Thread.sleep(3_000);

        // Assert columns again
        Assert.assertEquals("127.0.0.1rdp-kr-dev192.168.0.11088.88.188.10",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(2)').text()")));
        // check Computer port column
        Assert.assertEquals("338933894433389",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(4)').text()")));
        // check Computer domain column
        Assert.assertEquals("botf03.netnasa.govbotf03.netbotf03.net",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(5)').text()")));
        // check Username column
        Assert.assertEquals("ABCexadel1exadel2exadel3",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(6)').text()")));

        // TODO: ED-3635. Add test on uniqueness of records

        // Delete all
        vdisPage.clickSelectAllCheckbox();
        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = vdisPage.clickDelete();
        Thread.sleep(3_000);
        Assert.assertEquals("computerIp = 127.0.0.1computerIp = rdp-kr-devcomputerIp = 192.168.0.110computerIp = 88.88.188.10",
                followingItemsWillBeDeleted.getListOfItemsToDelete());
        followingItemsWillBeDeleted.clickDelete();
        Thread.sleep(3_000);

        Assert.assertEquals("No records found.", String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data').text()")));
    }
}
