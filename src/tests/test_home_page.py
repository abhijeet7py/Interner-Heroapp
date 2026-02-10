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

@allure.title("Home Page Tests")
@allure.description("Add Remove element Navigation test")
@pytest.mark.positive
def test_add_rem_ele_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_add_rem_ele()
    assert home.driver.current_url == Urls.add_rem_ele

@allure.title("Home Page Tests")
@allure.description("Basic Auth Navigation test")
@pytest.mark.positive
def test_basic_auth_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_basic_auth()
    assert home.driver.current_url == Urls.basic_auth

@allure.title("Home Page Tests")
@allure.description("Broken images Navigation test")
@pytest.mark.positive
def test_broken_img_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_broken_img()
    assert home.driver.current_url == Urls.broken_img

@allure.title("Home Page Tests")
@allure.description("Challenging dom Navigation test")
@pytest.mark.positive
def test_challe_dom_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_challe_dom()
    assert home.driver.current_url == Urls.challe_dom

@allure.title("Home Page Tests")
@allure.description("Checkboxes Navigation test")
@pytest.mark.positive
def test_checkbox_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_checkbox()
    assert home.driver.current_url == Urls.checkbox

@allure.title("Home Page Tests")
@allure.description("Context Menu Navigation test")
@pytest.mark.positive
def test_context_menu_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_context_menu()
    assert home.driver.current_url == Urls.context_menu






