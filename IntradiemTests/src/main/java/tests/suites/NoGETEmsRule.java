package tests.suites;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        RemoveGETEmsRule.class,
        SendSimpleQuitMessage.class,
        QuitIntradiemClient.class,
        CheckAbsenceOfSavedRule.class,
        CleanCacheDir.class,
        CleanLogDir.class,
        RestoreDpaConfig.class
})

// This is redundant rule
public class NoGETEmsRule
{

}
