package tests.suites;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        RemoveGETScheduleSegmentsRule.class,
        SendMessageToCheckAbsenceOfGETScheduleSegmentsRule.class,
        QuitIntradiemClient.class,
        CheckAbsenceOfSavedRule.class,
        CleanCacheDir.class,
        CleanLogDir.class,
        RestoreDpaConfig.class
})

public class NoGETscheduleSegmentsRule
{

}
