package tests.source;

import com.intradiem.LogReader;
import com.intradiem.helpers.Saver;
import org.junit.Assert;
import org.junit.Test;

import java.io.IOException;
import java.util.LinkedList;
import java.util.StringTokenizer;

/**
 * Applies only on WebSocket rules.
 */
public class CheckAbsenceOfWebSocketRule
{
    @Test
    public void checkAbsenceOfWebSocketRule() throws IOException
    {
        String rejectedWSRecord = LogReader.getRejectedWebsocketRecord();
        Assert.assertNotNull(rejectedWSRecord);

        System.out.println("[rejectedWSRecord] : " + rejectedWSRecord);

        String seq = getSEQ(rejectedWSRecord);

        LinkedList<String> recordsWithBody = LogReader.collectAllRecordsWithBody(Saver.getBodyOfRemovedRule());
        Assert.assertFalse(recordsWithBody.isEmpty());

        for( int i = 0; i < recordsWithBody.size(); i++ )
        {
            System.out.println("[recordsWithBody] : " + recordsWithBody.get(i));

            if( i % 2 == 0 )
            {
                Assert.assertTrue(recordsWithBody.get(i).endsWith(seq));
            }
        }
    }

    /**
     * <p>Get SEQ from rejectedWSRecord that looks like:</p>
     * <p>2018-09-21 12:00:39.130980-0500 [09788:010504] IAP51:SNIFFER: IAP: DPA WSRS SEQ=66 Rejected websocket frame by black-list frame rule 'WebSocket BlackList' for: Backend [10].</p>
     * <p>In this case method will return SEQ=66</p>
     * @param rejectedWSRecord
     * @return
     */
    private String getSEQ(String rejectedWSRecord)
    {
        StringTokenizer st = new StringTokenizer(rejectedWSRecord);
        while(st.hasMoreTokens())
        {
            String token = st.nextToken();
            if(token.contains("SEQ"))
            {
                return token;
            }
        }

        return null;
    }
}
