package tests.suites;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        RemoveGETV1Rule.class,
        LaunchIntradiemAndCheckPresenceOfPopup.class,
        CheckAbsenceOfSavedRule.class,
        RestoreDpaConfig.class,
        CleanCacheDir.class,
        CleanLogDir.class
})

public class NoGETV1Rule
{

}
