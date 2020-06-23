from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


from ..Locators import Locators
from ..TestData import TestData
from actions import actions


class Google(actions):
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.BASE_URL_GOOGLE)

    def search_google(self):
        self.driver.find_element(*Locators.SEARCH_TEXTBOX_GOOGLE).clear()
        self.enter_text_and_search(
            Locators.SEARCH_TEXTBOX_GOOGLE, TestData.SEARCH_TERM_GOOGLE_001)

    def search_google2(self):
        self.driver.find_element(*Locators.SEARCH_TEXTBOX_GOOGLE).clear()
        self.enter_text_and_search(
            Locators.SEARCH_TEXTBOX_GOOGLE, TestData.SEARCH_TERM_GOOGLE_002)
        self.click_on_link(Locators.SEARCH_LINK_GOOGLE)
        if(TestData.text_inside_stackoverflow in self.driver.page_source):
            print("SUCCES")
        else:
            print("FAIL")


class Amazon(actions):
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.BASE_URL_AMAZON)

    def search_amazon(self):
        self.driver.find_element(*Locators.SEARCH_TEXTBOX_AMAZON).clear()
        self.enter_text_and_search(
            Locators.SEARCH_TEXTBOX_AMAZON, TestData.SEARCH_TERM_AMAZON_001)
