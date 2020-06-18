from slic import winium
from main_app_window import Maw

Maw.destroy_connection()
window = winium.driver_winium.find_element_by_class_name("Window")
window.find_element_by_name("Закрыть").click()
