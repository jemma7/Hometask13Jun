import imp


import pytest 
from locators.locators import LocatorsXpath
from page.basepage import Base
from page.greenkart import Elements_greenkart
from selenium import webdriver

@pytest.mark.usefixtures('set_up')
class Test(Base):

    def test_title(self):
        actual_page = Elements_greenkart.page_title(self)
        expected_page = ("GreenKart - veg and fruits kart", "https://rahulshettyacademy.com/seleniumPractise/#/")
        assert actual_page == expected_page

    def scroll_page(self):
        scroll = Elements_greenkart.scroll(self)
        assert 
        
    def test_mango(self):
        driver = self.driver
        # elements_action = Elements_greenkart(driver)
        mango_add_to_cart = Elements_greenkart.mango(driver)
        assert mango_add_to_cart == True

    def test_add_cart(self):
        driver = self.driver

        
