package tests.source;

import net.portal.constants.Notifications;
import net.portal.forms.AlertDetails;
import net.portal.forms.EmailGroupsDetails;
import net.portal.pages.HeaderMenu;
import net.portal.pages.audit.Alerts;
import net.portal.pages.audit.EmailGroups;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class AddEmailGroup
{
    @Test
    public void addEmailGroup() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        EmailGroups emailGroupsPage = headerMenu.clickEmailGroups();

        EmailGroupsDetails emailGroupsDetails = emailGroupsPage.addEmailGroup();
        Thread.sleep(3_000);

        String emailGroupName = "AT EmGr",
               content = "skoval@botf03.net\nmilshtyu@botf03.net\njerry@botf03.net\nart.khassanov@gmail.com",
               description = "Description of AT";

        emailGroupsDetails.setName(emailGroupName);
        emailGroupsDetails.setContent(content);
        emailGroupsDetails.setDescription(description);
        emailGroupsDetails.clickAdd();
        Thread.sleep(3_000);

        System.out.println("Make sure that " + emailGroupName + " item is on the list...");

        // Check Name
        Assert.assertEquals(emailGroupName, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + emailGroupName + "\")').parent().text()")));
        // Check Content
        Assert.assertEquals(content, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + emailGroupName + "\")').parent().next().text()")));
        // Check Description
        Assert.assertEquals(description, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + emailGroupName + "\")').parent().next().next().text()")));

        System.out.println("Trying to edit just created Email Group...");

        content = "NEW content";
        description += " [ed]";

        emailGroupsPage.editEmailGroup(emailGroupName, emailGroupName += " [edited]", content, description);
        Thread.sleep(3_000);

        System.out.println("Assert changes...");

        // Check Name
        Assert.assertEquals(emailGroupName, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + emailGroupName + "\")').parent().text()")));
        // Check Content
        Assert.assertEquals(content, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + emailGroupName + "\")').parent().next().text()")));
        // Check Description
        Assert.assertEquals(description, String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + emailGroupName + "\")').parent().next().next().text()")));

        System.out.println("Check uniqueness of Email Group...");

        emailGroupsDetails = emailGroupsPage.addEmailGroup();
        Thread.sleep(3_000);

        emailGroupsDetails.setName(emailGroupName);
        emailGroupsDetails.setContent(content);
        emailGroupsDetails.setDescription(description);
        emailGroupsDetails.clickAdd();

        WebElement notificationPopup = (new WebDriverWait(FunctionalTest.getDriver(), 7)).until(ExpectedConditions.visibilityOfElementLocated(By.className("ui-growl-title")));
        Assert.assertEquals(Notifications.EMAIL_GROUP_NAME_SHOULD_BE_UNIQUE.getNotificationText(), notificationPopup.getText());

        emailGroupsDetails.clickCancel();
        Thread.sleep(1_000);

        System.out.println("Make sure that just created email group is visible on Alert Details form...");

        // Go to Alerts page...
        Alerts alertsPage = headerMenu.clickAlerts();

        AlertDetails alertDetailsForm = alertsPage.addAlert();
        Thread.sleep(3_000);

        alertDetailsForm.setEmailGroup(emailGroupName);

        Assert.assertEquals(emailGroupName, alertDetailsForm.getEmailGroup());

        alertDetailsForm.clickCancel();
        Thread.sleep(3_000);
    }
}
