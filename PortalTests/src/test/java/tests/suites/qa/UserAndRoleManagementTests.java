package tests.suites.qa;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;
import tests.source.web_driver_setup.ChromeHeadlessInternalQASetup;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        Login.class,
        IterateControllerType.class,
        UniquenessOfStratum.class,
        UniquenessOfAuthenticationGroup.class,
        UniquenessOfContext.class,
        UniquenessOfPolicy.class,
        AddNavigationItem.class,
        AddApplication.class,
        PropertiesForUIGroup.class,
        AddNavItemOnNavigationPage.class,
        AddComplexNavItem.class,
        DownloadUploadPolicy.class,
        NavigationTreePreview.class,
        MoveNavigationItems.class,
        NavigationItemOverride.class,
        //UploadNavigationItem.class, // ED-3873

//Vitaly's tests:
        NavigationMultipleValueIcon.class, //C4984 case on testrail
        NavigationItemAssigDetailsCheck.class, //C5550 case on testrail
        NavigationChildItems1.class, //C17941 case on testrail
        NavigationChildItems2.class, //C17942 case on testrail
        //NavigationChildItemsCheck.class, //C7489 	Navigation Item + Navigation: Create Parent + Child Items, add to Tree
})

public class UserAndRoleManagementTests extends ChromeHeadlessInternalQASetup
{

}
