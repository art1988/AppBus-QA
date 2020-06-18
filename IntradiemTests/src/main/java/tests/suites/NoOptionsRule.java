package tests.suites;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        RemoveOptionsRule.class,
        LaunchIntradiemAndCheckPresenceOfPopup.class,
        CheckAbsenceOfSavedRule.class,
        CleanCacheDir.class,
        CleanLogDir.class,
        RestoreDpaConfig.class,
})

public class NoOptionsRule
{

}
