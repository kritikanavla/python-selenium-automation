from selenium.webdriver.common.by import By
from behave import given, when, then

best_sellers_locater = (By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")
elements_best_sellers = (By.CSS_SELECTOR, "div#zg_header a")


@given('Open Amazon home')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('click on Best Sellers')
def best_sellers_click(context):
    context.driver.find_element(*best_sellers_locater).click()

@then('Verify that there are {expected_result} links')
def verify_links(context, expected_result):
    expected_result = int(expected_result)
    actual_result = context.driver.find_elements(*elements_best_sellers)
    assert len(actual_result) == expected_result, f"Expected {expected_result} links, but found {len(actual_result)} links."