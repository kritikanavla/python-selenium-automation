from pages.footer import Footer
from pages.main_page import MainPage
from pages.header import Header
from pages.search_result_page import SearchResult
from pages.shopping_cart import ShoppingCart
from pages.sign_in import SignIn


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_page = SearchResult(self.driver)
        self.footer = Footer(self.driver)
        self.sign_in = SignIn(self.driver)
        self.shopping_cart = ShoppingCart(self.driver)