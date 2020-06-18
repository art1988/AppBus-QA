from appium import webdriver
import unittest, time, os
# from time import sleep
import Config.Mail.main_window

mw = Config.Mail.main_window.Elements

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Test1(unittest.TestCase):
    "Class to run tests against the ATP WTA app"
    def setUp(self):
        print('123')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'ASUS Nexus 7'
        desired_caps['app'] = PATH('/storage/emulated/0/Download/e-Dapt-dev-debug.apk')
        desired_caps['appPackage'] = 'com.appbus.container'
        desired_caps['appActivity'] = 'com.appbus.container.MainActivity'
        desired_caps['appWaitActivity'] = 'com.appbus.container.MainActivity'
        print('1412z42141')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print('SU')

    def tearDown(self):
        "Tear down the test"
        print('TD')
        # self.driver.quit()

    def test_atp_wta(self):
        "Testing the ATP WTA app "
        print("T1")
        self.driver.implicitly_wait(10)
        time.sleep(5)

        new_email = self.driver.find_element_by_xpath(mw.new_email_button)
        new_email.click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test1)
    unittest.TextTestRunner(verbosity=2).run(suite)
