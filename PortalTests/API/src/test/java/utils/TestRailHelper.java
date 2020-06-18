
package utils;

import com.codepine.api.testrail.TestRail;
import com.codepine.api.testrail.model.*;

import java.util.Date;
import java.util.List;

public class TestRailHelper {
	public static TestRail testRail;

	public TestRailHelper() {
		String testRailUrl = PropertyReader.getInstance().getProperty("url");
		String testRailEmail = PropertyReader.getInstance().getProperty("email");
		String testRailPassword = System.getProperty("password");
		String testRailAppName = PropertyReader.getInstance().getProperty("applicationName");
		testRail = TestRail.builder(testRailUrl, testRailEmail, testRailPassword).applicationName(testRailAppName).build();
	}


	public List<Case> getCasesFromTestRail(Integer projectId, Integer suiteId) {
		List<CaseField> customCaseFields = testRail.caseFields().list().execute();
		return testRail.cases().list(projectId, suiteId, customCaseFields).execute();
		//return testRail.cases().get(caseId, customCaseFields).execute();
	}

	public Integer createTestRun(Integer projectId, Integer suiteId, String url) {
		Run run = new Run().setName("Teamcity test run " + url +" "+ new Date())
				.setSuiteId(suiteId);
		Run executeRun = testRail.runs().add(projectId, run).execute();
		return executeRun.getId();
	}
	public void closeTestRun(Integer runId) {
		testRail.runs().close(runId).execute();
	}

	public void updateTestRunStatus(Integer runId, Integer caseId, String comment, Integer statusId) {
		Result res = new Result().setStatusId(statusId)
				.setComment(comment);
		List<ResultField> resultFields = testRail.resultFields().list().execute();

		testRail.results().addForCase(runId, caseId, res, resultFields).execute();
	}


}
