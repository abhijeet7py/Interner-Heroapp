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

@allure.title("Home Page Tests")
@allure.description("Digest Auth Navigation test")
@pytest.mark.positive
def test_digest_auth_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_digest_auth()
    assert home.driver.current_url == Urls.digest_auth

@allure.title("Home Page Tests")
@allure.description("Disappearing elements Navigation test")
@pytest.mark.positive
def test_disappearing_ele_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_disappear_elem()
    assert home.driver.current_url == Urls.disappear_elem

@allure.title("Home Page Tests")
@allure.description("Drag and drop Navigation test")
@pytest.mark.positive
def test_drag_n_drop_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_drag_n_drop()
    assert home.driver.current_url == Urls.drag_n_drop

@allure.title("Home Page Tests")
@allure.description("Dropdown Navigation test")
@pytest.mark.positive
def test_dropdown_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_dropdown()
    assert home.driver.current_url == Urls.dropdown

@allure.title("Home Page Tests")
@allure.description("Dynamic content Navigation test")
@pytest.mark.positive
def test_dynamic_content_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_dynamic_content()
    assert home.driver.current_url == Urls.dyn_content

@allure.title("Home Page Tests")
@allure.description("Dynamic control Navigation test")
@pytest.mark.positive
def test_dynamic_control_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_dyn_controls()
    assert home.driver.current_url == Urls.dyn_controls

@allure.title("Home Page Tests")
@allure.description("Dynamic loading Navigation test")
@pytest.mark.positive
def test_dyn_load_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_dyn_loading()
    assert home.driver.current_url == Urls.dyn_loading

@allure.title("Home Page Tests")
@allure.description("Entry add Navigation test")
@pytest.mark.positive
def test_entry_add_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_entry_add()
    assert home.driver.current_url == Urls.entry_ad

@allure.title("Home Page Tests")
@allure.description("Exit intent Navigation test")
@pytest.mark.positive
def test_exit_intent_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_exit_intent()
    assert home.driver.current_url == Urls.exit_int

@allure.title("Home Page Tests")
@allure.description("File download Navigation test")
@pytest.mark.positive
def test_file_download_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_file_download()
    assert home.driver.current_url == Urls.file_download

@allure.title("Home Page Tests")
@allure.description("File upload Navigation test")
@pytest.mark.positive
def test_file_upload_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_file_upload()
    assert home.driver.current_url == Urls.file_upload

@allure.title("Home Page Tests")
@allure.description("Floating Menu Navigation test")
@pytest.mark.positive
def test_floating_menu_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_floating_menu()
    assert home.driver.current_url == Urls.float_menu

@allure.title("Home Page Tests")
@allure.description("Forgot Password Navigation test")
@pytest.mark.positive
def test_forgot_password_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_forgot_password()
    assert home.driver.current_url == Urls.forgot_password

@allure.title("Home Page Tests")
@allure.description("Frames Navigation test")
@pytest.mark.positive
def test_drag_n_drop_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_frames()
    assert home.driver.current_url == Urls.frames

@allure.title("Home Page Tests")
@allure.description("Geolocation Navigation test")
@pytest.mark.positive
def test_geolocation_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_geolocation()
    assert home.driver.current_url == Urls.geolocation

@allure.title("Home Page Tests")
@allure.description("Horizontal slider Navigation test")
@pytest.mark.positive
def test_hor_slider_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_hor_slider()
    assert home.driver.current_url == Urls.hor_slider

@allure.title("Home Page Tests")
@allure.description("Hovers Navigation test")
@pytest.mark.positive
def test_drag_n_drop_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_hovers()
    assert home.driver.current_url == Urls.hovers

@allure.title("Home Page Tests")
@allure.description("Infinite scroll Navigation test")
@pytest.mark.positive
def test_infinite_scroll_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_infinite_scroll()
    assert home.driver.current_url == Urls.inf_scroll

@allure.title("Home Page Tests")
@allure.description("Inputs Navigation test")
@pytest.mark.positive
def test_inputs_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_inputs()
    assert home.driver.current_url == Urls.inputs

@allure.title("Home Page Tests")
@allure.description("JQuery Navigation test")
@pytest.mark.positive
def test_jquery_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_jquery()
    assert home.driver.current_url == Urls.jquery


@allure.title("Home Page Tests")
@allure.description("JS Alert Navigation test")
@pytest.mark.positive
def test_js_alert_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_js_alert()
    assert home.driver.current_url == Urls.js_alert

@allure.title("Home Page Tests")
@allure.description("JS Error Navigation test")
@pytest.mark.positive
def test_js_error_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_js_error()
    assert home.driver.current_url == Urls.js_alert

@allure.title("Home Page Tests")
@allure.description("Key Presses Navigation test")
@pytest.mark.positive
def test_key_press_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_key_presses()
    assert home.driver.current_url == Urls.key_presses

@allure.title("Home Page Tests")
@allure.description("DOM Navigation test")
@pytest.mark.positive
def test_dom_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_dom()
    assert home.driver.current_url == Urls.dom

@allure.title("Home Page Tests")
@allure.description("Multiple Window Navigation test")
@pytest.mark.positive
def test_mul_window_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_mul_window()
    assert home.driver.current_url == Urls.mul_window

@allure.title("Home Page Tests")
@allure.description("Nested frames Navigation test")
@pytest.mark.positive
def test_nested_frames_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_nested_frames()
    assert home.driver.current_url == Urls.nes_frames

@allure.title("Home Page Tests")
@allure.description("Notifications Navigation test")
@pytest.mark.positive
def test_notifications_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_notifications()
    assert home.driver.current_url == Urls.notifications

@allure.title("Home Page Tests")
@allure.description("Redirect links Navigation test")
@pytest.mark.positive
def test_redirect_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_redirect()
    assert home.driver.current_url == Urls.redirect

@allure.title("Home Page Tests")
@allure.description("Secure file download Navigation test")
@pytest.mark.positive
def test_sec_file_down_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_sec_file_down()
    assert home.driver.current_url == Urls.sec_file_down

@allure.title("Home Page Tests")
@allure.description("Shadow dom Navigation test")
@pytest.mark.positive
def test_shadow_dom_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_shadow_dom()
    assert home.driver.current_url == Urls.shadow_dom

@allure.title("Home Page Tests")
@allure.description("Shifting content Navigation test")
@pytest.mark.positive
def test_shifting_content_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_shift_content()
    assert home.driver.current_url == Urls.shift_content

@allure.title("Home Page Tests")
@allure.description("Slow resources Navigation test")
@pytest.mark.positive
def test_slow_resc_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_slow_resc()
    assert home.driver.current_url == Urls.slow_resc

@allure.title("Home Page Tests")
@allure.description("Sort tables Navigation test")
@pytest.mark.positive
def test_sort_tables_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_sort_table()
    assert home.driver.current_url == Urls.sort

@allure.title("Home Page Tests")
@allure.description("Status codes Navigation test")
@pytest.mark.positive
def test_status_codes_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_status_codes()
    assert home.driver.current_url == Urls.status_codes

@allure.title("Home Page Tests")
@allure.description("Typos Navigation test")
@pytest.mark.positive
def test_typos_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_typos()
    assert home.driver.current_url == Urls.typos

@allure.title("Home Page Tests")
@allure.description("WYSIWYG editor Navigation test")
@pytest.mark.positive
def test_wysiwyg_editor_nav(driver):
    home = HomePage(driver)
    home.open(Urls.BASE_URL)
    home.click_wysiwyg_editor()
    assert home.driver.current_url == Urls.wysiwyg_editor









