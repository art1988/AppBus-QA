package tests.source;

import static tests.source.FunctionalTest.driver;

import net.portal.forms.AddNewProvConfig;
import net.portal.forms.SureToDelete;
import net.portal.pages.device_management.ProvisioningConfig;
import org.junit.Assert;
import org.junit.Test;
import net.portal.pages.HeaderMenu;
import net.portal.pages.WakeUpPortal;
import org.junit.runners.Suite;

public class ProvisionConfigDeleteConfig
{
    @Test
    public void ProvisionConfigDeleteConfig() throws InterruptedException
    {
        ProvisionConfigDeleteConfig(true);
    }

    public void ProvisionConfigDeleteConfig(boolean refresh) throws InterruptedException
    {
        driver.navigate().refresh();
        Thread.sleep(5_000);

        boolean doPortalWakeUp = true;
        Thread.sleep(1_000);
        if (refresh) driver.navigate().refresh();
        if (refresh) Thread.sleep(5_000);
        else Thread.sleep(2_000);
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());
        WakeUpPortal wkp = new WakeUpPortal(FunctionalTest.getDriver());
        Thread.sleep(2_000);

        ProvisioningConfig pc = headerMenu.clickProvisioningConfig(doPortalWakeUp);
        Boolean noProblems = wkp.fixAllProblems();
        System.out.println("ProvisionConfigDeleteConfig: noProblems = " + noProblems);

        String ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        if (!ItemLIst.contains("Upcoming config"))
        {
            System.out.println("ProvisionConfigDeleteConfig: going to creat Upcoming config...");
            AddNewProvConfig addPop = pc.clickAddConfig();
            Thread.sleep(1_000);
            addPop.clickTomorrowDay();
            Thread.sleep(1_000);
            String tomorrow = addPop.getStartTimeValue();
            Thread.sleep(1_000);
            addPop.clickOk();
            Thread.sleep(2_000);
            pc.clickApply();
            Thread.sleep(3_000);
        }

        pc.clickSelectConfiguration();
        Thread.sleep(1_000);
        pc.clickUpcomingConfig();
        Thread.sleep(3_000);
        SureToDelete pop = pc.clickDeleteConfig();
        Thread.sleep(1_000);
        pop.clickYes();
        Thread.sleep(2_000);

        ItemLIst = pc.getConfigItemsList();
        System.out.println("--------------------------");
        System.out.println(ItemLIst);
        System.out.println("--------------------------");

        Assert.assertTrue("ProvisionConfigDeleteConfig: Upcoming config doesn't exist",!ItemLIst.contains("Upcoming config"));
    }
}
