import unittest
import time
import HtmlTestRunner
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir+'\Resources')
sys.path.insert(0, parentdir+'\Drivers')
sys.path.insert(0, parentdir+'\Resources\PO')
from Locators import Locators
from TestData import TestData
from PO import tests_layers
from tests_layers import Google, Amazon
from driver import ChromeDriver, FirefoxDriver

class Test_001_Google(ChromeDriver):

    def test_001_user_try_to_search_on_google(self):
        self.google = Google(self.driver)
        self.google.search_google()

    def test_002_user_try_to_search_on_google(self):
        self.google = Google(self.driver)
        self.google.search_google2()

class Test_002_Amazon(ChromeDriver):

    def test_001_user_try_to_search_on_amazon(self):
        self.amazon = Amazon(self.driver)
        self.amazon.search_amazon()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=parentdir + '\Reports'))