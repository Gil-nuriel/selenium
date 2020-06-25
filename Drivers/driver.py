from selenium import webdriver
import unittest
import sys, os

class Driver(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        if(os.environ.get("CHROME")):
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        elif(os.environ.get("FIREFOX")):
            self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()
