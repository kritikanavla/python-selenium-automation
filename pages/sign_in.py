from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignIn(Page):
    SIGN_IN_LABLE = (By.XPATH, "//h1[@class='a-spacing-small']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='ap_email']")


    def verify_sign_in_page(self):
        expected_result = "Sign in"
        actual_result = self.get_text(self.SIGN_IN_LABLE)
        assert expected_result == actual_result, f"couldn't find {expected_result} lable, found :{actual_result} lable"
        email_input = self.find_element(self.EMAIL_INPUT)
        print(email_input)
        assert email_input, f"Email input element is missing. "
        print('Test case passed')
