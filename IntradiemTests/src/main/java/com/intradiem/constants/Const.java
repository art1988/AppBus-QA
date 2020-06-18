package com.intradiem.constants;

public final class Const
{
    public static final String INTRADIEM_CLIENT_USERNAME = "appbusag",
                               INTRADIEM_CLIENT_PASSWORD = "123",

                               INTRADIEM_ADMIN_USERNAME  = "appbusadmin",
                               INTRADIEM_ADMIN_PASSWORD  = "P@ssword1",

                               EDAPT_USERNAME = "edapt-setup",
                               EDAPT_PASSWORD = "511maps";

    public static final String URL_ADMIN  = "https://customersandbox95.intradiem.com",
                               URL_CONFIG = "https://dev.e-dapt.net:4440/edapt-admin/";

    public static final String CHROME_DRIVER_PATH = "D:\\Chromedriver\\chromedriver.exe";

    public static final String DPA_CONFIG_PATH      = "D:\\dpa.config",
                               DPA_CONFIG_COPY_PATH = "D:\\dpa_copy.config";

    public static final String INTRADIEM_CACHE_DIR = "C:\\Users\\User\\AppData\\Local\\IntradiemDesktopExperience\\cache\\QtWebEngine\\Default\\Cache",
                               INTRADIEM_LOG_DIR  = System.getenv("LocalLogsDir") + "\\AppBus\\";


    private Const() {}
}
