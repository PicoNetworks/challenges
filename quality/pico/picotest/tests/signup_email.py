import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from picotest.utils import *
from picotest import Session


class SignUp(unittest.TestCase):    
    def test_1_required(self):  
        Session.driver.get("https://staging.trypico.com/signup")
        """This will verify the required fields and disabled Next button."""
        # click logo to trigger required fields      
        time.sleep(3)  
        Session.driver.find_element_by_class_name("logo").click()
        
        # verify the required fields
        assert Session.driver.find_element_by_class_name("FormInput-module_error__125Gq")
        
        # verify disabled Next button
        assert Session.driver.find_element_by_class_name("Button-module_disabled__3y46V")
        print("Required Fields Present / Next Button Disabled...")  
        
        # quickly verify presence of the 'X' button
        assert Session.driver.find_element_by_class_name("_95ecdcb")
        
    def test_2_email(self):  
        """This will complete the sign up form using email."""    
        # enter email   
        email = Session.driver.find_element_by_class_name("FormInput-module_input__l-msZ")
        email.click()
        email.clear()
        email.send_keys("email@example.com")
        
        # click Next
        Session.driver.find_element_by_class_name("Button-module_primary__gfhd3").click()
        time.sleep(3)
        print("Email Entered...")     
        error = Session.driver.find_element_by_class_name("error")
        if error.is_displayed:
            raise Exception(error.get_attribute('outerText'))
        else:
            pass
        
        # verify "Let's get started." text
        assert Session.driver.find_element_by_class_name("_49f9433")