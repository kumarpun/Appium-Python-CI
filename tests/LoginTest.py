import unittest
import pytest
from selenium import webdriver

import time
from pages.LoginPage import LoginForm

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lf = LoginForm(self.driver)

    @pytest.mark.run(order=5)
    def test_selectLoginButton(self):
        self.lf.selectLoginButton()

    @pytest.mark.run(order=4)
    def test_enterDataInForm(self):
        self.lf.enterEmailAndPassword()

    @pytest.mark.run(order=3)
    def test_selectSignInWithEmail(self):
        self.lf.clickSignInWithEmailButton()

    @pytest.mark.run(order=2)
    def test_selectSignIn(self):
        self.lf.clickSignInButton()

    @pytest.mark.run(order=1)
    def test_openLoginForm(self):
        time.sleep(10)
        self.lf.clickLoginFormButton()

# driver1 = Driver()
# log = cl.customLogger()
#
# driver = driver1.getDriverMethod()
# log.info("Launch App")

# bp = BasePage(driver)
# element = bp.waitForElement("I'll do it later", "id")
# element.click()
# bp.clickElement("//android.widget.Button[@content-desc='I'll do it later']", "xpath")
# element = bp.isDisplayed("//android.widget.Button[@content-desc='Update Now']", "xpath")
# bp.clickElement("//android.widget.Button[@content-desc='Update Now']", "xpath")
# element_id = driver.find_element("accessibility id", "I'll do it later")
# element_id.click()
# lf = LoginForm(driver)
