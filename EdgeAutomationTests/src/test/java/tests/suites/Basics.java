package tests.suites;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;


@RunWith(Suite.class)
@Suite.SuiteClasses({
        AcceptAndLogin.class,

        //FancyEmail.class,
        // Block of email related tests
        SendNewEmail.class,
        DeleteEmail.class,
        DraftEmail.class,
        MoveAndMarkEmail.class,

        //
        Invitees.class,
        Calendar.class,
        AllEvents.class,
        Contacts.class,
        Logout.class,
        Lock.class,
        Documents.class,
        MarketData.class,
        Home.class,
        Search.class,
        NewContactForMail.class,
        EventAllDay.class,
        EventAlert.class,
})


public class Basics extends FunctionalTest
{

}

