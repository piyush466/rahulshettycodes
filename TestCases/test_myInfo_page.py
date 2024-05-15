import time

from TestCases.test_orangeHRM_login import TestOrangeLogin
from Utilities.logging import logGen
from selenium import webdriver
from PageObject.MyInfo_Page import MyInfo
from selenium.webdriver.common.by import By
from Utilities.readProperties import ReadProperties

class Test_MyInfo:
    username = ReadProperties.username_of_myinfo()
    logs = logGen.logger()

    def test_myinfo(self,setup_orangeHRM):
        self.driver = setup_orangeHRM

        TestOrangeLogin.test_login(self,setup_orangeHRM)
        self.myF = MyInfo(self.driver)
        self.myF.click_on_myinfo()
        self.myF.clearname_and_entername(self.username)
        self.myF.scroll_down(0, 300)
        self.myF.click_on_save()
        time.sleep(6)

        # assert self.driver == "OrangeHRM", " fail test"
        if self.driver.title == "OrangeHRM":
            self.logs.info("*********your test is pass**********")
            print("main to piyush 2nd time")

        else:
            self.logs.error("***********Your test is fail***************")
            self.driver.save_screenshot(r"C:\Users\ASUS\PycharmProjects\rahulshettycodes\Screenshots\info.png")




