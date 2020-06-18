package tests.source;

import com.intradiem.ConfigChanger;
import com.intradiem.constants.RuleArray;
import com.intradiem.helpers.Saver;
import org.json.simple.parser.ParseException;
import org.junit.Assert;
import org.junit.Test;

import java.io.IOException;

public class RemoveGETDefaultRule
{
    @Test
    public void removeGETDefaultRule() throws IOException, ParseException
    {
        ConfigChanger configChanger = new ConfigChanger();

        configChanger.makeCopyOfDpaConfig();

        String ruleComment = "Default WhiteList";
        configChanger.removeRule(RuleArray.MSG_WHITE, ruleComment);

        Assert.assertFalse(ConfigChanger.contains(ruleComment));

        Saver.setRemovedRule(ruleComment);
    }
}
