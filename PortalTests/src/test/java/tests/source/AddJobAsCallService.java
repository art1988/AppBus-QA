package tests.source;

import io.restassured.RestAssured;
import net.portal.forms.AddJob;
import net.portal.forms.AddTrigger;
import net.portal.forms.ViewData;
import net.portal.pages.DeleteJob;
import net.portal.pages.HeaderMenu;
import net.portal.pages.server_configuration.Scheduler;
import org.json.simple.JSONObject;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.JavascriptExecutor;

import java.util.ArrayList;
import java.util.HashMap;

import static io.restassured.RestAssured.given;

public class AddJobAsCallService
{
    @Test
    public void addJobAsCallService() throws InterruptedException
    {
        ArrayList timestampBefore = getTimestamp();

        System.out.println("timestampBefore = " + timestampBefore);

        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Scheduler schedulerPage = headerMenu.clickScheduler();

        AddJob addJobForm = schedulerPage.addJob();
        Thread.sleep(3_000);

        addJobForm.setAction("Call service");

        JSONObject requestParams = new JSONObject();

        requestParams.put("requestMethod", "GET");
        requestParams.put("substituteHostAndPortToLocal", true);
        requestParams.put("pathParameters", new HashMap<>()); // add as "pathParameters": {}
        requestParams.put("queryParameters", new HashMap<>());
        requestParams.put("headers", new HashMap<>());
        requestParams.put("body", new HashMap<>());

        String jobName = "FakeTEST_AT",
               environment = "edapt-demo",
               name = "Ex_REST",
               project = "Artur";

        addJobForm.setName(jobName);

        ViewData viewDataForm = addJobForm.viewEnvironment();
        Thread.sleep(3_000);
        viewDataForm.setValue(environment);
        viewDataForm.clickOk();
        Thread.sleep(2_000);

        viewDataForm = addJobForm.viewApiData();
        Thread.sleep(3_000);
        viewDataForm.setValue(requestParams.toJSONString());
        viewDataForm.clickOk();
        Thread.sleep(2_000);

        viewDataForm = addJobForm.viewName();
        Thread.sleep(3_000);
        viewDataForm.setValue(name);
        viewDataForm.clickOk();
        Thread.sleep(2_000);

        viewDataForm = addJobForm.viewProject();
        Thread.sleep(3_000);
        viewDataForm.setValue(project);
        viewDataForm.clickOk();
        Thread.sleep(2_000);

        AddTrigger addTrigger = addJobForm.addTrigger();
        Thread.sleep(2_000);

        addTrigger.setType("simple");
        addTrigger.setInterval("4");
        addTrigger.setIntervalType("Sec"); // wait 4 sec
        addTrigger.setRepeatType("count"); // 1 count
        addTrigger.setRepeatValue("1");

        addTrigger.clickSave();
        Thread.sleep(5_000);

        addJobForm.clickSave();

        System.out.println("Waiting for 14 sec...");
        Thread.sleep(14 * 1_000);

        ArrayList timestampAfter = getTimestamp();

        System.out.println("timestampAfter = " + timestampAfter);

        System.out.println("Asserting that timestamps are different...");
        Assert.assertFalse(timestampBefore.equals(timestampAfter));

        schedulerPage.clickRefresh();
        Thread.sleep(1_000);

        // Delete just created job
        DeleteJob deleteJob = schedulerPage.deleteJob(jobName);
        Thread.sleep(1_000);

        deleteJob.clickYes();
        Thread.sleep(1_000);

        // Make sure that job was deleted
        Assert.assertFalse((boolean) ((JavascriptExecutor) FunctionalTest.getDriver()).executeScript("return $('#schedulerForm\\\\:jobsTable_data tr td:contains(\"" + jobName + "\")').is(':visible')"));
    }

    private ArrayList getTimestamp()
    {
        RestAssured.baseURI = "https://api.appery.io/rest/1/apiexpress/api/";
        RestAssured.useRelaxedHTTPSValidation();

        ArrayList timestamp =
                given().
                        urlEncodingEnabled(false).
                        contentType("application/json; charset=utf-8").
                        queryParam("apiKey", "a981060b-fdc5-4b4f-9083-107371490cfb").
                        queryParam("where", "%7B%0A%7D").
                        queryParam("offset", "").
                        queryParam("limit", "").
                        queryParam("count", "false").
                        queryParam("sort", "").
                        expect().statusCode(200).
                 when().
                        get("/service-catalog").
                  then().
                        extract().path("timestamp");

        return timestamp;
    }
}
