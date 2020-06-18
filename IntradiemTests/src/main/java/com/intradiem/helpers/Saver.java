package com.intradiem.helpers;

import java.util.LinkedList;
import java.util.Queue;

public class Saver
{
    private static String commentOfRemovedRule;
    private static String headerOfRemovedRule;
    private static String bodyOfRemovedRule;
    private static Queue<String> fifo_Messages = new LinkedList<>();


    public static void setRemovedRule(String commentOfRuleThatWasRemoved)
    {
        commentOfRemovedRule = commentOfRuleThatWasRemoved;
    }

    public static String getRemovedRule()
    {
        return commentOfRemovedRule;
    }

    /**
     * Set header of removed rule that equals of header in dpa.config
     * @param headerOfRuleThatWasRemoved
     */
    public static void setHeaderOfRemovedRule(String headerOfRuleThatWasRemoved)
    {
        headerOfRemovedRule = headerOfRuleThatWasRemoved;
    }

    /**
     * Set unique header of removed rule.
     * This method rewrites headerOfRemovedRule.
     * As an example: "header": "Host:*fonts.gstatic.com" will not apper in User-filter.log,
     * but appear GET /s/materialicons/v41/flUhRq6tzZclQEJ-Vdg-IuiaDsNc.woff2
     * @param uniqueHeader
     */
    public static void setUniqueHeader(String uniqueHeader)
    {
        setHeaderOfRemovedRule(uniqueHeader);
    }

    public static String getHeaderOfRemovedRule()
    {
        return headerOfRemovedRule;
    }

    public static void setBodyOfRemovedRule(String bodyOfRuleThatWasRemoved)
    {
        bodyOfRemovedRule = bodyOfRuleThatWasRemoved;
    }

    public static String getBodyOfRemovedRule()
    {
        return bodyOfRemovedRule;
    }

    /**
     * Add one single message in fifo_Messages
     * @param messageText
     */
    public static void addDesiredMessageInFIFO(String messageText)
    {
        fifo_Messages.add(messageText);
    }

    /**
     * Get FIFO of desirable messages
     * @return
     */
    public static Queue<String> getDesirableMessages()
    {
        return fifo_Messages;
    }
}
