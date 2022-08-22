from appium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

saucelab_username = "oauth-cumarpun1234-49866"
saucelab_accessKey = "53255d8d-4e39-43c6-90bf-22f066cffa03"

caps = {}
caps['appiumVersion'] = "1.22.1"
caps['deviceName'] = "Google Pixel 3a GoogleAPI Emulator"
caps['deviceOrientation'] = "portrait"
caps['platformVersion'] = "10.0"
caps['platformName'] = "Android"
caps['app'] = "storage:filename=c8aec8df-a539-4ef7-8105-623a4c57edb3.apk"
caps['name'] = "Android Test"
caps['build'] = "Version 2.74.0"
caps['username'] = saucelab_username
caps['accessKey'] = saucelab_accessKey

url = "https://oauth-cumarpun1234-49866:53255d8d-4e39-43c6-90bf-22f066cffa03@ondemand.eu-central-1.saucelabs.com:443/wd/hub" \

driver = webdriver.Remote(url, caps, keep_alive=True)

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

ele = wait.until(lambda x: x.find_element("accessibility id", "I'll do it later"))
ele.click()

driver.quit()