package tests.source;

import net.portal.forms.ItemAssignmentDetails;
import net.portal.pages.HeaderMenu;
import net.portal.pages.user_and_role_management.NavigationItems;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

import java.util.HashMap;

public class IterateControllerType
{
    // Map Controller type to Controller property
    private HashMap<String, String> controller;

    /**
     * This test open Item Assignment Details and iterate through controller types and check controller properties:
     * which of them are required and which of them are not
     */
    @Test
    public void iterateControllerType() throws InterruptedException
    {
        System.out.println("--- START OF IterateControllerType ---");

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        NavigationItems navigationItemsPage = headerMenu.clickNavigationItems();

        ItemAssignmentDetails itemAssignmentDetails = navigationItemsPage.addNavigationItem();

        initControllerTypes();

        for(String key : controller.keySet())
        {
            itemAssignmentDetails.setControllerType(key);

            Thread.sleep(1_500);

            Assert.assertEquals(controller.get(key),
                    String.valueOf(((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#itemDetailsDlgForm\\\\:controllerItemPropertiesTable_data tr td:nth-child(2)').text()")));
        }

        itemAssignmentDetails.clickCancel();

        System.out.println("--- END OF IterateControllerType ---");
    }

    private void initControllerTypes()
    {
        controller = new HashMap<>();

        controller.put("WEB", "url");
        controller.put("RDP", "url");
        controller.put("SYSTEM-FUNCTION", "action");
        controller.put("DOCUMENTS", "typeurl");
        controller.put("RSSVIEWER", "typeurl");
        controller.put("PDF", "_property_edit_property_editedurl");
        controller.put("BARCODE", "");
        controller.put("APPINTEGRATOR", "");
        controller.put("CITRIX", "");
        controller.put("WEB-IE", "url");
    }
}
