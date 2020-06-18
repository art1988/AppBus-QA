package tests.source;

import com.appbus.pages.ActiveHamburgerMenu;
import com.appbus.pages.constants.Context;
import com.appbus.pages.email_related.Email;
import com.appbus.pages.menuItems.CommunicationsMenuItems;
import com.appbus.pages.tabs.MailTab;
import org.junit.Test;

public class FancyEmail
{
    @Test
    public void fancyEmail() throws InterruptedException
    {
        ActiveHamburgerMenu hamburgerMenu = new ActiveHamburgerMenu(FunctionalTest.getDriver());
        CommunicationsMenuItems commMenuItems = hamburgerMenu.clickCommunications();
        MailTab mailTab = commMenuItems.clickMail();
        Email email = mailTab.clickNewEmailButton();

        FunctionalTest.switchContext(Context.WEBVIEW);
        Thread.sleep(4_000);

        Email.RichEditor richEditor = email.clickAa();

        richEditor.clickRichEditorControl(Email.RichEditor.class_bold, "Bold on");
        email.setMessageBody("i'm bold text\n");
        richEditor.clickRichEditorControl(Email.RichEditor.class_bold, "Bold off");

        richEditor.clickRichEditorControl(Email.RichEditor.class_italic, "Italic on");
        email.setMessageBody("and i'm italic text\n");
        richEditor.clickRichEditorControl(Email.RichEditor.class_italic, "Italic off");

        richEditor.clickRichEditorControl(Email.RichEditor.class_underline, "Underline on");
        email.setMessageBody("It's underline here\n");
        richEditor.clickRichEditorControl(Email.RichEditor.class_underline, "Underline off");

        Thread.sleep(5_000);

        richEditor.clickRichEditorControl(Email.RichEditor.class_quote, "Quote on");
        email.setMessageBody(".....oh, i'm a quote (c)");
        richEditor.clickRichEditorControl(Email.RichEditor.class_quote, "Quote off");
        email.setMessageBody("\n");

        Thread.sleep(5_000);

        richEditor.clickRichEditorControl(Email.RichEditor.class_ul, "Ul on");
        email.setMessageBody("ul is here one");
        email.setMessageBody("\n");
        email.setMessageBody("ul is here two\n");
        email.setMessageBody("\n");
        richEditor.clickRichEditorControl(Email.RichEditor.class_ul, "Ul off");

        Thread.sleep(10_000);
    }
}
