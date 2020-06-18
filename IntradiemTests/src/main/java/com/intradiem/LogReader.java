package com.intradiem;

import com.intradiem.constants.Const;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.LinkedList;

public class LogReader
{
    /**
     * <p>Collect all Rejected HTTP records.</p>
     * <p>Consists of 3 records that looks like:</p>
     *
     * <ol>
     * <li>2018-09-13 15:00:05.825434-0500 [02188:011252] IAP51:SNIFFER: IAP: DPA REQ SEQ=3 Rejected HTTP message by black-list header rule 'Common BackList' for: Session [0].</li>
     * <li>2018-09-13 15:00:05.825434-0500 [02188:011252] IAP51:SNIFFER: IAP: REQ SEQ=3</li>
     * <li>GET /Default.aspx?ReturnUrl=%2f HTTP/1.1</li>
     * </ol>
     * @return list of all Rejected HTTP records
     * @throws IOException
     */
    public static LinkedList<String> collectAllRejectedHttpRecords() throws IOException
    {
        LinkedList<String> rejectedRecords = new LinkedList<>();
        BufferedReader bufferedReader = new BufferedReader(new FileReader(Const.INTRADIEM_LOG_DIR + getUserFilterFilename()));

        String line;
        while( ( line = bufferedReader.readLine() ) != null )
        {
            if (line.contains("Rejected HTTP"))
            {
                rejectedRecords.add(line);
                rejectedRecords.add(bufferedReader.readLine()); // get 2nd line
                rejectedRecords.add(bufferedReader.readLine()); // get 3rd line
            }
        }

        bufferedReader.close();

        return rejectedRecords;
    }

    /**
     * <p>Get Rejected websocket line that looks like:</p>
     * <p>2018-09-25 14:30:56.656236-0500 [09484:003972] IAP51:SNIFFER: IAP: DPA WSRS SEQ=66 Rejected websocket frame by black-list frame rule...</p>
     * @return
     * @throws IOException
     */
    public static String getRejectedWebsocketRecord() throws IOException
    {
        BufferedReader bufferedReader = new BufferedReader(new FileReader(Const.INTRADIEM_LOG_DIR + getUserFilterFilename()));

        try
        {
            String line;
            while( ( line = bufferedReader.readLine() ) != null )
            {
                if( line.contains("Rejected websocket") )
                {
                    return line;
                }
            }
        }
        finally
        {
            bufferedReader.close();
        }

        return null;
    }

    /**
     * <p>Collect all records with specific body</p>
     * <p>Consists of 2 records that looks like:</p>
     *
     * <ol>
     * <li>2018-09-25 14:30:56.656236-0500 [09484:003972] IAP51:SNIFFER: IAP: RSB SEQ=66</li>
     * <li>\x82~\x04HObj\x01\x02\x16avro.schema\xE6\x0E{"type":"record","name":"Message","namespace":"com.intradiem.enterprise.avro.resources",...</li>
     * </ol>
     * @param body
     * @return
     * @throws IOException
     */
    public static LinkedList<String> collectAllRecordsWithBody(String body) throws IOException
    {
        LinkedList<String> recordsWithBody = new LinkedList<>();
        BufferedReader bufferedReader = new BufferedReader(new FileReader(Const.INTRADIEM_LOG_DIR + getUserFilterFilename()));

        String line,
               prevLine = "";
        while( ( line = bufferedReader.readLine() ) != null )
        {
            if( line.contains(body) )
            {
                recordsWithBody.add(prevLine);
                recordsWithBody.add(line);
            }
            else
            {
                prevLine = line;
            }
        }

        bufferedReader.close();

        return recordsWithBody;
    }

    /**
     * <p>Collect all Forbidden By DPA records.</p>
     * <p>Consists of 2 records that looks like:</p>
     *
     * <ol>
     * <li>2018-09-13 15:00:05.825434-0500 [02188:011252] IAP51:SNIFFER: IAP: RES SEQ=3</li>
     * <li>HTTP/1.1 418 Forbidden By DPA</li>
     * </ol>
     * @return list of all Forbidden By DPA records
     * @throws IOException
     */
    public static LinkedList<String> collectAllForbiddenByDPARecords() throws IOException
    {
        LinkedList<String> forbiddenByDPARecords = new LinkedList<>();
        BufferedReader bufferedReader = new BufferedReader(new FileReader(Const.INTRADIEM_LOG_DIR + getUserFilterFilename()));

        String line,
               prevLine = "";
        while( ( line = bufferedReader.readLine() ) != null )
        {
            if( line.contains("Forbidden By DPA") )
            {
                forbiddenByDPARecords.add(prevLine);
                forbiddenByDPARecords.add(line);
            }
            else
            {
                prevLine = line;
            }
        }

        bufferedReader.close();

        return forbiddenByDPARecords;
    }

    /**
     * Get formatted filename: YYYY-MM-DD-User-filter.log
     * Example: 2018-09-11-User-filter.log
     * @return
     */
    private static String getUserFilterFilename()
    {
        StringBuffer fileName = new StringBuffer();
        Date date = new Date();

        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("Y");
        fileName.append(simpleDateFormat.format(date)).append("-");

        simpleDateFormat.applyPattern("MM");
        fileName.append(simpleDateFormat.format(date)).append("-");

        simpleDateFormat.applyPattern("dd");
        fileName.append(simpleDateFormat.format(date)).append("-");

        fileName.append("User-filter.log");

        return fileName.toString();
    }
}
