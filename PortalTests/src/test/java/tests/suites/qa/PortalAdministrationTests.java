package tests.suites.qa;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;
import tests.source.web_driver_setup.ChromeHeadlessInternalQASetup;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        Login.class,
        AddUserAndUserGroup.class,
        AddRole.class,
        MakeCopyOfRole.class,
        LandingPermissionCheck.class,
        DBAuditCheck.class,
        // RoleFilter.class // ED-4368, ED-4369
})

public class PortalAdministrationTests extends ChromeHeadlessInternalQASetup
{

}
