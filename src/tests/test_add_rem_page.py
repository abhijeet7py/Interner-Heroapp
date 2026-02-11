import pytest
from src.pages.a_b_test_page import ABTestPage
from src.constants.urls import Urls
from src.pages.add_rem_page import AddRemPage
from src.pages.home_page import HomePage
import allure

@allure.title("Add & Remove element Testing")
@allure.description("Testing Add & remove page")
@pytest.mark.positive
def test_add_rem_page(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_add_rem_ele()

    add_rem = AddRemPage(driver)
    add_rem.click_add_element()
    delete_text = add_rem.click_del_element().text
    assert delete_text == "Delete"
