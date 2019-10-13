from selenium import webdriver
import time

class SeleniumTest():

    # test data
    __website_path = "http://automationpractice.com/index.php"
    # __browser_path = "../chromedriver_win32/chromedriver.exe" # we will not use this since we put the driver in python folder

    def initialize_browser(self):
        """initialize the browser"""
        # self.driver = webdriver.Chrome(self.__browser_path)

        # paste the chromedriver in this location : C:\Program Files\Python37 (python installation folder)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def open_website(self):
        # open the page and enter the keyword
        self.driver.get(self.__website_path)

    def search_keyword(self, word):
        search_field = self.driver.find_element_by_name('search_query')
        time.sleep(5)
        search_field.send_keys(word)
        time.sleep(5)
        search_field.submit()
        time.sleep(5)

    def verify_product_names(self, word):
        """get the product name of listed products, search should be done before this function"""
        #     //*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[2]
        product_name_list = self.driver.find_elements_by_xpath("//div[@id='center_column']//a[@class='product-name']")
        for element in product_name_list:
            if word.lower() in element.text.lower():
                print(f"Test passed for {element.text}")
            else:
                print(f"Test FAILED for {element.text}")
    
    def verify_signin_button(self):
        # check sign in button 
        # signin_button = self.driver.find_element_by_class_name("login")
        # signin_button = self.driver.find_element_by_link_text("Sign in")
        signin_button = self.driver.find_element_by_partial_link_text("Sign")

        if signin_button.is_displayed:
            print("sign in button test passed")
        else:
            print("sign in button FAILED")

    def verify_cart_status(self):
        # xpath_sample = "//tag[@attribute = 'value']/a/span[href='value.html']"
        # xpath_sample1 = "//*[@attribute = 'value']//a/span[@class='submit']"
    
        # xpath of emptry cart = "//*[@id='header']/div[3]/div/div/div[3]/div/a/span[5]"
        # css selector of emptry cart = "#header > div:nth-child(3) > div > div > div:nth-child(3) > div > a > span.ajax_cart_no_product"

        xpath = "//span[@class='ajax_cart_no_product']"
        css_selector = '#header span.ajax_cart_no_product'
        
        # cart_status = self.driver.find_element_by_xpath(xpath)
        cart_status = self.driver.find_element_by_css_selector(css_selector)

        if cart_status.is_displayed:
            print(f"Cart status Passed , text: {cart_status.text}")
        else: 
            print("cart status FAILED")

    def verify_menu_items(self):
        top_menu_list = self.driver.find_elements_by_tag_name("li")
        print(len(top_menu_list))

    def minimize_browser(self):
        self.driver.minimize_window()

    def close_browser(self):
        # close the browser
        self.driver.quit()