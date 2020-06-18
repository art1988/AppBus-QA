package com.appbus.pages.tabs;

import com.appbus.pages.PageObject;
import com.appbus.pages.menuItems.DocumentsSubmenu;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.support.FindBy;

/**
 * Class represents SharePointTab and Attach popup in Mail
 */
public class SharePointTab extends PageObject
{
    @FindBy(name = "All documents")
    private MobileElement allDocumentsLabel;

    @FindBy(name = "Cloud")
    private MobileElement cloudButton;

    @FindBy(name = "Device")
    private MobileElement deviceButton;

    private DocumentsSubmenu submenu;

    @FindBy(name = "UploadItem")
    private MobileElement attachButton; // For Attach popup via Mail

    @FindBy(name = "Search")
    private MobileElement searchField; // For Attach popup via Mail


    /////////////////////////
    // Hardcoded filenames //
    /////////////////////////
    @FindBy(name = "Documents for POC")
    private MobileElement firstFolder;

    @FindBy(name = "Analytics App Catalog - App Review Questionnaire.docx")
    private MobileElement docxFile;

    @FindBy(name = "Report1.xlsx")
    private MobileElement xlsxFile;

    @FindBy(name = "11111.pdf")
    private MobileElement pdfFile;

    @FindBy(name = "XML_auto.xml")
    private MobileElement xmlFile;


    public SharePointTab(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return ( allDocumentsLabel.isDisplayed() & cloudButton.isDisplayed() & deviceButton.isDisplayed() );
    }

    public void clickFirstFolder()
    {
        firstFolder.click();
        System.out.println("First folder was clicked");
    }

    public void clickDocxFile()
    {
        docxFile.click();
        System.out.println("Docx file was clicked");
    }

    public void clickXlsxFile()
    {
        xlsxFile.click();
        System.out.println("Xlsx file was clicked");
    }

    public void clickPdfFile()
    {
        pdfFile.click();
        System.out.println("PDF file was clicked");
    }

    public void clickXmlFile()
    {
        xmlFile.click();
        System.out.println("XML file was clicked");
    }

    public DocumentsSubmenu getSubmenu()
    {
        submenu = new DocumentsSubmenu(driver);

        return submenu;
    }

    public void clickCloud()
    {
        cloudButton.click();
        System.out.println("Cloud button was clicked");
    }

    public void clickDevice()
    {
        deviceButton.click();
        System.out.println("Device button was clicked");
    }

    /**
     * Only for Attach popup via Mail
     */
    public void confirmAttach()
    {
        attachButton.click();
        System.out.println("Attach button was clicked");
    }

    /**
     * Only for Attach popup via Mail
     */
    public void searchFor(String text)
    {
        searchField.sendKeys(text);
    }

    public boolean isDeviceSelected()
    {
        if( Integer.parseInt(deviceButton.getAttribute("value")) == 1 )
        {
            return true;
        }

        return false;
    }

    public boolean isDocxVisible()
    {
        return docxFile.isDisplayed();
    }

    public boolean isXlsxVisible()
    {
        boolean isVisible = false;

        try
        {
            isVisible = xlsxFile.isDisplayed();
        }
        catch (NoSuchElementException ex)
        {
            System.err.println("Can't locate element: *.xlsx file");
        }

        return isVisible;
    }

    public boolean isPdfVisible()
    {
        return pdfFile.isDisplayed();
    }

    public boolean isXmlVisible()
    {
        return xmlFile.isDisplayed();
    }
}
