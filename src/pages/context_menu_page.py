from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from src.pages.base_page import BasePage
from src.pages.home_page import HomePage

class ContextMenuPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    box = (By.ID,"hot-spot")

    def right_click_in_box(self):
        actions = ActionChains(self.driver)
        actions.context_click(self.driver.find_element(*ContextMenuPage.box)).perform()
