import time
from time import sleep

from pages.auth_page import AuthPage
from pages.home_page import HomePage
from pages.coworking_page import CoworkingPage


def test_auth_chrome(driver_chrome):
    driver_chrome.get("https://my.proweb.uz/log-in")
    auth_page = AuthPage(driver_chrome)
    auth_page.enter_phone_number("998335814130")
    auth_page.click_btn_next()
    auth_page.enter_password("proweb3106632")
    auth_page.click_btn_submit()
    try:
        auth_page.click_btn_sessions()
        auth_page.click_btn_finish()
    except:
        pass
    time.sleep(3)
    auth_page.click_coworking()

    # home_page = HomePage(driver_chrome)
    # home_page.click_profile_icon()
    # time.sleep(5)
    # home_page.click_exit_btn()
    # home_page.click_confirm_exit()


    coworking_page = CoworkingPage(driver_chrome)
    coworking_page.click_sign_up_btn()
    coworking_page.click_aybek_2_btn()
    coworking_page.click_select_btn_1()
    coworking_page.click_date_btn()
    coworking_page.click_group_btn()
    coworking_page.click_round_btn()
    coworking_page.click_select_btn_2()
    coworking_page.enter_time()
    coworking_page.enter_hours("11")
    coworking_page.enter_minutes("00")
    time.sleep(5)
    coworking_page.click_select_btn_3()
    coworking_page.click_place()
    coworking_page.click_computer()
    coworking_page.click_select_btn_4()
    coworking_page.click_send_btn()


def test_invalid_auth_chrome(driver_chrome):
        driver_chrome.get("https://my.proweb.uz/log-in")
        auth_page = AuthPage(driver_chrome)
        auth_page.enter_phone_number("998974703818")
        auth_page.click_btn_next()


# def test_auth_edge(driver_edge):
#     driver_edge.get("https://my.proweb.uz/log-in")
#     auth_page = AuthPage(driver_edge)
#     auth_page.enter_phone_number("998335814130")
#     auth_page.click_btn_next()
#     auth_page.enter_password("proweb3106632")
#     auth_page.click_btn_submit()
#     auth_page.click_btn_sessions()
#     auth_page.click_btn_finish()


# def test_auth_firefox(driver_firefox):
#     driver_firefox.get("https://my.proweb.uz/log-in")
#     auth_page = AuthPage(driver_firefox)
#     auth_page.enter_phone_number("998335814130")
#     auth_page.click_btn_next()
#     auth_page.enter_password("proweb3106632")
#     auth_page.click_btn_submit()
#     auth_page.click_btn_sessions()
#     auth_page.click_btn_finish()
