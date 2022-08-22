from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import utilities.CustomLogger as cl

class BasePage:
    log = cl.customLogger()

    def __init__(self, driver=None):
        if driver is None:
            driver={}
        else:
            self.driver = driver

    def waitForElement(self, locatorvalue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorvalue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME,locatorvalue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().description("%s")' % (locatorvalue)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(%d)" % int(locatorvalue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("%s")' % locatorvalue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH,'%s' % (locatorvalue)))
            return element
        else:
            self.log.info("Locator value " + locatorvalue + "not found")

        return element

    def getElement(self, locatorvalue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorvalue, locatorType)
            self.log.info("Element found with LocatorType: " + locatorType + " with the locatorValue :" + locatorvalue)
        except:
            self.log.error(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue :" + locatorvalue)
        return element

    def clickElement(self, locatorvalue, locatorType="id, xpath"):
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorvalue, locatorType)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorvalue)
        except:
            self.log.error(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorvalue)

    def sendText(self, text, locatorvalue, locatorType="id, xpath"):
                try:
                    locatorType = locatorType.lower()
                    element = self.getElement(locatorvalue, locatorType)
                    element.send_keys(text)
                    self.log.info(
                        "Send text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorvalue)
                except:
                    self.log.error(
                        "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorvalue)

    def isDisplayed(self, locatorvalue, locatorType="xpath, id"):
            element: None
            try:
                locatorType = locatorType.lower()
                element = self.getElement(locatorvalue, locatorType)
                element.is_displayed()
                self.log.info(
                    " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorvalue + "is displayed ")
                return True
            except:
                self.log.error(
                    " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorvalue + " is not displayed")
                return False