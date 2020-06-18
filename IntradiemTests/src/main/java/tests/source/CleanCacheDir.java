package tests.source;

import com.intradiem.DirCleaner;
import com.intradiem.constants.Const;
import org.junit.Assert;
import org.junit.Test;

import java.io.File;
import java.io.IOException;

public class CleanCacheDir
{
    @Test
    public void cleanCacheDir() throws IOException, InterruptedException
    {
        File cacheDir = new File(Const.INTRADIEM_CACHE_DIR);

        DirCleaner.cleanDir(cacheDir);

        Assert.assertTrue(DirCleaner.isDirEmpty(cacheDir));

        System.out.println("Cache dir was cleaned");
    }
}
