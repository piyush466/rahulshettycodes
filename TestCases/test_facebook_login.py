from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObject.FacebookLogin import Facebook
from Utilities.logging import logGen

class TestFacebook:
    logs = logGen.logger()

    def test_login(self,setup):
        self.driver = setup
        self.logs = logGen.logger()
        self.fb = Facebook(self.driver)
        self.logs.info("Invoke the browser")
        self.fb.usernmae("Piyush")
        self.fb.password("Piyush@123")
        self.fb.click_login()
        self.logs.info("complete exicution")
        self.driver.save_screenshot(r"C:\Users\ASUS\PycharmProjects\RahulShetty\Screenshots\piyush.png")

        assert self.driver.title == "Facebook – log in or sign up", "Test Fail"



