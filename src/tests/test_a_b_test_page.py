from operator import contains

import pytest
from src.pages.a_b_test_page import ABTestPage
from src.constants.urls import Urls
from src.pages.home_page import HomePage
import allure

@allure.title("A/B Testing")
@allure.description("Testing A/B page")
@pytest.mark.positive
def test_a_b_testing(driver):
    homepage = HomePage(driver)
    homepage.open(Urls.BASE_URL)
    homepage.click_a_b_test()

    a_b_test = ABTestPage(driver)
    head_text = a_b_test.get_heading_text()
    para_text = a_b_test.get_para_text()

    assert head_text == "A/B Test Control"
    assert "Also known as split testing" in para_text


