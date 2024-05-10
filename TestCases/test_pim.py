from PageObject.PIM_Page import PIM
from TestCases.test_orangeHRM_login import TestOrangeLogin
from selenium import webdriver

from selenium.webdriver.common.by import By

class Test_PIM(TestOrangeLogin):

    def test_pim_page(self,setup_orangeHRM):
        self.driver = setup_orangeHRM
        TestOrangeLogin.test_login(self,setup_orangeHRM)
        self.pim = PIM(self.driver)
        self.pim.pim_click()
        self.pim.click_add_button()



