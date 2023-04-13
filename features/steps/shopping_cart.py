from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC



@then('Verify "Your Shopping Cart is empty." text present')
def verify_text_in_cart(context):
    context.app.shopping_cart.verify_shopping_cart()
