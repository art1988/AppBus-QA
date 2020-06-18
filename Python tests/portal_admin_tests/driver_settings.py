import sys
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options
# import tests.main_test as main_tests
import os

linux = 'Linux'
mac = 'Darwin'
windows = 'Windows'

project_path = os.path.dirname(os.path.dirname(__file__))
# print('project_path', project_path)
support_files_path = os.path.join(project_path, 'support_files')
# print('support_files_path', support_files_path)

print(sys.argv)


def driver(self):
    now_platform = platform.system()
    print('now_platform', now_platform, "\n")
    # if main_tests.browser == 'firefox':
    #     print('main_tests.browser', main_tests.browser)
    if now_platform == windows:
        firefox_options = Firefox_Options()
        firefox_options.headless = True
        self.driver = webdriver.Firefox(options=firefox_options,
                                        executable_path=support_files_path + '\geckodriver.exe')
        return self.driver
    elif now_platform == linux:
        firefox_options = Firefox_Options()
        firefox_options.headless = True
        # self.driver = webdriver.Firefox(options=firefox_options, executable_path= #### указать?)
        return self.driver
    elif now_platform == mac:
        firefox_options = Firefox_Options()
        firefox_options.headless = True
        # self.driver = webdriver.Firefox(options=firefox_options, executable_path= #### указать?)
        return self.driver


def driver_with_firefox_json_download(self, downloads_folder):
    now_platform = platform.system()
    print('now_platform', now_platform, "\n")
    # if main_tests.browser == 'firefox':
    #     print('main_tests.browser', main_tests.browser)
    if now_platform == windows:
        firefox_options = Firefox_Options()
        firefox_options.headless = True
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.dir", downloads_folder)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/json")
        self.driver = webdriver.Firefox(profile, options=firefox_options,
                                        executable_path=support_files_path + '\geckodriver.exe')
        return self.driver
    else:
        raise Exception('Something wrong')


def driver_with_firefox_octet_download(self, downloads_folder):
    now_platform = platform.system()
    print('now_platform', now_platform, "\n")
    # if main_tests.browser == 'firefox':
    #     print('main_tests.browser', main_tests.browser)
    if now_platform == windows:
        firefox_options = Firefox_Options()
        firefox_options.headless = True
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.dir", downloads_folder)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        self.driver = webdriver.Firefox(profile, options=firefox_options,
                                        executable_path=support_files_path + '\geckodriver.exe')
        return self.driver
    else:
        raise Exception('Something wrong')


def driver_with_firefox_txt_download(self, downloads_folder):
    now_platform = platform.system()
    print('now_platform', now_platform, "\n")
    # if main_tests.browser == 'firefox':
    #     print('main_tests.browser', main_tests.browser)
    if now_platform == windows:
        firefox_options = Firefox_Options()
        firefox_options.headless = True
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.dir", downloads_folder)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain")
        self.driver = webdriver.Firefox(profile, options=firefox_options,
                                        executable_path=support_files_path + '\geckodriver.exe')
        return self.driver
    else:
        raise Exception('Something wrong')
