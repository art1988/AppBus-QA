package tests.source;

import com.intradiem.ConfigChanger;
import com.intradiem.constants.RuleArray;
import com.intradiem.helpers.Saver;
import org.json.simple.parser.ParseException;
import org.junit.Assert;
import org.junit.Test;

import java.io.IOException;

public class RemoveMessageBlackListRule
{
    @Test
    public void removeMessageBlackListRule() throws IOException, ParseException
    {
        ConfigChanger configChanger = new ConfigChanger();

        configChanger.makeCopyOfDpaConfig();

        // First, remove messageBlackList rule (single rule)
        String ruleComment = "Common BackList";
        configChanger.removeRule(RuleArray.MSG_BLACK, ruleComment);

        Saver.setRemovedRule(ruleComment);

        Assert.assertFalse(ConfigChanger.contains(ruleComment));

        // Second, remove Connect WhiteList rule
        ruleComment = "Connect WhiteList";
        configChanger.removeRule(RuleArray.MSG_WHITE, ruleComment);

        Assert.assertFalse(ConfigChanger.contains(ruleComment));

        System.out.println("Checking that Intradiem Client will open without warning popup (because Connect rule was removed)...");
    }
}
