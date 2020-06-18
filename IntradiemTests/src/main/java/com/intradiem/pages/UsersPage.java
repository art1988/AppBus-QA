package com.intradiem.pages;

import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;

public class UsersPage extends PageObject
{
    @FindBy(id = "ctl00_ActionBarContent_rbAction_Share_input")
    private WebElement messageButton;

    @FindBy(id = "ctl00_ActionBarContent_rbAction_QuickAction_input")
    private WebElement quickActionButton;


    public UsersPage(WebDriver driver)
    {
        super(driver);
    }

    /**
     * Select checkbox near given user in table
     * @param user to find in table
     * @throws InterruptedException
     */
    public void selectCheckBoxNearUser(String user) throws InterruptedException
    {
        String usernameInTable = "";

        while( true )
        {
            usernameInTable = String.valueOf(((JavascriptExecutor)driver).executeScript("return $('#ctl00_GridContent_gridUsers_ctl00 tbody tr td:contains(\"" + user + "\")').text()"));

            if( usernameInTable.equals(user) )
            {
                // Click checkbox near given user
                ((JavascriptExecutor)driver).executeScript("$('#ctl00_GridContent_gridUsers_ctl00 tbody tr td:contains(\"" + user + "\")').prev('td').find(\"input\").click()");

                System.out.println("Checkbox near user: " + user + " was checked");

                return;
            }
            else
            {
                // Click next page button
                ((JavascriptExecutor)driver).executeScript("$('input[name=\"ctl00$GridContent$gridUsers$ctl00$ctl03$ctl01$ctl28\"]').click()");

                Thread.sleep(5_000);
            }
        }
    }

    /**
     * Fill in Message form and submit
     * @param subject of a message
     * @param messageText message text
     */
    public void sendMessage(String subject, String messageText) throws InterruptedException
    {
        // Click Message button
        messageButton.click();

        Thread.sleep(5000);

        // Set subject
        ((JavascriptExecutor)driver).executeScript("$($('[name=\"RadWindowShareMessages\"]')[0].contentDocument).find(\".valueContainer input\").val('" + subject + "')");

        Thread.sleep(1000);

        // Set message body
        ((JavascriptExecutor)driver).executeScript("$($('[name=\"RadWindowShareMessages\"]')[0].contentDocument).find(\"#ctl00_overlayContent_radMessageEditor_contentIframe\")[0].contentDocument.body.textContent=\"" + messageText + "\"");

        Thread.sleep(2000);

        // Click submit
        ((JavascriptExecutor)driver).executeScript("$($('[name=\"RadWindowShareMessages\"]')[0].contentDocument).find(\".rbDecorated\").click()");

        System.out.println("Submit was clicked");
        System.out.println("Message with subject = " + subject + " and body = " + messageText + " was sent");
    }
}
