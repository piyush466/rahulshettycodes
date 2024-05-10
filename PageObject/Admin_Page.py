from PageObject.OrangeHRM_Login import OrangeHRM
from selenium import webdriver

from selenium.webdriver.common.by import By

class Admin_user:

    admin_click_xpath = "//span[text()='Admin']"


    def __init__(self,driver):

        self.driver = driver

    def click_admin(self):
        self.driver.find_element(By.XPATH, self.admin_click_xpath).click()
