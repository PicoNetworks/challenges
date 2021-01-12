import os
import unittest
from selenium import webdriver
from picotest.utils import *

"""
    Initial class that launches appium session. 
    Connects to altunity driver.
"""
class Session:
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()        

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()