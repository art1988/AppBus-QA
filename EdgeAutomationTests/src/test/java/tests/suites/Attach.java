package tests.suites;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        AcceptAndLogin.class,
        AttachViaEmail.class,
        AttachViaDocuments.class,
        Reattach.class,
})

public class Attach extends FunctionalTest
{

}