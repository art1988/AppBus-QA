package tests.suites.qa;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import tests.source.*;
import tests.source.web_driver_setup.ChromeHeadlessInternalQASetup;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        Login.class,
        AddProject.class,
        AddJSLibrary.class,
        AddJavaLibrary.class,
        AddRESTService.class,
        AddJSService.class,
        ServiceDashboardTest.class,
        DeleteProject.class,
        AddDbConnection.class,

//Vitaly's tests:
          TestUICatalog.class, //was C4983 case on testrail //now it checks ionic 4 applying
          TestServiceDashboard.class, //C4993 case on testrail: "Service Dashboard: Check main functions"
})

public class ServiceManagementTests extends ChromeHeadlessInternalQASetup
{

}