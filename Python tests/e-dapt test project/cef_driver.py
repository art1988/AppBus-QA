from selenium import webdriver


CEF_PORT = "8088"
DEBUGGER_ADDRESS = "localhost:{}".format(CEF_PORT)
CHROMEDRIVER_PATH = "c:\\drova\\chromedriver.exe"


class Driver(object):

    @classmethod
    def __init__(cls):
        options = webdriver.ChromeOptions()
        options.debugger_address = DEBUGGER_ADDRESS
        cls.instance = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
