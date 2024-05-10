from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

cr_option = Options()
cr_option.add_experimental_option("debuggerAddress","localhost:9222")
driver = webdriver.Chrome(options=cr_option)
# driver.get("https://www.facebook.com/")
#
# driver.find_element(By.NAME, "email").send_keys("piyush")
# driver.find_element(By.NAME,"pass").send_keys("sdfsdg")
driver.find_element(By.NAME, "login").click()