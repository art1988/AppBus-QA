package tests.suites;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        RemoveGETRouteRule.class,
        SimpleLaunchAndExitIntradiemClient.class,
        CheckAbsenceOfSavedRule.class,
        CleanCacheDir.class,
        CleanLogDir.class,
        RestoreDpaConfig.class
})

public class NoGETRouteRule
{

}
