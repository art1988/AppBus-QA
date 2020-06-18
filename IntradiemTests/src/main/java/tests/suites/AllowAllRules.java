package tests.suites;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        SendMessageToCheckAllRules.class,
        QuitIntradiemClient.class,
        CheckThatLogDoesntHaveRejectedRecords.class,
        CleanCacheDir.class,
        CleanLogDir.class
})

public class AllowAllRules
{

}
