package tests.suites.stage;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.Basic_AddConfig;
import tests.source.Basic_AddUser;
import tests.source.Login;
import tests.source.web_driver_setup.ChromeHeadlessInternalQASetup;
import tests.source.web_driver_setup.ChromeWindowedExternalStageSetup;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        Login.class,
        Basic_AddUser.class,
        Basic_AddConfig.class,
})

public class Basics extends ChromeWindowedExternalStageSetup
{

}
