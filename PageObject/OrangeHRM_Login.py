from selenium import webdriver

from selenium.webdriver.common.by import By

class OrangeHRM:
    username_name = "username"
    password_name = "password"
    login_btn_xpath = "//button"

    def __init__(self,driver):
        self.driver = driver

    def usernmae(self,username):
        self.driver.find_element(By.NAME,self.username_name).send_keys(username)

    def password(self,password):
        self.driver.find_element(By.NAME,self.password_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()