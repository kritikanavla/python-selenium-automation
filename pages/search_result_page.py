from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResult(Page):
    SEARCH_RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    SEARCH_RESULT = (By.CSS_SELECTOR, ".s-result-item")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h2 span.a-text-normal")
    def verify_search_result(self, expected_result):
        actual_result = self.find_element(self.SEARCH_RESULT_TEXT).text
        assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'

    def verify_product_name_and_image(self):
        all_products = self.find_elements(self.SEARCH_RESULT)
        # print(len(all_products))

        for product in all_products:
            assert product.find_element(self.PRODUCT_IMAGE).is_displayed(), 'Product image is missing'
            assert product.find_element(self.PRODUCT_TITLE).text, 'Product title is missing'