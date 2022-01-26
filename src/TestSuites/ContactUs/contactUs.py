from tools.webActions import WebActions as WA
from selenium.webdriver.common.by import By

"""
These are the attributes available for By class:
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
"""


class ContactUsFeature(WA):
    
    """By Locators/ of a web element"""

    ContactUsButton = (By.CSS_SELECTOR, "#header-navbar > ul.nav.navbar-nav.navbar-right > li:nth-child(1) > a")
    BlogPageLink = (By.CSS_SELECTOR, "#header-navbar > ul.nav.navbar-nav.section-links > li:nth-child(6) > a")

    contact_us_form_name = (By.ID, "name") #1
    contact_us_form_emailadd = (By.ID, "emailadd") #2
    
    
    """Sample Test Input Values"""

    contact_us_form_name_sample = "Din" #1
    contact_us_form_emailadd_sample = "dinbabia@gmail.com" #2

    
    """Constructor of Page"""

    def __init__(self, driver):
        super().__init__(driver)


    """=====PAGE ACTIONS====="""

    def click_contact_us_button(self):
        self.web_click(self.ContactUsButton)
        
    def input_text_name(self):
        self.web_send_keys(self.contact_us_form_name, self.contact_us_form_name_sample)
    
    def input_text_emailadd(self):
        self.web_send_keys(self.contact_us_form_emailadd, self.contact_us_form_emailadd_sample)
    
    """PAGE ASSERTIONS"""

    
