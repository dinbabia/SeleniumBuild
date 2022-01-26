import pytest
from TestSuites.test_base import BaseTest
from TestSuites.ContactUs.contactUs import ContactUsFeature 
from TestSuites.conftest import DriverInfo



class Test_Contact_Us(BaseTest):

    # ===================================================================================
    def test_contact_us_button(self):
        '''Test the contact us button on the Homepage
        Test Case 000-001 : Contact Us Button
        '''
        self.contact_us = ContactUsFeature(self.driver)
        print(DriverInfo.base_url , DriverInfo.environment , DriverInfo.browser)
        self.contact_us.click_contact_us_button()
        assert True
        
    def test_contact_us_form_inputs(self):
        '''Test the contact us form inputs
        Test Case 000-002 : Contact Us Form Inputs
        '''
        self.contact_us = ContactUsFeature(self.driver)
        self.contact_us.click_contact_us_button()
        self.contact_us.input_text_name() 
        self.contact_us.input_text_emailadd()
        assert True
        
        

        



