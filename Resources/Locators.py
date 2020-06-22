from selenium.webdriver.common.by import By

class Locators():
    SEARCH_TEXTBOX_AMAZON=(By.ID, "twotabsearchtextbox")
    SEARCH_TEXTBOX_GOOGLE=(By.NAME, "q")
    SEARCH_LINK_GOOGLE=(By.XPATH, "//*[@id='rso']/div[2]/div/div[1]/a/h3/span")
    


