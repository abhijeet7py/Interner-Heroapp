from src.pages.base_page import BasePage
from src.pages.home_page_locators import HomePageLocators

class HomePage(BasePage):
    def click_a_b_test(self):
        self.click(HomePageLocators.a_b_test)

    def click_add_rem_ele(self):
        self.click(HomePageLocators.add_rem_ele)


