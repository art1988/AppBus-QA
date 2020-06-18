package tests.suites.stage;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;
import tests.source.web_driver_setup.ChromeHeadlessInternalQASetup;
import tests.source.web_driver_setup.ChromeWindowedExternalStageSetup;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        Login.class,
        VisitContainerPage.class,
        ContainerFilterTest.class,
        VisitLoginLogoutPage.class,
        VisitDeviceLogPage.class,
        //DecodeTest.class,
        AddEmailGroup.class,
        AddAlert.class,
})

public class AuditTests extends ChromeWindowedExternalStageSetup
{

}
