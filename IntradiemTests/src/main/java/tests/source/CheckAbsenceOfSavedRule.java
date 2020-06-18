package tests.source;

import com.intradiem.LogReader;
import com.intradiem.helpers.Saver;
import org.junit.Assert;
import org.junit.Test;

import java.io.IOException;
import java.util.LinkedList;

/**
 * Check absence of saved rule.
 * Read log file and make sure it has Rejected HTTP and Forbidden By DPA lines with correct SEQ.
 * Applies only on http headers.
 */
public class CheckAbsenceOfSavedRule
{
    @Test
    public void checkAbsenceOfSavedRule() throws IOException
    {
        String seq = "";

        LinkedList<String> rejectedRecords  = LogReader.collectAllRejectedHttpRecords(),
                           forbiddenRecords = LogReader.collectAllForbiddenByDPARecords();

        // Assert that rejectedRecords and forbiddenRecords have at least one record
        Assert.assertFalse(rejectedRecords.isEmpty());
        Assert.assertFalse(forbiddenRecords.isEmpty());

        for( int rejIndex = 0, lineNum = 1, forbIndex = 0; rejIndex < rejectedRecords.size(); )
        {
            System.out.println("[rejectedRecords] : " + rejectedRecords.get(rejIndex++));
            lineNum++;

            if( lineNum == 2 )
            {
                String secondLine = rejectedRecords.get(rejIndex++);
                seq = secondLine.substring(secondLine.indexOf("SEQ")); // Save SEQ
                System.out.println("[rejectedRecords] : " + secondLine);
            }

            String thirdLine = rejectedRecords.get(rejIndex++);
            // Assert that in has correct rejected header
            Assert.assertTrue(thirdLine.contains(Saver.getHeaderOfRemovedRule()));

            System.out.println("[rejectedRecords] : " + thirdLine);
            lineNum = 1;

            // Assert that 'Forbidden By DPA' message has correct SEQ
            Assert.assertTrue(forbiddenRecords.get(forbIndex).endsWith(seq));

            System.out.println("[forbiddenRecords] : " + forbiddenRecords.get(forbIndex++));
            System.out.println("[forbiddenRecords] : " + forbiddenRecords.get(forbIndex++));
        }
    }
}
