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
        # click logo to trigger required field      
        time.sleep(3)  
        Session.driver.find_element_by_class_name("logo").click()
        
        # verify the required field
        assert Session.driver.find_element_by_class_name("FormInput-module_error__125Gq")
        
        # verify disabled Next button
        assert Session.driver.find_element_by_class_name("Button-module_disabled__3y46V")
        print("Required Fields Present / Next Button Disabled...")  
        
        # quickly verify presence of the 'X' button
        assert Session.driver.find_element_by_class_name("_95ecdcb")
        
    def test_2_email(self):  
        """This will complete the sign up form using Google."""    
        # click Google button
        Session.driver.find_element_by_class_name("Button-module_button__3M3oN").click()
        
        # switch to pop up window
        time.sleep(3)  
        Session.driver.switch_to.window(Session.driver.window_handles[1])
        
        # enter email
        email = Session.driver.find_element_by_id("identifierId")
        email.click()
        email.clear()
        email.send_keys("email@example.com")
        
        # click Next
        Session.driver.find_element_by_id("identifierNext").click()
        print("Email Entered...") 
        
        # error message
        time.sleep(3)
        error = Session.driver.find_element_by_xpath("//div[@id='view_container']/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/div[2]/div[2]/div").text
        if error:
            raise Exception(error)
        else:
            pass 
            print("Captcha present may be present")