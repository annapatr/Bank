from selenium import webdriver
import time
import unittest

class SearchTests(unittest.TestCase):

    # test data
    __website_path = "http://automationpractice.com/index.php"

    @classmethod
    def setUpClass(cls):
        """initialize the browser and opens the page"""
        # paste the chromedriver in this location : C:\Program Files\Python37 (python installation folder)
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

        # open the page and enter the keyword
        cls.driver.get(cls.__website_path)


    def test_verify_product_names(self):
        # """get the product name of listed products, search should be done before this function"""
        try:
            word = 'dress' # to search for 
            self.search_keyword(word)
            product_name_list = self.driver.find_elements_by_xpath("//div[@id='center_column']//a[@class='product-name']")
            
            # assert number of products
            self.assertEqual(7, len(product_name_list))

            # assert product names
            for element in product_name_list:
                self.assertTrue(word.lower() in element.text.lower())
        
        except AssertionError as error:
            print(f"Handled Assertation: {error}")
        except Exception as other:
            print(f"Other exceptions occured : {other}")
            
    @classmethod
    def tearDownClass(cls):
        # close the browser
        cls.driver.quit()

    def search_keyword(self, word):
        search_field = self.driver.find_element_by_name('search_query')
        time.sleep(5)
        search_field.send_keys(word)
        time.sleep(5)
        search_field.submit()
        time.sleep(5)

# this line makes the current file executable file, verbosity helps to display more details in execution result
if __name__ == '__main__':
    unittest.main(verbosity=2)