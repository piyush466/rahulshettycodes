import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from TestCases.test_pim import Test_PIM
from Utilities.readProperties import ReadProperties
from Utilities.logging import logGen

class PIM:

    PIM_click_xpath = "//span[text()='PIM']"
    adddata_click_xpath = "//button[text()=' Add ']"
    employe_name = "firstName"
    mid_name = "middleName"
    last_names  = "lastName"
    upload_img_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button/i"
    click_on_save_xpath = "//button[@type='submit']"

    logs = logGen.logger()


    def __init__(self,driver):
        self.driver = driver

    def pim_click(self):
        self.driver.find_element(By.XPATH, self.PIM_click_xpath).click()


    def click_add_button(self):
        self.driver.find_element(By.XPATH, self.adddata_click_xpath).click()
        time.sleep(5)

    def employee_name(self,emp_name):
        self.driver.find_element(By.NAME, self.employe_name).send_keys(emp_name)
        self.logs.info(f'The Locator is "{self.employe_name}" and Employee name is "{emp_name}"')



    def middle_name(self,mid_name):
        self.driver.find_element(By.NAME, self.mid_name).send_keys(mid_name)
        self.logs.info(f'The Locator is "{self.mid_name}" and Employee name is "{mid_name}"')

    def last_name(self,l_name):
        self.driver.find_element(By.NAME, self.last_names).send_keys(l_name)
        self.logs.info(f'The Locator is "{self.last_names}" and Employee name is "{l_name}"')


    def upload_img(self,img):
        img_data = self.driver.find_element(By.XPATH, self.upload_img_xpath)
        # img_data.click()
        time.sleep(5)
        # img_data.send_keys(img)
        # # C:\Users\ASUS\Downloads\piyush.jpg
        # time.sleep(6)

    def click_save(self):

        self.driver.find_element(By.XPATH, self.click_on_save_xpath).click()
        self.logs.info(f'The Locator is "{self.click_on_save_xpath}" and Click on the save"')

        time.sleep(5)


