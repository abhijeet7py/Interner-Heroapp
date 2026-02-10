from src.pages.base_page import BasePage
from src.pages.home_page_locators import HomePageLocators

class HomePage(BasePage):
    def click_a_b_test(self):
        self.click(HomePageLocators.a_b_test)

    def click_add_rem_ele(self):
        self.click(HomePageLocators.add_rem_ele)

    def click_basic_auth(self):
        self.click(HomePageLocators.basic_auth)

    def click_broken_img(self):
        self.click(HomePageLocators.broken_img)

    def click_challe_dom(self):
        self.click(HomePageLocators.challe_dom)

    def click_checkbox(self):
        self.click(HomePageLocators.checkbox)

    def click_context_menu(self):
        self.click(HomePageLocators.context_menu)




