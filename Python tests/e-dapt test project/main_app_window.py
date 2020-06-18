from cef_driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


driver_instance = Driver().instance
driver_instance.implicitly_wait(10)


class Maw(object):

    @classmethod
    def destroy_connection(cls):
        driver_instance.quit()

    @classmethod
    def get_devices(cls):
        return WebDriverWait(driver_instance, 10).until(ec.presence_of_element_located((By.ID, "main-app-window")))

    @classmethod
    def get_driver(cls):
        return driver_instance

