import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from assertlib import *
import time
from picotest.utils import *
from picotest import Session


class SignUp(unittest.TestCase):    
    def test_1_required(self): 
        # start your browser session  
        Session.driver.get("https://demoqa.com/automation-practice-form")
        """This will verify that the correct number of required fields exists after hitting submit with no data entered."""   
        time.sleep(3)  
        # click submit
        Session.driver.find_element_by_class_name("btn-primary").click()
        
        # verify the correct number of required fields are present
        rf = len(Session.driver.find_elements_by_css_selector("input[required='']"))
        self.assertEqual(rf, 6)      
        print("All Required Fields Present...")  
        
        # NOTE - future tests might include filling in required fields one at a time, clicking submit, and validating that you can't proceed until all are filled out.
        
    def test_2_form(self):   
        """This will fill out the enitre form."""     
        # first name
        fn = Session.driver.find_element_by_id("firstName")
        fn.click()
        fn.clear()
        fn.send_keys("Test First") 
        print("First Name Entered...")     
        
        # last name
        ln = Session.driver.find_element_by_id("lastName")
        ln.click()
        ln.clear()
        ln.send_keys("Test Last") 
        print("Last Name Entered...")     
        
        # email
        email = Session.driver.find_element_by_id("userEmail")
        email.click()
        email.clear()
        email.send_keys("email@example.com")
        print("Email Entered...")     
        
        # click genders
        Session.driver.find_element_by_xpath("//div[@id='genterWrapper']/div[2]/div/label").click()
        Session.driver.find_element_by_xpath("//div[@id='genterWrapper']/div[2]/div[2]/label").click()
        Session.driver.find_element_by_xpath("//div[@id='genterWrapper']/div[2]/div[3]/label").click()
        print("Gender Chosen...")     
        
        # phone number
        pn = Session.driver.find_element_by_id("userNumber")
        pn.click()
        pn.clear()
        pn.send_keys("5555555555")
        print("Phone Number Entered...")   
        
        # subjects
        sub = Session.driver.find_element_by_id("subjectsInput")
        sub.click()
        sub.clear()
        sub.send_keys("Commerce")
        Session.driver.find_element_by_id("react-select-2-option-0").click()
        print("Subject Entered...")     
        
        # hobbies check
        Session.driver.find_element_by_xpath("//div[@id='hobbiesWrapper']/div[2]/div/label").click()
        Session.driver.find_element_by_xpath("//div[@id='hobbiesWrapper']/div[2]/div[2]/label").click()
        Session.driver.find_element_by_xpath("//div[@id='hobbiesWrapper']/div[2]/div[3]/label").click()
        
        # hobbies uncheck
        Session.driver.find_element_by_xpath("//div[@id='hobbiesWrapper']/div[2]/div[3]/label").click()
        Session.driver.find_element_by_xpath("//div[@id='hobbiesWrapper']/div[2]/div[2]/label").click()
        Session.driver.find_element_by_xpath("//div[@id='hobbiesWrapper']/div[2]/div/label").click()
        print("Hobbies Checked / Unchecked...")                  

        # current address
        ca = Session.driver.find_element_by_id("currentAddress")
        ca.click()
        ca.clear()
        ca.send_keys("123 Test Street")
        print("Address Entered...")   
        
        # toggle through states (Note: each state selection results in a different list of cities.  Also, dropdown contents can also be verified as well)
        Session.driver.find_element_by_id("state").click()
        Session.driver.find_element_by_id("react-select-3-option-0").click()
        Session.driver.find_element_by_id("state").click()
        Session.driver.find_element_by_id("react-select-3-option-1").click()
        Session.driver.find_element_by_id("state").click()
        Session.driver.find_element_by_id("react-select-3-option-2").click()
        Session.driver.find_element_by_id("state").click()
        Session.driver.find_element_by_id("react-select-3-option-3").click()        
        print("State Selected...")  
        
        # select city
        Session.driver.find_element_by_id("city").click()
        Session.driver.find_element_by_id("react-select-4-option-1").click()
        print("City Selected...") 
        
        # DOB
        dob = Session.driver.find_element_by_id("dateOfBirthInput")
        dob.click()
        dob.clear()
        dob.send_keys("11 January 2020")
        print("DOB Selected...")
        
        # click submit
        Session.driver.find_element_by_class_name("btn-primary").click()
    
        # verify thanks
        thanks = Session.driver.find_element_by_id("example-modal-sizes-title-lg").get_attribute('innerHTML')
        print(thanks)
        self.assertEqual(thanks, "Thanks for submitting the form")
        
        # NOTE - future tests may include storing form data and validating it against what is listed on the thank you screen.