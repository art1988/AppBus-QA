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
import static org.hamcrest.Matchers.*;

public class AddJobAndCheckOneCountTrigger
{
    @Test
    public void addJobAndCheckOneCountTrigger() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Scheduler schedulerPage = headerMenu.clickScheduler();

        AddJob addJobForm = schedulerPage.addJob();
        Thread.sleep(3_000);

        String jobName = "AT sc_job",
               description = "job_description",
               topic = "AT_topic",
               message = "Hello from Scheduler !!! [AT]";

        addJobForm.setName(jobName);
        addJobForm.setAction("Publish event");
        addJobForm.setDescription(description);

        ViewData viewDataForm = addJobForm.viewTopic();
        Thread.sleep(3_000);
        viewDataForm.setValue(topic);
        viewDataForm.clickOk();
        Thread.sleep(2_000);

        viewDataForm = addJobForm.viewMessage();
        Thread.sleep(3_000);
        viewDataForm.setValue(message);
        viewDataForm.clickOk();
        Thread.sleep(2_000);

        AddTrigger addTriggerForm = addJobForm.addTrigger();
        Thread.sleep(3_000);

        addTriggerForm.setType("simple");
        addTriggerForm.setInterval("30");
        addTriggerForm.setIntervalType("Sec"); // wait for 30 sec
        addTriggerForm.setRepeatType("count"); // 1 count
        addTriggerForm.setRepeatValue("1");

        addTriggerForm.clickSave();
        Thread.sleep(3_000);

        addJobForm.clickSave();

        System.out.println("Waiting for 45 sec...");
        Thread.sleep(45 * 1_000);


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
                body("$", hasSize(1)).
                body("[0].topic", equalTo("AT_topic")).
                body("[0].message", equalTo(message));

        System.out.println("Waiting for another 45 sec...");
        Thread.sleep(45 * 1_000);

        System.out.println("Asserting that response is empty...");

        given().
                contentType("application/json; charset=utf-8").
                body(requestParams.toJSONString()).
                expect().statusCode(200).
        when().
               post("/edapt-pubsub/getMessages").
         then().
                assertThat().
                body("$", empty());
    }
}
