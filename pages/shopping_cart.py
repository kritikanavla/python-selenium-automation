from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


YOUR_CART_IS_EMPTY = (By.CSS_SELECTOR, ".sc-your-amazon-cart-is-empty")

class ShoppingCart(Page):
    def verify_shopping_cart(self):
        actual_text = self.get_text(YOUR_CART_IS_EMPTY)
        expected_text = 'Your Amazon Cart is empty'
        assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'
