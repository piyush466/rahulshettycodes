import time
from selenium.webdriver.common.keys import Keys
from Utilities.logging import logGen
from selenium import webdriver
from Utilities.readProperties import ReadProperties
from selenium.webdriver.common.by import By

class MyInfo:

    logs = logGen.logger()

    def __init__(self,driver):
        self.driver = driver


    def click_on_myinfo(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, ReadProperties.myinfo_btn_xpath()).click()
        self.logs.info(f'Locator is "{ReadProperties.myinfo_btn_xpath()}" and click on myinfo button')

    def clearname_and_entername(self,username):
        time.sleep(3)

        self.nameText = self.driver.find_element(By.NAME, ReadProperties.enter_name())
        self.nameText.send_keys(Keys.BACK_SPACE * 115)
        self.nameText.send_keys(username)
        time.sleep(2)


    def click_on_save(self):
        self.driver.find_element(By.XPATH, ReadProperties.save_btn_xpath()).click()

    def scroll_down(self,up,down):
        self.driver.execute_script(f"window.scrollBy({up},{down})")
