from selenium.webdriver.common.by import By
from src.constants.urls import Urls
from src.pages.base_page import BasePage


class ABTestPage(BasePage):
    heading = (By.XPATH, "//div[@class='example']/h3")
    para = (By.XPATH, "//div[@class='example']/p")

    def get_heading_text(self):
        return self.driver.find_element(*ABTestPage.heading).text

    def get_para_text(self):
        return self.driver.find_element(*ABTestPage.para).text



