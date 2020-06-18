package tests.suites.stage;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;
import tests.source.web_driver_setup.ChromeHeadlessInternalQASetup;
import tests.source.web_driver_setup.ChromeWindowedExternalStageSetup;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        SubscribeToTopic.class,
        Login.class,
        AddJobAndCheckOneCountTrigger.class, // Publish event action
        EditScheduledJob.class,
        UnsubscribeFromTopic.class,
        UnsubscriptionCheck.class,
        DeleteScheduledJob.class,
        AddJobAsCallService.class, // Call service action
})

public class SchedulerTests extends ChromeWindowedExternalStageSetup
{

}
