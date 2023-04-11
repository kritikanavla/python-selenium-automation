from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


footer_links = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")
search_button = (By.ID, "nav-search-submit-button")
sign_in_button = (By.CSS_SELECTOR, "#nav-signin-tooltip a.nav-action-button")
#search_result = (By.CSS_SELECTOR, "div.sg-col-inner")
search_result = (By.CSS_SELECTOR, ".s-result-item")
#search_result = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
#product_image = (By.CSS_SELECTOR, "img.s-image")
product_image = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")
#product_title = (By.CSS_SELECTOR, "h2.a-color-base")
product_title = (By.CSS_SELECTOR, "h2 span.a-text-normal")



@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input text {search_word}')
def input_search_word(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)


@when('Click on search button')
def click_search(context):
    context.driver.find_element(*search_button).click()


@when('Click Sign In from popup')
def click_sign_in(context):
    context.driver.wait.until(EC.element_to_be_clickable(sign_in_button)).click()


@then('Verify signin popup appears')
def signin_popup_appears(context):
    context.driver.wait.until(EC.visibility_of_element_located(sign_in_button), message= 'Sign in button did not appear.')


@when('wait for {sec} seconds')
def wait_sec(context, sec):
    sleep(int(sec))


@then ('verify signin popup disappears')
def signin_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(sign_in_button), message='Sign in button did not dissappear.')


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

@then('Verify that every product has an name and an image')
def verify_product_name_and_image(context):
    all_products = context.driver.find_elements(*search_result)
    print(len(all_products))

    for product in all_products:
        #print(product)
        #image = product.find_element(*product_image)
        #sprint(image)
      assert product.find_element(*product_image).is_displayed(), 'Product image is missing'
  #      print(product.find_element(*product_title).text())
      assert product.find_element(*product_title).text, 'Product title is missing'


