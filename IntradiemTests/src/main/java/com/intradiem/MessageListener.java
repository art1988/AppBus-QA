package com.intradiem;

import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.NoSuchSessionException;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import tests.source.IntradiemClientListener;

import java.awt.*;
import java.awt.event.KeyEvent;
import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;

public class MessageListener extends Thread
{
    private Queue<String> fifo_Messages;

    private String messageText;


    public MessageListener(Queue<String> fifo_Messages)
    {
        super("Message listener");

        this.fifo_Messages = new LinkedList<>(fifo_Messages); // Make our own copy of messages
    }

    @Override
    public void run()
    {
        while( true )
        {
            WebElement messageTextElement = null;

            try
            {
                messageTextElement = new WebDriverWait(IntradiemClientListener.getDriver(), 5 * 60 * 1000).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/Window/Custom/Custom[3]/Document/Custom/Custom/Custom[3]/Text")));
                Assert.assertNotNull(messageTextElement);
            }
            catch(NoSuchSessionException e)
            {
                System.out.println("------- MessageListener was interrupted. Quitting... -------");
                System.out.println("Another caught NoSuchSessionException is OK...");
                return;
            }

            // To remove duplicate messages
            if( messageTextElement.getText().equals(messageText) == false )
            {
                messageText = messageTextElement.getText().trim();

                if( messageText.equals("") ) // do not pay attention on empty strings
                {
                    continue;
                }

                System.out.println("[Client Listener] received message : " + messageText);

                try
                {
                    messageHandler(messageText);
                }
                catch (InterruptedException | IOException e)
                {
                    e.printStackTrace();
                }

                Assert.assertEquals(fifo_Messages.remove(), messageText);
            }

            // Issue 'quit' message to terminate MessageListener
            if( messageText.equals("quit") )
            {
                // Click VIEW
                WebElement viewButton = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/Window/Custom/Custom[3]/Document/Custom/Custom/Button[2]")));
                viewButton.click();

                try
                {
                    Thread.sleep(500);

                    Robot robot = new Robot();
                    // need to set focus on DONE button, because sometimes clicking on it doesn't fire
                    for (int tabCount = 0; tabCount < 4; tabCount++)
                    {
                        robot.keyPress(KeyEvent.VK_TAB);
                        robot.keyRelease(KeyEvent.VK_TAB);
                    }
                }
                catch (AWTException | InterruptedException e)
                {
                    e.printStackTrace();
                }

                // Click Done button DONE
                WebElement doneButton = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.name("DONE")));
                doneButton.click();

                return; // terminate thread
            }
        }
    }

    private void messageHandler(String receivedMessage) throws InterruptedException, IOException
    {
        switch (receivedMessage)
        {
            // Do behavior to test NoDelete rule
            case "NoDELETE":
                // Click VIEW
                WebElement viewButton = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/Window/Custom/Custom[3]/Document/Custom/Custom/Button[2]")));
                viewButton.click();

                // Click DELETE button
                WebElement deleteButton = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.name("DELETE")));
                deleteButton.click();

                // Check that we got "The API is not responding or an API error has occurred." pop up
                WebElement popup = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.name("The API ...")));
                Assert.assertNotNull(popup);

                // Click OK by pressing tab and then hit Enter key
                popup.sendKeys(Keys.TAB);
                popup.sendKeys(Keys.RETURN);

                // Then click DONE
                WebElement doneButton = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.name("DONE")));
                doneButton.click();

                break;

            // Do behavior to test NoGETScheduleSegments rule
            case "NoGETScheduleSegments":
                clickOnMenuButton();

                // Click on 'My Schedule' label
                WebElement myScheduleItem = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/Window/Custom/Custom[3]/Document/Group/List/MenuItem[3]/ListItem/Custom/Custom[2]")));
                myScheduleItem.click();

                Thread.sleep(1_000);

                // Check that we got "There was an error retrieving schedules. Please come back later." pop up
                popup = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.name("There was ...")));
                Assert.assertNotNull(popup);

                // Close popup
                popup.sendKeys(Keys.TAB);
                popup.sendKeys(Keys.RETURN);

                Thread.sleep(1_000);

                // Click quit button
                WebElement quitButton = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/Window/Custom/Custom[3]/Document/Button[2]")));
                quitButton.click();

                break;

            // Do behavior to test NoGETMessages rule
            case "NoGETMessages":
                clickOnMenuButton();

                // Click on 'Messages & Activity' label
                WebElement messagesAndActivityItem = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/Window/Custom/Custom[3]/Document/Group[3]/List/MenuItem[2]/ListItem/Custom/Custom[2]")));
                messagesAndActivityItem.click();

                Thread.sleep(1_000);

                // Check that we got "The API is not responding or an API error has occurred." pop up
                popup = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.name("The API ...")));
                Assert.assertNotNull(popup);

                Thread.sleep(1_000);

                // Click OK by pressing tab and then hit Enter key
                popup.sendKeys(Keys.TAB);
                popup.sendKeys(Keys.RETURN);

                // kill Intradiem process since there is unable to locate Quit button
                Runtime.getRuntime().exec("taskkill /f /im Intra*");
                System.out.println("Intradiem process was killed");

                IntradiemClientListener.getDriver().quit(); // Shut down driver
                System.out.println("IntradiemClientListener.getDriver().quit()");

                Thread.currentThread().interrupt(); // stop the thread

                break;

            // Do behavior to test NoFonts rule
            case "NoFonts":
                clickOnMenuButton();

                // Click on 'Tasks and Assignments' label
                WebElement taskAndAssignmentsItem = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/Window/Custom/Custom[3]/Document/Group[3]/List/MenuItem[1]/ListItem/Custom/Custom[2]")));
                taskAndAssignmentsItem.click();

                // Click on 'Tasks and Assignments' label
                WebElement tasksAndAssignmentsLabel = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/Window/Custom/Custom[3]/Document/Custom")));
                tasksAndAssignmentsLabel.click();

                // Press Tab to move focus on close button and click Enter
                try
                {
                    Robot robot = new Robot();

                    robot.keyPress(KeyEvent.VK_TAB);
                    Thread.sleep(500);
                    robot.keyRelease(KeyEvent.VK_TAB);

                    Thread.sleep(1_000);

                    robot.keyPress(KeyEvent.VK_ENTER);
                    Thread.sleep(200);
                    robot.keyRelease(KeyEvent.VK_ENTER);
                }
                catch (AWTException | InterruptedException e)
                {
                    e.printStackTrace();
                }

                break;
        }
    }

    private void clickOnMenuButton() throws InterruptedException
    {
        // Click VIEW
        WebElement viewButton = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/Window/Custom/Custom[3]/Document/Custom/Custom/Button[2]")));
        viewButton.click();

        Thread.sleep(500);

        // Click on message area
        WebElement messageArea = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/Window/Custom/Custom[3]/Document/Custom[1]/Custom[4]")));
        messageArea.click();

        // Click Tab to set focus on prev. element <- ( arrow back)
        messageArea.sendKeys(Keys.TAB);
        messageArea.sendKeys(Keys.RETURN); // Click Enter

        Thread.sleep(500);

        // Click on 'Tasks and Assignments' label
        WebElement tasksAndAssignmentsLabel = new WebDriverWait(IntradiemClientListener.getDriver(), 20_000).until(ExpectedConditions.visibilityOfElementLocated(By.xpath("/Window/Custom/Custom[3]/Document/Custom")));
        tasksAndAssignmentsLabel.click();

        // Press Shift+Tab to set focus on menu button and click Enter
        try
        {
            Robot robot = new Robot();

            robot.keyPress(KeyEvent.VK_SHIFT);
            Thread.sleep(500);
            robot.keyPress(KeyEvent.VK_TAB);
            Thread.sleep(500);
            robot.keyRelease(KeyEvent.VK_TAB);
            Thread.sleep(500);
            robot.keyRelease(KeyEvent.VK_SHIFT);

            Thread.sleep(1_000);

            robot.keyPress(KeyEvent.VK_ENTER);
            Thread.sleep(200);
            robot.keyRelease(KeyEvent.VK_ENTER);
        }
        catch (AWTException | InterruptedException e)
        {
            e.printStackTrace();
        }

        Thread.sleep(2_000);
    }

}
