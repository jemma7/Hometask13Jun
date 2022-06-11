from lib2to3.pgen2 import driver
import selenium
from basepage import Base
from locators.locators import LocatorsXpath
from selenium.webdriver import ActionChains

class Elements_greenkart:

    def __init__(self, driver):
        self.driver = driver

    def page_title(self):
        driver = self.driver
        get_title = driver.title
        current_url = driver.current_url
        return get_title, current_url

    def scroll(self):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        

    def mango(self):
        mango_button = self.driver.find_element_by_xpath(LocatorsXpath.mango)      
        # mango_button.click()
        actions = ActionChains(self.driver)
        actions.move_to_element(mango_button).perform()

    def add_to_cart(self):
        add_button = self.driver.find_element_by_xpath(LocatorsXpath.add_to_chart)
        add_button.click()
        # status = add.is_selected()
        # return status

    def price_item(self):
        price_button =  self.driver.find_element_by_xpath(LocatorsXpath.price)
        actions = ActionChains(self.driver)
        actions.move_to_element(price_button)
        items_button =  self.driver.find_element_by_xpath(LocatorsXpath.items)
        actions.move_to_element(items_button)

    def cart(self):
        cart_button = self.driver.find_element_by_xpath(LocatorsXpath.cart)
        cart_button.click()

    def products(self):
        product = self.driver.find_element_by_xpath(LocatorsXpath.product_name)
        product.select_by_visible_text('Mango')

    def proceed(self):
        proceed_button = self.driver.find_element_by_xpath(LocatorsXpath.proceed)
        proceed_button.click()

    def cart_open(self):
        cart = self.driver.find_element_by_xpath(LocatorsXpath.cart_page)      
        cart.select_by_visible_text('1')

    def order(self):
        place_order_button = self.driver.find_element_by_xpath(LocatorsXpath.place_order) 
        place_order_button.click()

    def terms(self):
        terms_button = self.driver.find_element_by_xpath(LocatorsXpath.terms_and_conditions)
        terms_button.click()
    
    def proceed(self):
        proceed_button = self.driver.find_element_by_xpath(LocatorsXpath.proceed)
        proceed_button.click()

    def message(self):
        message_page = self.driver.find_element_by_xpath(LocatorsXpath.success_message)
        message_page.select_by_visible_text("""Thank you, your order has been placed successfully
You'll be redirected to Home page shortly!!""")
        

    

