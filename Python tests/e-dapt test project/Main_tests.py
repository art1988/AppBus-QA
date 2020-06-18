import slic
from slic import winium
import sys
import unittest
import Mail_Tests
import Mail_Tests.basics_new_email_tests

import Mail_Tests.create_new_email_tests
from Mail_Tests.basics_new_email_tests import *
from Mail_Tests.create_new_email_tests import *
from Mail_Tests.sorting_mail_tests import *
from main_app_window import Maw




# testLoad = unittest.TestLoader()
# suites = testLoad.loadTestsFromModule(Mail_Tests.basics_new_email_tests)
#
# testResult = unittest.TestResult()
#
# runner = unittest.TextTestRunner(verbosity=1)
# testResult = runner.run(suites)
# print("errors")
# print(len(testResult.errors))
# print("failures")
# print(len(testResult.failures))
# print("skipped")
# print(len(testResult.skipped))
# print("testsRun")
# print(testResult.testsRun)
#
#
# mainTestSuite = unittest.TestSuite()
# mainTestSuite.addTest(unittest.makeSuite(Mail_Tests.basics_new_email_tests.Test1NewEmail))
#
#
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(mainTestSuite)
#
#
# class MainTest(unittest.TestSuite):
#
#     @classmethod
#     def setUpClass(cls):
#         print("MainTest.setUpClass")
#
#     @classmethod
#     def tearDownClass(cls):
#         print("teardcls")
#         Maw.destroy_connection()
#         winium.driver_winium.quit()
#
#
#     def suite(self):
#         suite = unittest.TestSuite()
#         suite.addTest(Mail_Tests.basics_new_email_tests.Test1NewEmail)
#         suite.addTest(Mail_Tests.basics_new_email_tests.Test2)
#         suite.addTest(Mail_Tests.create_new_email_tests.TestCreateNewEmail)
#         # suite.addTest(TestCase('test_*'))
#         return suite
#
#
# if __name__ == '__main__':
#     unittest.main()
#     Maw.destroy_connection()
#     winium.driver_winium.quit()
#
#
#
