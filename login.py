import time

from appium import webdriver
import pytest
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestLogin:
    def setup(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                       desired_capabilities={
                                           "platformName": "Android",
                                           "appium:platformVersion": "5.0.2",
                                           "appium:deviceName": "Android Emulator",
                                           "aapium:app": "enthu1.apk",
                                           "appium:appPackage": "com.enthuziastic.mobileapp.staging",
                                           "appium:appActivity": "com.enthuziastic.mobileapp.MainActivity"
                                       })

    # login with valid email and password
    def test_login(self):
        time.sleep(5)
        self.driver.find_element("accessibility id", "I'll do it later").click()
        sleep(2)
        self.driver.find_element("accessibility id", "Sign In").click()
        sleep(2)
        self.driver.find_element("accessibility id", "Sign In with Email").click()
        sleep(2)
        self.driver.find_element("xpath", "//android.widget.EditText[@text='Enter your Email ID']").click()
        self.driver.find_element("xpath", "//android.widget.EditText[@text='Enter your Email ID']").set_text("cumarpun1234@gmail.com")
        self.driver.find_element("xpath", "//android.widget.EditText[@text='Enter your password']").click()
        self.driver.find_element("xpath", "//android.widget.EditText[@text='Enter your password']").send_keys("qwertyuiop")
        self.driver.press_keycode(4)
        sleep(2)
        self.driver.find_element('xpath', '//android.widget.Button[@content-desc="Sign In"]').click()
        sleep(15)
        # EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Button[@text='Allow']"))
        assert self.driver.find_element("xpath", "//android.widget.Button[@text='Allow']").is_displayed()
        sleep(2)

    def teardown(self):
        self.driver.quit()
