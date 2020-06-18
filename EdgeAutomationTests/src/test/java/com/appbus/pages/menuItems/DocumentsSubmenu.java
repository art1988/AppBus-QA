package com.appbus.pages.menuItems;

import com.appbus.pages.email_related.Email;
import com.appbus.pages.PageObject;
import com.appbus.pages.popups.DeleteDocumentPopup;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;

public class DocumentsSubmenu extends PageObject
{
    @FindBy(name = "Edit")
    private MobileElement edit;

    @FindBy(name = "Attach")
    private MobileElement attach;

    @FindBy(name = "Download")
    private MobileElement download;

    @FindBy(name = "Delete")
    private MobileElement delete;

    @FindBy(name = "Resize")
    private MobileElement resize;


    public DocumentsSubmenu(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( attach.isDisplayed() & resize.isDisplayed() );
    }

    public Email clickAttach()
    {
        attach.click();
        System.out.println("Attach menu button was clicked");

        return new Email(driver);
    }

    public void clickDownload()
    {
        download.click();
        System.out.println("Download menu button was clicked");
    }

    public DeleteDocumentPopup clickDelete()
    {
        delete.click();
        System.out.println("Delete menu button was clicked");

        return new DeleteDocumentPopup(driver);
    }
}
