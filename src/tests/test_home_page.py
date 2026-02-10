import pytest

from src.pages.home_page import HomePage
from src.constants.urls import Urls
import allure

@allure.title("Home Page Tests")
@allure.description("A/B Navigation test")
@pytest.mark.positive
def test_a_b_test_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_a_b_test()
    assert home.driver.current_url == Urls.a_b_testing





