# login page class
# responsibility -> get username and send keys - email
# get password and send keys -email
# click the submit button and navigate to dashboard page
# Invalid - error message
# forgot password


# page class
# page Locators
# page Actions
# Webdriver Init
# custom functions
# No assertions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # page locators
    username = (By.ID, "login-username")
    password = (By.NAME, "password")
    submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    # forgot_password = (By.XPATH, "//*[text()='Forgot Password?']")
    error_message = (By.ID, "js-notification-box-msg")
    # free_trail = (By.XPATH, "//*[text()='Start a free trial']")
    # sso_login = (By.XPATH, "//*[text()='Start a free trial']")
    # remember_checkbox = (By.XPATH, "//*[@class='checkbox-radio-icon']")

    # Page Actions

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    # Page Action - Main Action

    def login_to_vwo(self,usr,pwd):
        self.get_username().send_keys(usr)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()

    def get_error_message_text(self):
        return self.get_error_message().text

