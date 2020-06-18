package tests.source;

import io.restassured.RestAssured;
import net.portal.constants.Const;
import org.json.simple.JSONObject;
import org.junit.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;

public class UnsubscribeFromTopic
{
    @Test
    public void unsubscribeFromTopic()
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
                post("/edapt-pubsub/unsubscribe").
          then().
                assertThat().
                body("status", equalTo("SUCCESS"));

        System.out.println("Was successfully unsubscribed from topic: AT_topic");
    }
}
