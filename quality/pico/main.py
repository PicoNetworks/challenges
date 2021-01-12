import unittest
from HtmlTestRunner import HTMLTestRunner
# launch browser
from picotest import Session
# pytests
from picotest.tests import signup_email
from picotest.tests import signup_google
from picotest.tests import signup_demoqa

try:
    # start your session
    Session.setUpClass()
    
    # load all test cases from given module and create a test suite
    suite = unittest.TestLoader().loadTestsFromModule(signup_demoqa)
    suite.addTests(unittest.TestLoader().loadTestsFromModule(signup_email)) 
    suite.addTests(unittest.TestLoader().loadTestsFromModule(signup_google)) 
    
    # create output
    runner = HTMLTestRunner(output='Test_Results', combine_reports=True, add_timestamp=True, report_name="Pico Sign Up Results")
    # run the suite
    runner.run(suite)
    
finally:     
    Session.tearDownClass()
    
    
    

    
    