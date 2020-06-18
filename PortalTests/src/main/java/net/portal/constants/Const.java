package net.portal.constants;

public final class Const
{
    public static final String USER_EDAPT    = "edapt-setup";
    public static final String USER_QADEV    = "qadev";
    public static final String USER_MILSHTYU = "milshtyu";
    public static final String PASSWORD = "511maps";

    public static final String GECKO_DRIVER_PATH  = "D:\\Geckodriver\\geckodriver.exe";
    public static final String CHROME_DRIVER_PATH = "D:\\Chromedriver\\chromedriver.exe";
    public static final String DOWNLOAD_FOLDER = "C:\\automation\\Downloads";

    public static final String QA_INTERNAL_LOGIN_PAGE    = "https://dev-msa-qa.botf03.net:9613/edapt-admin/login.jsp";
                                                            //"https://dev-msa-qa.botf03.net:9613/edapt-admin/login.jsp" QA internal
                                                            //"https://dev.e-dapt.net:5564/edapt-admin/" //QA external

    public static final String STAGE_EXTERNAL_LOGIN_PAGE = "https://dev.e-dapt.net:5554/edapt-admin/login.jsp";
                                                            //"https://dev.e-dapt.net:5564/edapt-admin/";
                                                            //"https://dev-msa-qa-stag.botf03.net:9613/edapt-admin/login.jsp"; //QA Stage
                                                            //"https://dev.e-dapt.net:5564/edapt-admin/" //QA external
                                                            //"https://dev-msa-qa.botf03.net:9613/edapt-admin/login.jsp" //QA internal
                                                            //"https://dev.e-dapt.net:4440/edapt-admin"
                                                            //"https://dev.e-dapt.net:5554/edapt-admin/login.jsp"; //QA Stage Ex

    public static final String BASE_URI_QA    = "https://128.66.200.151:9613/";
    public static final String BASE_URI_STAGE = "https://dev-msa-qa-stag.botf03.net:9613/";

    // The following files supposed to be on every win system... (?)
    // Sample of binary file (241 Kb)
    public static final String BINARY_FILE_SAMPLE = "C:\\WINDOWS\\System32\\notepad.exe";
    // Sample of non-binary file
    public static final String TEXT_FILE_SAMPLE   = System.getProperty("user.dir") + "\\Samples\\system.ini";
    public static final String TEXT_FILE_SAMPLE_2 = System.getProperty("user.dir") + "\\Samples\\WindowsUpdate.log";

    // Sample of js file
    public static final String JS_FILE_SAMPLE     = System.getProperty("user.dir") + "\\Samples\\JSSample.js";
    // Sample of Java lib file
    public static final String JAVA_FILE_SAMPLE   = System.getProperty("user.dir") + "\\Samples\\Const.java";

    private Const() {}
}
