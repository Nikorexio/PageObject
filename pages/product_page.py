from .base_page import BasePage
from .locators import BuyPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*BuyPageLocators.ADD_TO_CART)
        button.click()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*BuyPageLocators.ADD_TO_CART), "Нет кнопки добавить в корзину"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        #time.sleep(120)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def print_name_and_price(self):
        name = self.browser.find_element(*BuyPageLocators.PRODUCT_NAME).text
        price = self.browser.find_element(*BuyPageLocators.PRODUCT_PRICE).text

    def is_price_equal_to_basket_price(self):
        price_base = self.browser.find_element(*BuyPageLocators.PRODUCT_PRICE).text
        price_basket = self.browser.find_element(*BuyPageLocators.PRODUCT_PRICE_BASKET).text
        assert price_basket == price_base, "price are not equal"

    def is_name_equal_to_basket_price(self):
        name_base = self.browser.find_element(*BuyPageLocators.PRODUCT_NAME).text
        name_basket = self.browser.find_element(*BuyPageLocators.PRODUCT_NAME_BASKET).text
        assert name_base == name_basket, "name are not equal"
