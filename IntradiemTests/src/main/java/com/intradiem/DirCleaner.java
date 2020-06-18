package com.intradiem;

import org.apache.commons.io.FileUtils;
import org.aspectj.util.FileUtil;

import java.io.File;
import java.io.IOException;

public class DirCleaner
{
    public static void cleanDir(File dir) throws IOException
    {
        FileUtils.cleanDirectory(dir);
    }

    public static boolean isDirEmpty(File dir) throws InterruptedException
    {
        String[] listOfFiles = FileUtil.listFiles(dir);

        Thread.sleep(1_000);

        return ( listOfFiles.length == 0 ) ? true : false;
    }

}
