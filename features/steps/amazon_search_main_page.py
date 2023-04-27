from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC



#footer_links = (By.CSS_SELECTOR, "table.navFooterMoreOnAmazon td.navFooterDescItem")
#search_button = (By.ID, "nav-search-submit-button")
#search_result = (By.CSS_SELECTOR, "div.sg-col-inner")
#search_result = (By.CSS_SELECTOR, ".s-result-item")
#search_result = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
#product_image = (By.CSS_SELECTOR, "img.s-image")
#product_image = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")
#product_title = (By.CSS_SELECTOR, "h2.a-color-base")
#product_title = (By.CSS_SELECTOR, "h2 span.a-text-normal")



@given('Open Amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main_page()


@when('Input text {text}')
def input_search_word(context, text):
    #context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)
    context.app.header.input_search_text(text)


@when('Click on search button')
def click_search(context):
    #context.driver.find_element(*search_button).click()
    context.app.header.click_search()


@when('Click Sign In from popup')
def click_sign_in(context):
    context.driver.wait.until(EC.element_to_be_clickable(sign_in_button)).click()


@then('Verify that text {expected_result} is shown')
def verify_search_result(context, expected_result):
    #actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    #assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
    context.app.search_page.verify_search_result(expected_result)

@then('Verify that footer has {expected_count} links')
def verify_footer_links(context, expected_count):
    # expected_count= int(expected_count)
    # actual_footer_count = context.driver.find_elements(*footer_links)
    # print(actual_footer_count)
    # print('\n actual number of links:', len(actual_footer_count))
    # assert len(actual_footer_count) == expected_count, f"Expected {expected_count} links, but got {len(actual_footer_count)}"
    context.app.footer.verify_footer_links(expected_count)

@then('Verify that every product has an name and an image')
def verify_product_name_and_image(context):
    # all_products = context.driver.find_elements(*search_result)
    #
    # for product in all_products:
    #   assert product.find_element(*product_image).is_displayed(), 'Product image is missing'
    #   assert product.find_element(*product_title).text, 'Product title is missing'
    context.app.search_page.verify_product_name_and_image()

@when('Click on cart icon')
def click_on_cart(context):
    context.app.header.click_cart()
