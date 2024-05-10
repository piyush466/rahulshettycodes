import time

from PageObject.Admin_Page import Admin_user
from TestCases.test_orangeHRM_login import TestOrangeLogin
from selenium import webdriver

from selenium.webdriver.common.by import By



class TestAdmin(TestOrangeLogin):

    def test_adminflow(self,setup_orangeHRM):
        self.driver = setup_orangeHRM
        TestOrangeLogin.test_login(self,setup_orangeHRM)
        self.adu = Admin_user(self.driver)
        self.adu.click_admin()
        
