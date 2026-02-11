from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.pages.base_page import BasePage
from src.pages.home_page import HomePage

class AddRemPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    add_element = (By.XPATH,"//button[normalize-space()='Add Element']")
    del_element = (By.XPATH,"//button[normalize-space()='Delete']")

    def click_add_element(self):
        return self.driver.find_element(*AddRemPage.add_element).click()

    def click_del_element(self):
        return self.wait.until(EC.visibility_of_element_located(self.del_element))
