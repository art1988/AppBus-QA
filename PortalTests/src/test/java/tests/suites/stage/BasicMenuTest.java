package tests.suites.stage;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.Basic_Check_All_Menu;
import tests.source.Login;
import tests.source.web_driver_setup.ChromeHeadlessInternalQASetup;
import tests.source.web_driver_setup.ChromeWindowedExternalStageSetup;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        Login.class,

//Vitaly's tests:
        Basic_Check_All_Menu.class,
})

public class BasicMenuTest extends ChromeWindowedExternalStageSetup
{

}