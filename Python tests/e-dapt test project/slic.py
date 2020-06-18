from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

security_data = []
file = open('security.txt', 'r')
for line in file:
    security_data.append(line.split()[1])
file.close()
sd_login = security_data[0]
sd_password = security_data[1]
sd_rsapassword = security_data[2]


class winium(object):

    driver_winium = webdriver.Remote(
       command_executor='http://localhost:9999',
       desired_capabilities={
           "app": r"C:\Users\Guest-user\Documents\Debug\AppBus.exe"
       })

    time.sleep(5)
    window = driver_winium.find_element_by_name("AppBus")
    WebDriverWait(driver_winium, 5).until(ec.element_to_be_clickable((By.CLASS_NAME, "ToSControl")))
    windowLogin = window.find_element_by_class_name("LoginControl")

    login = windowLogin.find_element_by_id("Login")
    login.send_keys(sd_login)

    password = windowLogin.find_element_by_id('Password')
    password.send_keys(sd_password)

    rsaPasscode = windowLogin.find_element_by_id("TfaPasscode")
    rsaPasscode.send_keys(sd_rsapassword)
    login = windowLogin.find_element_by_name("Log In")
    login.click()
    # time.sleep(30)
    wait = WebDriverWait(window, 40)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "CefBrowserWindow")))

    inspectWindow = window.find_element_by_class_name("CefBrowserWindow")
    inspectCloseButton = inspectWindow.find_element_by_name("Закрыть")
    inspectCloseButton.click()
    time.sleep(2)
    top_menu = window.find_element_by_id('TopMenuGroup')
    mail_folder = top_menu.find_element_by_name('Mail')
    mail_folder.click()
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "CefBrowserWindow")))
    inspectWindow = window.find_element_by_class_name("CefBrowserWindow")
    inspectCloseButton = inspectWindow.find_element_by_name("Закрыть")
    inspectCloseButton.click()
    time.sleep(5)


    @classmethod
    def destroy_connection(cls):
        winium.driver_winium.close()
