C:
cd C:\automation\QA\API\apiTestsFromTestRail-master\apiTestsFromTestRail-master
mvn clean test -Dprops="testRailAppBus.properties" -DprojectId="5" -DsuiteId="22" -DserverUrl="https://dev.e-dapt.net:5554" -Dpassword="maps511"