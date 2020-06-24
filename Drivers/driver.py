from selenium import webdriver
import unittest
import sys, os

class Driver(unittest.TestCase):
    def setUp(self):
        if(os.environ["chrome"]):
            self.driver = webdriver.Chrome()
        if(os.environ["firefox"]):
            self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()
