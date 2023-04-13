from selenium.webdriver.common.by import By
from pages.base_page import Page

class Footer(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    FOOTER_LINKS = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")

    def input_search_text(self, text):
        self.input_text(self.AMAZON_SEARCH_FIELD, text)

    def click_search(self):
        self.click(self.SEARCH_ICON)

    def verify_footer_links(self, expected_count):
        expected_count = int(expected_count)
        actual_footer_count = self.find_elements(self.FOOTER_LINKS)
        print(actual_footer_count)
        print('\n actual number of links:', len(actual_footer_count))
        assert len(
            actual_footer_count) == expected_count, f"Expected {expected_count} links, but got {len(actual_footer_count)}"
