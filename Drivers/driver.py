from selenium import webdriver
import unittest
import sys, os

class Driver(unittest.TestCase):
    def setUp(self):
        if(os.environ.get("CHROME")):
            self.driver = webdriver.Chrome()
        elif(os.environ.get("FIREFOX")):
            self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()
