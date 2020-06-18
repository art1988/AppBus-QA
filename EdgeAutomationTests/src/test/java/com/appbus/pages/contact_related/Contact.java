package com.appbus.pages.contact_related;

import com.appbus.pages.PageObject;
import com.appbus.pages.constants.Context;
import com.appbus.pages.helpers.JSExecutor;
import com.appbus.pages.popups.DeleteContactPopup;
import com.appbus.pages.popups.MoveContactPopup;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;
import org.junit.Assert;
import org.openqa.selenium.support.FindBy;
import tests.source.FunctionalTest;

public class Contact extends PageObject
{
    // Use these two native elemetns only for init()
    @FindBy(name = "Profile")
    private MobileElement profileTab;

    @FindBy(name = "Contacts")
    private MobileElement contactsTab;


    /**
     * Non native elements
     * id's of subtabs
     */
    private static final String id_ProfileSubtab  = "tab-header-profile",
                                id_ContactsSubtab = "tab-header-contacts",
                                id_AddressSubtab  = "tab-header-address",
                                id_MoreSubtab     = "tab-header-more";
    /**
     * id's of Profile subtab
     */
    private static final String  id_Name       = "FullName",
                                 id_JobTitle   = "JobTitle",
                                 id_Company    = "Company",
                                 id_Department = "Department",
                                 id_Birthday   = "Birthday";

    /**
     * id's of Contacts subtab
     */
    private static final String id_BusinessPhone   = "Phone",
                                id_MobilePhone     = "MobilePhone",
                                id_HomePhone       = "HomePhone",
                                id_WebSite         = "WebAddress",
                                id_Email_1         = "Email1",
                                id_Email_2         = "Email2",
                                id_Email_3         = "Email3",
                                id_ImId            = "IMId";

    /**
     * id's of Address subtab
     */
    private static final String id_WorkStreet     = "BusinessAddressStreet",
                                id_WorkCity       = "BusinessAddressCity",
                                id_WorkState      = "BusinessAddressState",
                                id_WorkPostalCode = "BusinessAddressPostalCode",
                                id_WorkCountry    = "BusinessAddressCountry",

                                id_HomeStreet     = "HomeAddressStreet",
                                id_HomeCity       = "HomeAddressCity",
                                id_HomeState      = "HomeAddressState",
                                id_HomePostalCode = "HomeAddressPostalCode",
                                id_HomeCountry    = "HomeAddressCountry";

    /**
     * id's of More subtab
     */
    private static final String id_Language = "Language",
                                id_Hobbies  = "Hobbies",
                                id_Gender   = "Gender";

    private static final String id_Accept  = "contact-save-option",
                                id_Move    = "contact-move-option",
                                id_Delete  = "contact-delete-option";


    public Contact(AppiumDriver driver)
    {
        super(driver);

        Assert.assertTrue(isInit());
    }

    private boolean isInit()
    {
        return (profileTab.isDisplayed() & contactsTab.isDisplayed());
    }

                                            /* Profile subtab */
    public void setName(String name)
    {
        JSExecutor.setTextForField(id_Name, name);
    }

    public String getName()
    {
        return JSExecutor.getTextFromFiled(id_Name);
    }

    public void setJobTitle(String jobTitle)
    {
        JSExecutor.setTextForField(id_JobTitle, jobTitle);
    }

    public String getJobTitle()
    {
        return JSExecutor.getTextFromFiled(id_JobTitle);
    }

    public void setCompany(String company)
    {
        JSExecutor.setTextForField(id_Company, company);
    }

    public String getCompany()
    {
        return JSExecutor.getTextFromFiled(id_Company);
    }

    public void setDepartment(String dep)
    {
        JSExecutor.setTextForField(id_Department, dep);
    }

    public String getDepartment()
    {
        return JSExecutor.getTextFromFiled(id_Department);
    }

    /**
     *  Format: YYYY-MM-DD
     */
    public void setBirthday(String birthday)
    {
       JSExecutor.setTextForField(id_Birthday, birthday);
    }

    public String getBirthday()
    {
        return JSExecutor.getTextFromFiled(id_Birthday);
    }
                                                    /* * */

                                            /* Address subtab */
    public void setWorkStreet(String street)
    {
        JSExecutor.setTextForField(id_WorkStreet, street);
    }

    public String getWorkStreet()
    {
        return JSExecutor.getTextFromFiled(id_WorkStreet);
    }

    public void setHomeStreet(String street)
    {
        JSExecutor.setTextForField(id_HomeStreet, street);
    }

    public String getHomeStreet()
    {
        return JSExecutor.getTextFromFiled(id_HomeStreet);
    }

    public void setWorkCity(String city)
    {
        JSExecutor.setTextForField(id_WorkCity, city);
    }

    public String getWorkCity()
    {
        return JSExecutor.getTextFromFiled(id_WorkCity);
    }

    public void setHomeCity(String city)
    {
        JSExecutor.setTextForField(id_HomeCity, city);
    }

    public String getHomeCity()
    {
        return JSExecutor.getTextFromFiled(id_HomeCity);
    }

    public void setWorkState(String state)
    {
        JSExecutor.setTextForField(id_WorkState, state);
    }

    public String getWorkState()
    {
        return JSExecutor.getTextFromFiled(id_WorkState);
    }

    public void setHomeState(String state)
    {
        JSExecutor.setTextForField(id_HomeState, state);
    }

    public String getHomeState()
    {
        return JSExecutor.getTextFromFiled(id_HomeState);
    }

    public void setWorkPostalCode(String postalCode)
    {
        JSExecutor.setTextForField(id_WorkPostalCode, postalCode);
    }

    public String getWorkPostalCode()
    {
        return JSExecutor.getTextFromFiled(id_WorkPostalCode);
    }

    public void setHomePostalCode(String postalCode)
    {
        JSExecutor.setTextForField(id_HomePostalCode, postalCode);
    }

    public String getHomePostalCode()
    {
        return JSExecutor.getTextFromFiled(id_HomePostalCode);
    }

    public void setWorkCountry(String country)
    {
        JSExecutor.setTextForField(id_WorkCountry, country);
    }

    public String getWorkCountry()
    {
        return JSExecutor.getTextFromFiled(id_WorkCountry);
    }

    public void setHomeCountry(String country)
    {
        JSExecutor.setTextForField(id_HomeCountry, country);
    }

    public String getHomeCountry()
    {
        return JSExecutor.getTextFromFiled(id_HomeCountry);
    }
                                                    /* * */

                                            /* Contacts subtab */
    public void setBusinessPhone(String phone)
    {
        JSExecutor.setTextForField(id_BusinessPhone, phone);
    }

    public String getBusinessPhone()
    {
        return JSExecutor.getTextFromFiled(id_BusinessPhone);
    }

    public void setMobilePhone(String phone)
    {
        JSExecutor.setTextForField(id_MobilePhone, phone);
    }

    public String getMobilePhone()
    {
        return JSExecutor.getTextFromFiled(id_MobilePhone);
    }

    public void setHomePhone(String phone)
    {
        JSExecutor.setTextForField(id_HomePhone, phone);
    }

    public String getHomePhone()
    {
        return JSExecutor.getTextFromFiled(id_HomePhone);
    }

    public void setWebsite(String website)
    {
        JSExecutor.setTextForField(id_WebSite, website);
    }

    public String getWebsite()
    {
        return JSExecutor.getTextFromFiled(id_WebSite);
    }

    public void setEmail_1(String email)
    {
        JSExecutor.setTextForField(id_Email_1, email);
    }

    public String getEmail_1()
    {
        return JSExecutor.getTextFromFiled(id_Email_1);
    }

    public void setEmail_2(String email)
    {
        JSExecutor.setTextForField(id_Email_2, email);
    }

    public String getEmail_2()
    {
        return JSExecutor.getTextFromFiled(id_Email_2);
    }

    public void setEmail_3(String email)
    {
        JSExecutor.setTextForField(id_Email_3, email);
    }

    public String getEmail_3()
    {
        return JSExecutor.getTextFromFiled(id_Email_3);
    }

    public void setIMID(String imid)
    {
        JSExecutor.setTextForField(id_ImId, imid);
    }

    public String getIMID()
    {
        return JSExecutor.getTextFromFiled(id_ImId);
    }
                                                    /* * */

                                            /*  More subtab */
    public void setLanguage(String lang)
    {
        JSExecutor.setTextForField(id_Language, lang);
    }

    public String getLanguage()
    {
        return JSExecutor.getTextFromFiled(id_Language);
    }

    public void setHobbies(String hobbies)
    {
        JSExecutor.setTextForField(id_Hobbies, hobbies);
    }

    public String getHobbies()
    {
        return JSExecutor.getTextFromFiled(id_Hobbies);
    }

    public void setGender(String gender)
    {
        JSExecutor.setTextForSelect(id_Gender, gender);
    }

    public String getGender()
    {
        return JSExecutor.getTextFromSelect(id_Gender);
    }
                                                    /* * */

    public void clickProfileSubtab()
    {
        JSExecutor.clickByElement(id_ProfileSubtab);
        System.out.println("Profile subtab was clicked");
    }

    public void clickContactsSubtab()
    {
        JSExecutor.clickByElement(id_ContactsSubtab);
        System.out.println("Contacts subtab was clicked");
    }

    public void clickAddressSubtab()
    {
        JSExecutor.clickByElement(id_AddressSubtab);
        System.out.println("Address subtab was clicked");
    }

    public void clickMoreSubtab()
    {
        JSExecutor.clickByElement(id_MoreSubtab);
        System.out.println("More subtab was clicked");
    }

    /**
     * Click green button - save contact
     */
    public void clickAccept()
    {
        JSExecutor.clickByElement(id_Accept);
        System.out.println("Accept button was clicked");
    }

    public MoveContactPopup clickMove()
    {
        JSExecutor.clickByElement(id_Move);
        System.out.println("Move button was clicked");

        return new MoveContactPopup(driver);
    }

    public DeleteContactPopup clickDelete()
    {
        JSExecutor.clickByElement(id_Delete);
        System.out.println("Delete button was clicked");

        FunctionalTest.switchContext(Context.NATIVE);

        return new DeleteContactPopup(driver);
    }

}
