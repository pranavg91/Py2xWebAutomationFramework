import time

import allure
import pytest
from selenium import webdriver
from tests.pageObjects.loginPage import LoginPage
from tests.pageObjects.dashboardPage import *


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver


@allure.epic("VWO login")
@pytest.mark.negative
# def test_vwo_login_negative(setup):
#     driver = setup
#     loginpage = LoginPage(driver)
#     loginpage.login_to_vwo(usr="admin@gmail.com", pwd="admin")
#     time.sleep(50)
#     error_message = loginpage.get_error_message_text()
#     assert error_message == "Your email, password, IP address or location did not match"

@pytest.mark.positive
def test_login_positive(setup):
    driver = setup
    loginpage = LoginPage(driver)
    loginpage.login_to_vwo(usr="cdijxph9f2@ezztt.com",pwd="Wingify@123")

    time.sleep(80)
    dashboapage = DashboardPage(driver)
    assert driver.current_url == "https://app.vwo.com/#/dashboard"
    assert "Py2xATB" in dashboapage.user_logged_in_text()