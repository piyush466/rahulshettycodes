import pytest
from PageObject.OrangeHRM_Login import OrangeHRM
from Utilities.logging import logGen
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestOrangeLogin:

    # @pytest.mark.smoke
    def test_login(self,setup_orangeHRM):
        # self.logs = logGen.logger()
        self.driver = setup_orangeHRM
        # self.logs.info("*******Invoke the browser*********")
        self.hrm = OrangeHRM(self.driver)
        self.hrm.usernmae("Admin")
        # self.logs.info("**********Entering user name**********")
        self.hrm.password("admin123")
        # self.logs.info("***********Entering the password*********")
        self.hrm.click_login()
        # self.logs.info("*************Click on login button***********")

        waits = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH, "//h6"))).text

        if waits == "Dashboard":
            print("Test Is pass")

        else:
            print("Test is Fail")
            self.driver.save_screenshot(r"C:\Users\ASUS\PycharmProjects\RahulShetty\Screenshots\piyush.png")


