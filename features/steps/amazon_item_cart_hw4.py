from selenium.webdriver.common.by import By
from behave import given, when, then

search_box = (By.CSS_SELECTOR,"input#twotabsearchtextbox")
search_button =(By.CSS_SELECTOR, "#nav-search-submit-button")
pizza_cutter =(By.CSS_SELECTOR,"img[data-image-index='1']")
add_to_cart =(By.CSS_SELECTOR,"input#add-to-cart-button")
cart_button =(By.CSS_SELECTOR,"#attach-sidesheet-view-cart-button")
item_subtotal =(By.CSS_SELECTOR,"span#sc-subtotal-label-activecart")

@given('Open Amazon HomePage')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('input {search_item} into search')
def input_search_item(context,search_item):
    context.driver.find_element(*search_box).send_keys(search_item)

@when('click on item search button')
def search_button_click(context):
    context.driver.find_element(*search_button).click()

@when('click on the item link')
def item_click(context):
    context.driver.find_elements(*pizza_cutter)[0].click()

@when('click on Add to Cart')
def click_to_add(context):
    context.driver.find_element(*add_to_cart).click()

@when('click on cart button')
def click_cart(context):
    context.driver.find_element(*cart_button).click()

@then('verify that cart has 1 item')
def verify_cart_item(context):
    actual_subtotal = context.driver.find_element(*item_subtotal).text
    assert actual_subtotal == 'Subtotal (1 item):', f"Expected 'Subtotal (1 item)' but got {actual_subtotal}"
