package tests.suites.qa;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;
import tests.source.web_driver_setup.ChromeHeadlessInternalQASetup;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        Login.class,

//Vitaly's tests:
        Basic_Check_All_Menu.class,
})

public class BasicMenuTest extends ChromeHeadlessInternalQASetup
{

}