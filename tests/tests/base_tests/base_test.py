import os
import unittest
from appium import webdriver
from tests.pages import CalculatorPage


class BaseTest(unittest.TestCase):
    """Basis for all tests."""
    def setUp(self):
        """Sets up desired capabilities and the Appium driver."""
        url = 'http://0.0.0.0:4723/wd/hub'
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Nexus'
        desired_caps['app'] = '/home/priscila/poc_calculator/calculator.apk'
        desired_caps['appPackage'] = 'com.maroyakasoft.dentak'
        desired_caps['appActivity'] = 'com.umadigital.dentak.MainActivity'

        self.driver = webdriver.Remote(url, desired_caps)

    def tearDown(self):
        """Shuts down the driver."""
        self.driver.quit()
