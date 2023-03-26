from selenium.webdriver.common.by import By
from behave import given, when, then

footer_links = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")
search_button = (By.ID, "nav-search-submit-button")
@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input text {search_word}')
def input_search_word(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)


@when('Click on search button')
def click_search(context):
    context.driver.find_element(*search_button).click()


@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'

@then('Verify that footer has {expected_count} links')
def verify_footer_links(context, expected_count):
    expected_count= int(expected_count)
    actual_footer_count = context.driver.find_elements(*footer_links)
    print(actual_footer_count)
    print('\n actual number of links:', len(actual_footer_count))
    assert len(actual_footer_count) == expected_count, f"Expected {expected_count} links, but got {len(actual_footer_count)}"
