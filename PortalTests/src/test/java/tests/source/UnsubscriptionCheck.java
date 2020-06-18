package tests.source;

import io.restassured.RestAssured;
import net.portal.constants.Const;
import net.portal.forms.AddTrigger;
import net.portal.pages.HeaderMenu;
import net.portal.pages.server_configuration.Scheduler;
import org.json.simple.JSONObject;
import org.junit.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.empty;

public class UnsubscriptionCheck
{
    @Test
    public void unsubscriptionCheck() throws InterruptedException
    {
        HeaderMenu headerMenu = new HeaderMenu(FunctionalTest.getDriver());

        Scheduler schedulerPage = headerMenu.clickScheduler();

        String jobName = "AT sc_job";

        System.out.println("Add trigger for unsubscribed job with name = " + jobName);

        AddTrigger addTriggerForm = schedulerPage.addTrigger(jobName);
        Thread.sleep(3_000);

        addTriggerForm.setType("simple");
        addTriggerForm.setInterval("7000"); // 7000 millisec = 7 sec
        addTriggerForm.setIntervalType("Ms");
        addTriggerForm.setRepeatType("forever");
        addTriggerForm.clickSave();

        System.out.println("Waiting for 16 sec...");
        Thread.sleep(16 * 1_000);

        System.out.println("Asserting that response is empty...");
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
                body("$", empty());
    }
}
