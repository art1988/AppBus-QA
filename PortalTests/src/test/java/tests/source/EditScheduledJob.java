package tests.source;

import io.restassured.RestAssured;
import net.portal.constants.Const;
import net.portal.forms.AddJob;
import net.portal.forms.AddTrigger;
import net.portal.forms.ViewData;
import net.portal.pages.HeaderMenu;
import net.portal.pages.server_configuration.Scheduler;
import org.json.simple.JSONObject;
import org.junit.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.hasSize;

public class EditScheduledJob
{
    @Test
    public void editScheduledJob() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Scheduler schedulerPage = headerMenu.clickScheduler();

        String jobName = "AT sc_job",
               message = "count #3 AT";

        System.out.println("Edit Scheduled Job with name = " + jobName);

        AddJob addJobForm = schedulerPage.editJob(jobName);
        Thread.sleep(3_000);

        ViewData viewDataForm = addJobForm.viewMessage();
        Thread.sleep(3_000);

        viewDataForm.setValue(message);
        viewDataForm.clickOk();
        Thread.sleep(2_000);

        AddTrigger addTriggerForm = addJobForm.addTrigger();
        Thread.sleep(3_000);

        addTriggerForm.setType("simple");
        addTriggerForm.setInterval("10");
        addTriggerForm.setIntervalType("Sec"); // 10 sec interval
        addTriggerForm.setRepeatType("count"); // 3 counts
        addTriggerForm.setRepeatValue("3");

        addTriggerForm.clickSave();
        Thread.sleep(3_000);

        addJobForm.clickSave();

        System.out.println("Waiting for 40 sec...");
        Thread.sleep(40 * 1_000);

        System.out.println("Asserting response...");
        JSONObject requestParams = new JSONObject();

        requestParams.put("clientId", "AT_akm");

        RestAssured.useRelaxedHTTPSValidation();

        given().
                contentType("application/json; charset=utf-8").
                body(requestParams.toJSONString()).
                expect().statusCode(200).
         when().
                post("/edapt-pubsub/getMessages").
          then().
                assertThat().
                body("$", hasSize(3)).
                body("[0].topic", equalTo("AT_topic")).
                body("[0].message", equalTo(message)).
                body("[2].topic", equalTo("AT_topic")).
                body("[2].message", equalTo(message));
    }
}
