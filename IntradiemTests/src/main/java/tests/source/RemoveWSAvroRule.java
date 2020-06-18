package tests.source;

import com.intradiem.ConfigChanger;
import com.intradiem.constants.RuleArray;
import com.intradiem.helpers.Saver;
import org.json.simple.parser.ParseException;
import org.junit.Assert;
import org.junit.Test;

import java.io.IOException;

public class RemoveWSAvroRule
{
    @Test
    public void removeWSAvroRule() throws IOException, ParseException
    {
        ConfigChanger configChanger = new ConfigChanger();

        configChanger.makeCopyOfDpaConfig();

        String ruleComment = "WebSocket Avro WhiteList";
        configChanger.removeRule(RuleArray.WS_WHITE, ruleComment);

        Assert.assertFalse(ConfigChanger.contains(ruleComment));

        Saver.setRemovedRule(ruleComment);

        // Remove * wildcard in this rule
        Saver.setBodyOfRemovedRule(Saver.getBodyOfRemovedRule().replace("*",""));

        // Do not start MessageListener because user is unable to receive message without 'WebSocket Avro' rule
        IntradiemClientListener.doNotStartMessageListener();
    }
}
