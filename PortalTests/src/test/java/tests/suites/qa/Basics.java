package tests.suites.qa;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;
import tests.source.web_driver_setup.ChromeHeadlessInternalQASetup;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        Login.class,
        Basic_AddUser.class,
        Basic_AddConfig.class,
})

public class Basics extends ChromeHeadlessInternalQASetup
{

}
