package tests.source;

import io.restassured.RestAssured;
import org.json.simple.JSONObject;
import org.junit.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;

public class SubscribeToTopic
{
    @Test
    public void subscribeToTopic()
    {
        JSONObject requestParams = new JSONObject();

        requestParams.put("clientId", "AT_akm");
        requestParams.put("topic", "AT_topic");

        RestAssured.useRelaxedHTTPSValidation();

        given().
                contentType("application/json; charset=UTF-8").
                body(requestParams.toJSONString()).
                expect().statusCode(200).
         when().
                post("/edapt-pubsub/subscribe").
          then().
                assertThat().
                body("status", equalTo("SUCCESS"));

        System.out.println("Was successfully subscribed to topic: AT_topic");
    }
}
