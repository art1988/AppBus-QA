package tests.suites;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        AcceptAndLogin.class,
        RepeatEventEveryDay.class,
        RepeatEventEveryWeek.class,
        RepeatEventEveryMonth.class,
        RepeatEventEveryYear.class,
})

public class EventRepeat extends FunctionalTest
{

}
