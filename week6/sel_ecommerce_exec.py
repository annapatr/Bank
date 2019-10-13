from sel_ecommerce import SeleniumTest

# test execution
keyword = 'dress'
test1 = SeleniumTest()
test1.initialize_browser()
test1.open_website()

test1.verify_signin_button()
test1.verify_cart_status()
test1.verify_menu_items()
# test1.search_keyword(keyword)
# test1.verify_product_names(keyword)

test1.close_browser()