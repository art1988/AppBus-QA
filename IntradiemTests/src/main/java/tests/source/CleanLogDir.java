package tests.source;

import com.intradiem.DirCleaner;
import com.intradiem.constants.Const;
import org.junit.Assert;
import org.junit.Test;

import java.io.File;
import java.io.IOException;

public class CleanLogDir
{
    @Test
    public void cleanLogDir() throws IOException, InterruptedException
    {
        File logDir = new File(Const.INTRADIEM_LOG_DIR);

        DirCleaner.cleanDir(logDir);

        Assert.assertTrue(DirCleaner.isDirEmpty(logDir));

        System.out.println("Log dir was cleaned");
    }
}
