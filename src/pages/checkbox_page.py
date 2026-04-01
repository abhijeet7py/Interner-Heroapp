from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from src.pages.base_page import BasePage
from src.pages.home_page import HomePage

class CheckBox(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    checkbox_1 = (By.XPATH,"//input[@type='checkbox'][1]")
    checkbox_2 = (By.XPATH,"//input[@type='checkbox'][2]")

    def checkbox_1_select(self):
        self.driver.find_element(*CheckBox.checkbox_1).click()

    def checkbox_2_select(self):
        self.driver.find_element(*CheckBox.checkbox_2).click()

    def is_checkbox_1_selected(self):
        return self.driver.find_element(*CheckBox.checkbox_1).is_selected()

    def is_checkbox_2_selected(self):
        return self.driver.find_element(*CheckBox.checkbox_2).is_selected()

