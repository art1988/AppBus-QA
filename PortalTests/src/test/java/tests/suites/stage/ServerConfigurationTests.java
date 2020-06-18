package tests.suites.stage;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;
import tests.source.web_driver_setup.ChromeHeadlessInternalQASetup;
import tests.source.web_driver_setup.ChromeWindowedExternalStageSetup;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        Login.class,
        AddEnvironment.class,
        AddConfig.class,
        AddSetting.class,
        SettingsGroupFilter.class,
        RevertConfig.class,
})

public class ServerConfigurationTests extends ChromeWindowedExternalStageSetup
{

}
