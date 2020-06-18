package tests.suites;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        RemoveWSAvroRule.class,
        SendSimpleQuitMessage.class, // send any message - in this case - quit. But user won't receive it without avro rule
        QuitIntradiemClient.class,
        CheckAbsenceOfWebSocketRule.class,
        CleanCacheDir.class,
        CleanLogDir.class,
        RestoreDpaConfig.class,
})

public class NoWSAvroRule
{

}
