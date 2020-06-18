package tests.suites;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        RemoveMessageBlackListRule.class,
        SimpleLaunchAndExitIntradiemClient.class,
        RestoreDpaConfig.class,
        CleanCacheDir.class,
        CleanLogDir.class
})

public class NoMessageBlackListRule
{

}
