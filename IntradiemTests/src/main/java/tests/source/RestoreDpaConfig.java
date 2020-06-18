package tests.source;

import com.intradiem.ConfigChanger;
import com.intradiem.helpers.Saver;
import org.junit.Assert;
import org.junit.Test;

import java.io.IOException;

public class RestoreDpaConfig
{
    @Test
    public void restoreDpaConfig() throws IOException, InterruptedException
    {
        ConfigChanger.restoreDpaConfig();

        Thread.sleep(1_000);

        // Make sure that rule is still in dpa.config
        Assert.assertTrue(ConfigChanger.contains(Saver.getRemovedRule()));
    }
}
