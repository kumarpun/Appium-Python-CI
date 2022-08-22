from appium import webdriver

class Driver:
    saucelab_username = "oauth-cumarpun1234-49866"
    saucelab_accessKey = "53255d8d-4e39-43c6-90bf-22f066cffa03"

    def getDriverMethod(self):
        # Create "Desired Capabilities"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '13'
        desired_caps['deviceName'] = 'sdk_gphone64_x86_64'
        desired_caps['app'] = ('/Users/apple/Downloads/c8aec8df-a539-4ef7-8105-623a4c57edb3.apk')
        desired_caps['appPackage'] = 'com.enthuziastic.mobileapp.staging'
        desired_caps['appActivity'] = 'com.enthuziastic.mobileapp.MainActivity'

        # Create "Driver object"
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver

    def cloudDriver(self):
        caps = {}
        caps['appiumVersion'] = "1.22.1"
        caps['deviceName'] = "Google Pixel 3a GoogleAPI Emulator"
        caps['deviceOrientation'] = "portrait"
        caps['platformVersion'] = "10.0"
        caps['platformName'] = "Android"
        caps['app'] = "storage:filename=c8aec8df-a539-4ef7-8105-623a4c57edb3.apk"
        caps['name'] = "Android Test"
        caps['build'] = "Version 2.74.0"
        caps['username'] = self.saucelab_username
        caps['accessKey'] = self.saucelab_accessKey

        url = "https://oauth-cumarpun1234-49866:53255d8d-4e39-43c6-90bf-22f066cffa03@ondemand.eu-central-1.saucelabs.com:443/wd/hub" \

        driver = webdriver.Remote(url, caps, keep_alive=True)

        return driver
