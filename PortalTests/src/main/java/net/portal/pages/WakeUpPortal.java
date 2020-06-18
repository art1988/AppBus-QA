package net.portal.pages;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.interactions.Actions;

public class WakeUpPortal  extends PageObject
{


    private Actions action = new Actions(driver);
    JavascriptExecutor JSexecutor = (JavascriptExecutor)driver;

    public WakeUpPortal(WebDriver driver)
    {
        super(driver);
    }

    public boolean ifError() throws InterruptedException
    {
        //Thread.sleep(1_000);
        boolean ifPageErr = false;
        String xP = "//h1[contains(.,'Error occurred.')]";
        String Err = "no error page";
        try {
            driver.findElement(By.xpath(xP)).getText();
            ifPageErr = true;
            System.out.println("WakeUpPortal: " + driver.findElement(By.xpath(xP)).getText());
        } catch (Exception e) {}

        System.out.println("WakeUpPortal ifPageErr : " + ifPageErr);
        return ifPageErr;
    }

    public boolean ifLoadBar() throws InterruptedException
    {
        //Thread.sleep(1_000);
        boolean ifBar = false;
        String Bar = "no load bar";
        try {
            driver.findElement(By.id("ajaxLoadingBar_modal")).getText();
            ifBar = true;
            System.out.println("WakeUpPortal: " + driver.findElement(By.id("ajaxLoadingBar_modal")).getText() + "element is presented");
        } catch (Exception e) {}

        System.out.println("WakeUpPortal ifBar : " + ifBar);
        return ifBar;
    }

    public boolean ifNoEnvironment() throws InterruptedException
    {
        //Thread.sleep(1_000);
        boolean ifNoEnv = false;
        try {
            if (driver.findElement(By.id("environmentForm:environmentSelect_label")).getText().equals("&nbsp;")) ifNoEnv = true;
            System.out.println("WakeUpPortal: environment is: " + driver.findElement(By.id("environmentForm:environmentSelect_label")).getText());
        } catch (Exception e) {}

        System.out.println("WakeUpPortal ifNoEnv : " + ifNoEnv);
        return ifNoEnv;
    }

    public boolean fixAllProblems() throws InterruptedException
    {
        Boolean noProblem = true;

        Boolean problem = this.ifError();
        if (problem) {
            String curURL = driver.getCurrentUrl();
            driver.navigate().back();
            Thread.sleep(2_000);
            System.out.println("WakeUpPortal: AHTUNG!!! the Page causes error (" + curURL + ") ");
            noProblem = false;
        }

        problem = this.ifNoEnvironment();
        if (problem) {
            String curURL = driver.getCurrentUrl();
            driver.navigate().refresh();
            Thread.sleep(2_000);
            System.out.println("WakeUpPortal: AHTUNG!!! the Page hangs (" + curURL + ") ");
            noProblem = false;
        }

        problem = this.ifLoadBar();
        if (problem) {
            String curURL = driver.getCurrentUrl();
            Thread.sleep(7_000);
            System.out.println("WakeUpPortal: AHTUNG!!! the Page is under loadbar (" + curURL + ") ");
            noProblem = false;
        }

        return noProblem;
    }

    public boolean fixLoadBarProblem() throws InterruptedException
    {
        Boolean noProblem = true;

        boolean problem = this.ifLoadBar();
        if (problem) {
            String curURL = driver.getCurrentUrl();
            Thread.sleep(17_000);
            System.out.println("WakeUpPortal: AHTUNG!!! the Page is under loadbar (" + curURL + ") ");

            problem = this.ifLoadBar();
            if (problem)
            {
                driver.navigate().back();
                Thread.sleep(7_000);
                System.out.println("WakeUpPortal: AHTUNG!!! the Page was under loadbar (" + curURL + "), did get back... ");
                noProblem = false;
            }

        }

        return noProblem;
    }

    public boolean fixEnvProblemOnes() throws InterruptedException
    {
        Boolean noProblem = true;

        boolean problem = this.ifNoEnvironment();
        if (problem) {
            driver.navigate().refresh();
            Thread.sleep(2_000);
            System.out.println("WakeUpPortal: AHTUNG!!! the Page hangs (" + driver.getCurrentUrl() + ") [fixEnvProblemOnes() method]");
            noProblem = false;
        }

        return noProblem;
    }

    public boolean fixEnvProblemCycle() throws InterruptedException {
        Boolean noProblem = true;
        for (int i = 0; i < 10; i++) {
            noProblem = this.fixEnvProblemOnes();
            if (noProblem) break;
            Thread.sleep((500 * i+1));
        }
        if (noProblem) {
            System.out.println("wakeupportal: good, the page is not under env. problem");
        } else {
            System.out.println("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
            System.out.println("WakeUpPortal: AHTUNG!!!, the page :" + driver.getCurrentUrl() + " is under env. problem");
            System.out.println("IT'S HIGHTLY LIKELY THIS SCENARIO WILL BE FAILED");
            System.out.println("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
        }
        return noProblem;
    }


}
