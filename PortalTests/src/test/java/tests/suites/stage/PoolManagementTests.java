package tests.suites.stage;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.AddPoolProvider;
import tests.source.AddVDI;
import tests.source.Login;
import tests.source.web_driver_setup.ChromeHeadlessInternalQASetup;
import tests.source.web_driver_setup.ChromeWindowedExternalStageSetup;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        Login.class,
        AddVDI.class,
        AddPoolProvider.class
})

public class PoolManagementTests extends ChromeWindowedExternalStageSetup
{

}
