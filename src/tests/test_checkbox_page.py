import pytest
from src.constants.config import Urls
from src.pages.checkbox_page import CheckBox
from src.pages.home_page import HomePage
import allure

@allure.title("Checkbox Testing")
@allure.description("Testing Checkbox page")
@pytest.mark.positive
def test_checkbox_page_1(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_checkbox()

    checkbox = CheckBox(driver)
    checkbox.checkbox_1_select()
    checkbox.is_checkbox_1_selected()
    assert checkbox.is_checkbox_1_selected() is True


@allure.title("Checkbox Testing")
@allure.description("Testing Checkbox page")
@pytest.mark.positive
def test_checkbox_page_2(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_checkbox()

    checkbox = CheckBox(driver)
    checkbox.checkbox_2_select()
    checkbox.is_checkbox_1_selected()
    assert checkbox.is_checkbox_2_selected() is False


