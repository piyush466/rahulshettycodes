import time

from selenium import webdriver

from selenium.webdriver.common.by import By

class PIM:

    PIM_click_xpath = "//span[text()='PIM']"
    adddata_click_xpath = "//button[text()=' Add ']"

    def __init__(self,driver):
        self.driver = driver

    def pim_click(self):
        self.driver.find_element(By.XPATH, self.PIM_click_xpath).click()
        time.sleep(5)

    def click_add_button(self):
        self.driver.find_element(By.XPATH, self.adddata_click_xpath).click()
        time.sleep(5)
