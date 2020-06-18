package tests.suites.qa;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;
import tests.source.web_driver_setup.ChromeHeadlessInternalQASetup;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        Login.class,
        VisitContainerPage.class,
        ContainerFilterTest.class,
        VisitLoginLogoutPage.class,
        VisitDeviceLogPage.class,
        DecodeTest.class,
        AddEmailGroup.class,
        AddAlert.class,
})

public class AuditTests extends ChromeHeadlessInternalQASetup
{

}
