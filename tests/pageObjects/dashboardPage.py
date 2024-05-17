# Dashboard class
# Verify the username

# Page class
# Page actions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self,driver):
        self.driver = driver

    #Page Locator
    user_logged_in = (By.XPATH,"//*[@data-qa='lufexuloga']")

    def get_user_logged_in(self):
        return self.driver.find_element(*DashboardPage.user_logged_in)

    # Page Action
    def user_logged_in_text(self):
        return self.get_user_logged_in().text
