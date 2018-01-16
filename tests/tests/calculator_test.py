import os
import unittest
import time
from appium import webdriver
from time import sleep
from base_tests.base_test import BaseTest
from tests.pages import CalculatorPage



class CalculatorTest(BaseTest):

    UM   = "1"
    DOIS = "2"
    TRES = "3"
    QUATRO = "4"
    CINCO = "5"
    SEIS = "6"
    SETE = "7"
    OITO = "8"
    NOVE = "9"
    DEZ = "10"
    KEYBOARD_ANIMATION_DELAY = 4

    def setUp(self):
        BaseTest.setUp(self)
        self.calculator = CalculatorPage(self.driver)

    def test_mult(self):
        self.calculator.click_number(self.NOVE)
        self.calculator.click_mult()
        self.calculator.click_number(self.NOVE)
        self.calculator.click_equal()
        sleep(self.KEYBOARD_ANIMATION_DELAY)
        element = self.driver.find_element_by_id("com.maroyakasoft.dentak:id/display").get_attribute("text")
        assert element == "81"
        self.calculator.click_clear()

    def test_sum(self):
        self.calculator.click_number(self.NOVE)
        self.calculator.click_sum()
        self.calculator.click_number(self.NOVE)
        self.calculator.click_equal()
        sleep(self.KEYBOARD_ANIMATION_DELAY)
        element = self.driver.find_element_by_id("com.maroyakasoft.dentak:id/display").get_attribute("text")
        assert element == "18"
        self.calculator.click_clear()

    def test_sub(self):
        self.calculator.click_number(self.NOVE)
        self.calculator.click_sub()
        self.calculator.click_number(self.NOVE)
        self.calculator.click_equal()
        sleep(self.KEYBOARD_ANIMATION_DELAY)
        element = self.driver.find_element_by_id("com.maroyakasoft.dentak:id/display").get_attribute("text")
        assert element == "0"
        self.calculator.click_clear()

    def test_div(self):
        self.calculator.click_number(self.NOVE)
        self.calculator.click_div()
        self.calculator.click_number(self.NOVE)
        self.calculator.click_equal()
        sleep(self.KEYBOARD_ANIMATION_DELAY)
        element = self.driver.find_element_by_id("com.maroyakasoft.dentak:id/display").get_attribute("text")
        assert element == "1"
        self.calculator.click_clear()
