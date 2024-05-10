from selenium import webdriver
from selenium.webdriver.common.by import By


class Facebook:
    email_name = "email"
    password_name = "pass"
    login_btn_name= "login"

    def __init__(self,driver):
        self.driver = driver

    def usernmae(self,username):
        self.driver.find_element(By.NAME,self.email_name).send_keys(username)

    def password(self,password):
        self.driver.find_element(By.NAME,self.password_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.NAME, self.login_btn_name).click()