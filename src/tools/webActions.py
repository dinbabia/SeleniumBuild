from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""
EC docu = https://selenium-python.readthedocs.io/waits.html

"""


class WebActions:
    """
    Contains Web Interactions.
    """
    
    def __init__(self, driver):
        self.driver = driver

    def web_click(self, by_locator):
        '''Web Interaction: Basic left click on a web element
            --------------------------------
        * @param: self.driver -> Initialized driver
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @return : None
        '''
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def web_element_visible(self, by_locator):
        '''Web Interaction: Check if the element is visible
            --------------------------------
        * @param: self.driver -> Initialized driver
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @return: boolean-> True if visible
        '''
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def web_get_element_text(self, by_locator):
        '''Web Interaction: Get the string/text of a web element
            --------------------------------
        * @param: self.driver -> Initialized driver
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @return: String/Text of a web element
        '''
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def web_get_element_value(self, by_locator):
        '''Web Interaction: Get the value attribute of a web element
            --------------------------------
        * @param: self.driver -> Initialized driver
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @return: Value attribute of a web element
        '''
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute('value')

    def web_get_title(self, title):
        '''Web Interaction: Get the title of the webpage
            --------------------------------
        * @param: self.driver -> Initialized driver
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @return: The title of the page as string
        '''
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def web_send_keys(self, by_locator, text):
        '''Web Interaction: Send a string to a web element
            --------------------------------
        * @param: self.driver -> Initialized driver
        * @param: by_locator -> Tuple (By Class Attribute, Element Locator/Selector)
        * @param: text -> The string to be inputted on an element
        * @return: None
        '''
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    

    

    



