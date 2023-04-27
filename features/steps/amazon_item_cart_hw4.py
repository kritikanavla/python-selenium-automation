from selenium.webdriver.common.by import By
from behave import given, when, then

search_box = (By.CSS_SELECTOR,"input#twotabsearchtextbox")
search_button =(By.CSS_SELECTOR, "#nav-search-submit-button")
pizza_cutter =(By.CSS_SELECTOR,"img[data-image-index='1']")
add_to_cart =(By.CSS_SELECTOR,"input#add-to-cart-button")
cart_button =(By.CSS_SELECTOR,"#attach-sidesheet-view-cart-button")
item_subtotal =(By.CSS_SELECTOR,"span#sc-subtotal-label-activecart")


@when('click on the item link')
def item_click(context):
    context.app.search_page.find_elements(pizza_cutter)[0].click()

@when('click on Add to Cart')
def click_to_add(context):
    context.app.search_page.click(add_to_cart)

@when('click on cart button')
def click_cart(context):
    context.app.search_page.click(cart_button)

@then('verify that cart has 1 item')
def verify_cart_item(context):
    actual_subtotal = context.app.search_page.get_text(item_subtotal)
    assert actual_subtotal == 'Subtotal (1 item):', f"Expected 'Subtotal (1 item)' but got {actual_subtotal}"
