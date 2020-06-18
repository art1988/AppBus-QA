package tests.suites;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        NoConnectRule.class,
        AllowAllRules.class,
        NoDeleteRule.class,
        NoOptionsRule.class,
        NoGETRootRule.class,
        NoGETDefaultRule.class,
        NoGETRouteRule.class,
        NoGETV1Rule.class,
        NoGETAgentExperienceRule.class,
        NoGETIconRule.class,
        NoGETCommonUIRule.class,
        NoGETOAuthRule.class,
        //NoGETEmsRule.class, // redundant rule because all GET /ems requests have headers: Connection: Upgrade, Upgrade: websocket
        NoGETClientRule.class,
        NoGETContentRule.class,
        NoGETWebResourceRule.class,
        NoPUTV1Rule.class,
        NoPOSTV1Rule.class,
        NoPATCHMessagesRule.class,
        NoGETscheduleSegmentsRule.class,
        NoFontsRule.class,
        NoMessageBlackListRule.class,
        NoWSAvroRule.class,
        NoGETMessagesRule.class,
})

// Main suite that contains other test suites. Run this to test all
public class MainSuite
{

}