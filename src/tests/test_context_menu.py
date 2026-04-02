import time

import pytest
from src.pages.a_b_test_page import ABTestPage
from src.constants.config import Urls
from src.pages.add_rem_page import AddRemPage
from src.pages.context_menu_page import ContextMenuPage
from src.pages.home_page import HomePage
import allure

@allure.title("Context Menu Testing")
@allure.description("Testing Context menu page")
@pytest.mark.positive
def test_context_menu_page(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_context_menu()

    context_menu = ContextMenuPage(driver)
    context_menu.right_click_in_box()
    alert = driver.switch_to.alert
    text = alert.text
    assert text == "You selected a context menu"
    # time.sleep(5)
    alert.accept()
    time.sleep(5)