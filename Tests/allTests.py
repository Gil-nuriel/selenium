import unittest
import time
import HtmlTestRunner
from ..Resources.Locators import Locators
from ..Resources.TestData import TestData
from ..Resources.PO import tests_layers
from tests_layers import Google, Amazon
from ..Drivers.driver import ChromeDriver, FirefoxDriver


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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output=parentdir + '\Reports'))
