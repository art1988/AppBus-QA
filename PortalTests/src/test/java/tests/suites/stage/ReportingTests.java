package tests.suites.stage;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;
import tests.source.web_driver_setup.ChromeHeadlessInternalQASetup;
import tests.source.web_driver_setup.ChromeWindowedExternalStageSetup;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        Login.class,
        VisitActiveUsersPage.class,
        VisitUserDetails.class,
        VisitTotalLogins.class,
        VisitVisitsPage.class,
        VisitCrashLog.class,
        VisitUserDevices.class,

//Vitaly's test that requires "Active Users" data
        ActiveUsersListCheck.class, //Datasensitive case //TODO: made changes after fixing of ED-3933
})

public class ReportingTests extends ChromeWindowedExternalStageSetup
{

}
