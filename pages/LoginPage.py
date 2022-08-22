from base.BasePage import BasePage
import time


class LoginForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator values
    _updateLaterButton = "//android.widget.Button[@index='3']"
    _signInButton = "//android.view.View[@content-desc='Sign In']"
    _signInWithEmailButton = "//android.widget.ImageView[@content-desc='Sign In with Email']"
    _enterEmail = "//android.widget.EditText[@text='Enter your Email ID']"
    _enterPassword = "//android.widget.EditText[@text='Enter your password']"
    _selectLoginButton = "//android.widget.Button[@content-desc='Sign In']"
    _allowButton = "//android.widget.Button[@text='Allow']"

    def clickLoginFormButton(self):
        self.clickElement(self._updateLaterButton, "xpath")

    def clickSignInButton(self):
        self.clickElement(self._signInButton, "xpath")

    def clickSignInWithEmailButton(self):
        self.clickElement(self._signInWithEmailButton, "xpath")

    def enterEmailAndPassword(self):
        self.clickElement(self._enterEmail, "xpath")
        self.sendText("cumarpun1234@gmail.com", self._enterEmail, "xpath")
        self.clickElement(self._enterPassword, "xpath")
        self.sendText("qwertyuiop", self._enterPassword, "xpath")
        self.driver.press_keycode(4)

    def selectLoginButton(self):
        self.clickElement(self._selectLoginButton, "xpath")
        time.sleep(15)
        self.isDisplayed(self._allowButton, "xpath")