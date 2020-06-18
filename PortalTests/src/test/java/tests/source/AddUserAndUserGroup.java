package tests.source;

import net.portal.constants.Const;
import net.portal.forms.*;
import net.portal.pages.HeaderMenu;
import net.portal.pages.user_and_role_management.UserGroups;
import net.portal.pages.portal_administration.Users;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

import java.io.File;

public class AddUserAndUserGroup
{
    @Test
    public void addUserAndUserGroup() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Users usersPage = headerMenu.clickUsers();

        // Add 3 new users
        for(int i = 1; i < 4; i++)
        {
            UserDetail userDetailForm = usersPage.addNewUser();

            Thread.sleep(2_000);

            //userDetailForm.setDomain("botf03");
            userDetailForm.setUserName("autotestUser_" + i);
            userDetailForm.setFirstName("First name #" + i);
            userDetailForm.setLastName("Last name #" + i);

            userDetailForm.clickAdd();

            Thread.sleep(6_000);
        }

        // Make sure that they were added
        usersPage.searchForUserName("autotestUs");
        usersPage.searchForFirstName(" "); // place cursor on the next field to trigger refresh

        Thread.sleep(2_000);

        Assert.assertEquals(3,
                (long) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr').length" ));

        System.out.println("Creating new User Group by selecting existing users...");
        UserGroups userGroupsPage = headerMenu.clickUserGroups();

        UserGroupDetails userGroupDetails = userGroupsPage.addNewUserGroup();

        String userGroupName = "UG autotest";
        userGroupDetails.setName(userGroupName);
        userGroupDetails.setDescription("Autotest user group: from existing users");

        ListOfUsers listOfUsersForm = userGroupDetails.clickEdit();
        Thread.sleep(3_000);

        listOfUsersForm.searchForUser("autotestUs");
        Thread.sleep(2_000);

        listOfUsersForm.clickSelectAllCheckbox();
        listOfUsersForm.clickSave();

        Thread.sleep(2_000);
        userGroupDetails.clickAdd();

        Thread.sleep(2_000);

        System.out.println("Make sure that column Users has 3 added users");
        Assert.assertEquals("autotestUser_1@botf03.netautotestUser_2@botf03.netautotestUser_3@botf03.net",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data span:contains(\"" + userGroupName + "\")').parent().next().next().find(\"span\").text()")));

        userGroupsPage.clickDownload(userGroupName);

        Thread.sleep(7_000);

        System.out.println("Make sure that file was downloaded...");
        File downloadedFile = new File(Const.DOWNLOAD_FOLDER + "\\" + userGroupName + ".txt");
        Assert.assertTrue(downloadedFile.exists());

        // Go to users and delete those users
        usersPage = headerMenu.clickUsers();

        usersPage.searchForUserName("autotestUs");
        usersPage.searchForFirstName(" "); // place cursor on the next field to trigger refresh
        Thread.sleep(2_000);

        usersPage.clickSelectAllCheckbox();

        DeleteFollowingUsers deleteFollowingUsersPopup = usersPage.deleteUser();
        Thread.sleep(2_000);

        Assert.assertEquals("userName = autotestUser_1userName = autotestUser_2userName = autotestUser_3", deleteFollowingUsersPopup.getListOfUsersToDelete());
        deleteFollowingUsersPopup.clickDelete();

        Thread.sleep(2_000);
        // Refresh page by visiting it again
        headerMenu.clickUsers();

        // Go to User Groups
        userGroupsPage = headerMenu.clickUserGroups();

        userGroupsPage.selectUserGroup(userGroupName);
        FollowingItemsWillBeDeleted followingItemsWillBeDeleted = userGroupsPage.deleteUserGroup();

        Assert.assertEquals("name = UG autotest", followingItemsWillBeDeleted.getListOfItemsToDelete());

        followingItemsWillBeDeleted.clickDelete();

        Thread.sleep(5_000);

        System.out.println("Creating new User Group by uploading file...");
        userGroupDetails = userGroupsPage.addNewUserGroup();

        userGroupDetails.setName(userGroupName);
        userGroupDetails.setDescription("Autotest user group: from file");

        userGroupDetails.chooseFile(downloadedFile.getAbsolutePath());
        userGroupDetails.clickUpload();
        Thread.sleep(1_000);

        Assert.assertEquals("autotestUser_1@botf03.netautotestUser_2@botf03.netautotestUser_3@botf03.net",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#entity\\\\:dialogsForm\\\\:group-users_content > span').text()")));

        userGroupDetails.clickAdd();
        Thread.sleep(1_000);

        // Go back to Users
        usersPage = headerMenu.clickUsers();

        usersPage.searchForUserName("autotestUs");
        usersPage.searchForFirstName(" "); // place cursor on the next field to trigger refresh
        Thread.sleep(2_000);

        // Check that these 3 users has 'UG autotest' as User group
        Assert.assertEquals("UG autotestUG autotestUG autotest",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(6)').text()")));

        Thread.sleep(5_000);

        // Go back to User Groups and edit just created
        userGroupsPage = headerMenu.clickUserGroups();

        userGroupDetails = userGroupsPage.editUserGroup(userGroupName);
        Thread.sleep(1_000);

        userGroupName += " [edited]";
        userGroupDetails.setName(userGroupName);
        userGroupDetails.clickSave();
        Thread.sleep(1_000);

        // Go to Users to make sure that user group has new name
        usersPage = headerMenu.clickUsers();

        usersPage.searchForUserName("autotestUs");
        usersPage.searchForFirstName(" "); // place cursor on the next field to trigger refresh
        Thread.sleep(2_000);

        // Check that these 3 users has edited user group
        Assert.assertEquals("UG autotest [edited]UG autotest [edited]UG autotest [edited]",
                String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#table\\\\:tableForm\\\\:entityTable_data tr td:nth-child(6)').text()")));

        // After-test clean-up
        // 1. Delete downloaded file
        if( downloadedFile.delete() )
        {
            System.out.println(downloadedFile.getAbsolutePath() + " was deleted");
        } else
        {
            System.err.println("Unable to delete " + downloadedFile.getAbsolutePath());
        }

        // 2. Remove users
        usersPage.clickSelectAllCheckbox();
        deleteFollowingUsersPopup = usersPage.deleteUser();
        Thread.sleep(2_000);
        deleteFollowingUsersPopup.clickDelete();

        Thread.sleep(5_000);

        // 3. Remove user group
        userGroupsPage = headerMenu.clickUserGroups();
        userGroupsPage.selectUserGroup(userGroupName);
        followingItemsWillBeDeleted = userGroupsPage.deleteUserGroup();
        followingItemsWillBeDeleted.clickDelete();

        Thread.sleep(5_000);
    }
}
