package tests.source;

import com.intradiem.ConfigChanger;
import com.intradiem.constants.RuleArray;
import com.intradiem.helpers.Saver;
import org.json.simple.parser.ParseException;
import org.junit.Assert;
import org.junit.Test;

import java.io.IOException;

public class RemoveOptionsRule
{
    @Test
    public void removeOptionsRule() throws IOException, ParseException
    {
        ConfigChanger configChanger = new ConfigChanger();

        configChanger.makeCopyOfDpaConfig();

        String ruleComment = "Options WhiteList";
        configChanger.removeRule(RuleArray.MSG_WHITE, ruleComment);

        Assert.assertFalse(ConfigChanger.contains(ruleComment));

        Saver.setRemovedRule(ruleComment);

        // Remove ^ wildcard from header because in logs there is no ^ in front of OPTIONS header
        Saver.setUniqueHeader(Saver.getHeaderOfRemovedRule().substring(1));
    }
}
