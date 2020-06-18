package apiTests;

import com.codepine.api.testrail.model.*;
import org.testng.annotations.Test;
import utils.RequestSender;
import utils.TestRailHelper;
import org.apache.commons.lang3.RandomStringUtils;

import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class ApiTest {
	private static final String prefix = "TC_";
	private static final String random_parameter = "<random>";
	private static Map<String, String> urlRandomMap = new HashMap<>();

	@Test
	public void testCaseFromTestRail() {
		Integer projectId = Integer.valueOf(System.getProperty("projectId"));
		Integer suiteId = Integer.valueOf(System.getProperty("suiteId"));
		String serverUrl = System.getProperty("serverUrl");
		TestRailHelper testRail = new TestRailHelper();

		boolean atListOneFail = false;
		List<Case> testCases = testRail.getCasesFromTestRail(projectId, suiteId);
		Integer runId = testRail.createTestRun(projectId, suiteId, serverUrl);
		for (Case testCase : testCases) {
			String title = testCase.getTitle();
			String body = (String) testCase.getCustomFields().get("steps");
			String expected = (String) testCase.getCustomFields().get("expected");
			String url = extractUrl(title, serverUrl);
			String comment = "executed by teamcity";
			ApiTestResult testResult = createRequestAndGetResponseString(title, body, expected, url, comment);
			testRail.updateTestRunStatus(runId, testCase.getId(), testResult.getComment(), testResult.getStatus());
			if (!atListOneFail && testResult.getStatus() == 5) {
				atListOneFail = true;
			}
		}
		testRail.closeTestRun(runId);
		assert !atListOneFail;
	}


	private String extractUrl(String title, String serverUrl) {
		String url = title.substring(title.indexOf("{{URL}}"));
		url = url.replace("{{URL}}", serverUrl);
		return url;
	}

	private ApiTestResult createRequestAndGetResponseString(String title, String body, String expectedResponse,
															String url, String comment) {
		String response = "";
		ApiTestResult res = new ApiTestResult();
		if (title.startsWith("GET")) {
			try {
				response = RequestSender.getInstance().sendGet(url);
				System.out.println("\nresponse " + response + "\n");
			} catch (Exception e) {
				e.printStackTrace();
			}
		} else if (title.startsWith("POST")) {
			try {
				if (body.contains(random_parameter)) {
					String randStr = prefix + RandomStringUtils.randomAlphanumeric(5);
					body = body.replace(random_parameter, randStr);
					expectedResponse = expectedResponse.replace(random_parameter, randStr);
					urlRandomMap.put(url, randStr);
				}
				response = RequestSender.getInstance().sendPost(url, body);
			} catch (Exception e) {
				e.printStackTrace();
			}
		} else if (title.startsWith("DEL")) {
			try {
				if (title.contains(random_parameter)) {
					String postUrl = url.substring(0, url.lastIndexOf("/"));
					System.out.println("postUrl " + postUrl);
					if (urlRandomMap.containsKey(postUrl)) {
						url = url.replace(random_parameter, urlRandomMap.get(postUrl));
						System.out.println("new url " + url);
						response = RequestSender.getInstance().sendDel(url);
						expectedResponse = expectedResponse.replace(random_parameter, urlRandomMap.get(postUrl));
						System.out.println("response " + response);
					}
				} else {
					response = RequestSender.getInstance().sendDel(url);
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		if (compareJsons(response, expectedResponse)) {
			res.setStatus(1);
			res.setComment(comment);
			return res;
		} else {
			res.setStatus(5);
			res.setComment(comment + "\n" + response);
			return res;
		}
	}

	private boolean compareJsons(String json1, String json2) {
		if (json1 == null && json2 == null) {
			return true;
		}
		if (json1.replaceAll("\\s+", "").equals(json2.replaceAll("\\s+", ""))) {
			return true;
		}
		return json1.equals(json2);

//		JSONObject obj1 = new JSONObject(json1);
//		JSONObject obj2 = new JSONObject(json2);

}

class ApiTestResult {
	int status;
	String comment;

	public int getStatus() {
		return status;
	}

	public void setStatus(int status) {
		this.status = status;
	}

	public String getComment() {
		return comment;
	}

	public void setComment(String comment) {
		this.comment = comment;
	}
}

}
