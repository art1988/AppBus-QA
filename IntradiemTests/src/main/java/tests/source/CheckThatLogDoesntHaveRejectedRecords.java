package tests.source;

import com.intradiem.LogReader;
import org.junit.Assert;
import org.junit.Test;

import java.io.IOException;

public class CheckThatLogDoesntHaveRejectedRecords
{
    @Test
    public void checkThatLogDoesntHaveRejectedRecords() throws IOException
    {
        Assert.assertTrue(LogReader.collectAllRejectedHttpRecords().isEmpty());
        Assert.assertTrue(LogReader.collectAllForbiddenByDPARecords().isEmpty());
    }
}
