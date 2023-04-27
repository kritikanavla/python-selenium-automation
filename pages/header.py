from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC



class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "#nav-signin-tooltip a.nav-action-button")
    ORDERS_LINK = (By.XPATH, "//a[@id='nav-orders']")
    CART_ICON = (By.CSS_SELECTOR, ".nav-cart-icon")

    def input_search_text(self, text):
        self.input_text(self.AMAZON_SEARCH_FIELD, text)

    def click_search(self):
        self.click(self.SEARCH_ICON)

    def click_cart(self):
        self.click(self.CART_ICON)

    def verify_signin_appears(self):
        self.wait_unit_element_visibility(
            EC.visibility_of_element_located(self.SIGN_IN_BUTTON),
            'Sign in button did not appear.')

    def verify_signin_disappears(self):
        self.wait_unit_element_visibility(
            EC.invisibility_of_element_located(self.SIGN_IN_BUTTON),
            'Sign in button did not disappear.')


    def orders_link_click(self):
        self.click(self.ORDERS_LINK)