import time
import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.ProductsPage import ProductsPage
from Pages.LogoutPage import LogoutPage
from Utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestFramwork():


    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        time.sleep(5)
        login = LoginPage(driver)
        login.enter_username(utils.Username)
        login.enter_password(utils.Password)
        login.click_submit()
        print("Page login succesfully")


    def test_products(self):
        time.sleep(4)
        driver = self.driver
        Products = ProductsPage(driver)
        Products.click_women()
        Products.click_Dresses()
        Products.click_SummerDresses()
        print("Summer dresses Page opened")
        quantity = driver.find_element_by_xpath("//h1/span[contains(text(),'Summer Dresses')]/following::span[1]").text
        print(quantity)

    def click_logout(self):
        time.sleep(3)
        driver = self.driver
        logout = LogoutPage(driver)
        logout.click_submit()




