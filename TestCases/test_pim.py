import time

from PageObject.PIM_Page import PIM
from TestCases.test_orangeHRM_login import TestOrangeLogin
from Utilities.logging import logGen
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.readProperties import ReadProperties


class Test_PIM(TestOrangeLogin):
    name = ReadProperties.userfname()
    mname = ReadProperties.usermname()
    lname  = ReadProperties.userlnamee()
    logs = logGen.logger()

    def test_pim_page(self,setup_orangeHRM):
        self.driver = setup_orangeHRM
        TestOrangeLogin.test_login(self,setup_orangeHRM)
        self.logs.info("test is starting")

        self.pim = PIM(self.driver)
        self.driver.implicitly_wait(10)
        self.pim.pim_click()
        self.pim.click_add_button()
        self.pim.employee_name(self.name)
        self.pim.middle_name(self.mname)
        self.pim.last_name(self.lname)
        self.pim.click_save()
        waits = WebDriverWait(self.driver,10)
        self.ele = waits.until(EC.presence_of_element_located((By.XPATH,"//h6[@class='oxd-text oxd-text--h6 --strong']")))
        # print(self.ele)
        time.sleep(2)
        if  self.ele.text == "Piyush Dravyaka":
            print("Pass")
        else:
            print("Fail")
            self.logs.error("Test is fail")
            self.driver.save_screenshot(r"C:\Users\ASUS\PycharmProjects\RahulShetty\Screenshots\PIM.jpg")









