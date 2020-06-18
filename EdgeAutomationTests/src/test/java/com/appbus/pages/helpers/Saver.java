package com.appbus.pages.helpers;

/**
 * Class to save transition data between separate tests
 */
public class Saver
{
    private static String emailSubject,
                          draftEmailSubject;


    public Saver()
    {
    }

    public static void saveEmailSubject(String subj)
    {
        emailSubject = subj;
    }

    public static String getEmailSubject()
    {
        return emailSubject;
    }

    public static void saveDraftEmailSubject(String subj)
    {
        draftEmailSubject = subj;
    }

    public static String getDraftEmailSubject()
    {
        return draftEmailSubject;
    }
}
