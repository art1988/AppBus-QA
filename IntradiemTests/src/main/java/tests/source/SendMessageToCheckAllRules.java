package tests.source;

import com.intradiem.helpers.Saver;
import org.apache.maven.surefire.junitcore.JUnitCoreParameters;
import org.apache.maven.surefire.junitcore.pc.ParallelComputer;
import org.apache.maven.surefire.junitcore.pc.ParallelComputerBuilder;
import org.apache.maven.surefire.report.DefaultConsoleReporter;
import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;

import java.util.Properties;

public class SendMessageToCheckAllRules
{
    @Test
    public void allowAllRules()
    {
        Saver.addDesiredMessageInFIFO("AllowAllRules");
        Saver.addDesiredMessageInFIFO("quit");

        Class[] clazz = {IntradiemClientListener.class, IntradiemMessageSender.class};

        // Run junit with concurrency configured
        Properties properties = new Properties();

        properties.put(JUnitCoreParameters.PARALLEL_KEY, "classes");
        properties.put(JUnitCoreParameters.THREADCOUNT_KEY, "2");
        properties.put(JUnitCoreParameters.PERCORETHREADCOUNT_KEY, "false");

        JUnitCoreParameters parameters = new JUnitCoreParameters(properties);
        ParallelComputerBuilder builder = new ParallelComputerBuilder(new DefaultConsoleReporter(System.out), parameters);

        ParallelComputer computer = builder.buildComputer();
        // Run tests in parallel
        Result result = JUnitCore.runClasses(computer, clazz);
    }
}
