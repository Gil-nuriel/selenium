from selenium import webdriver
import unittest
import sys, os

class Driver(unittest.TestCase):
    def setUp(self):
        if(os.environ.get("CHROME")):
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(options=chrome_options)
        elif(os.environ.get("FIREFOX")):
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--headless")
            self.driver = webdriver.Firefox(options=firefox_options)

    def tearDown(self):
        self.driver.quit()
