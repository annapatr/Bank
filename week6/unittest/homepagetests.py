from selenium import webdriver
import time
import unittest

class HomePageTests(unittest.TestCase):

    # test data
    __website_path = "http://automationpractice.com/index.php"

    @classmethod
    def setUpClass(cls):
        """initialize the browser and opens the page"""
        # paste the chromedriver in this location : C:\Program Files\Python37 (python installation folder)
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # open the page and enter the keyword
        cls.driver.get(cls.__website_path)
    
    def test_verify_signin_button(self):
        # check sign in button 
        signin_button = self.driver.find_element_by_link_text("Sign in")
        # signin_button.tag_name

        self.assertTrue(signin_button.is_enabled)
        print(self.driver.current_url)
        print(self.driver.current_window_handle)
        self.assertEqual("My Store", self.driver.title)
        # print(self.driver.current_url)


    def test_verify_cart_status(self):
        css_selector = 'span.ajax_cart_no_product'
        cart_status = self.driver.find_element_by_css_selector(css_selector)
        self.assertTrue(cart_status.is_displayed)

    @classmethod
    def tearDownClass(cls):
        # close the browser
        cls.driver.quit()

    #  below methods do not start with test_ so these are not test cases, but we can still used them in our above test cases
    def verify_menu_items(self):
        top_menu_list = self.driver.find_elements_by_tag_name("li")
        print(len(top_menu_list))

    def minimize_browser(self):
        self.driver.minimize_window()


# this line makes the current file executable file, verbosity helps to display more details in execution result
if __name__ == '__main__':
    unittest.main(verbosity=2)