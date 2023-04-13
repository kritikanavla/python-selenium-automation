from selenium.webdriver.common.by import By
from behave import given, when, then

color_options = (By.CSS_SELECTOR,"#variation_color_name li")
current_color = (By.CSS_SELECTOR, "#variation_color_name span.selection")

@given('Open Amazon product page for {product_id}')
def open_product_page(context,product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')

@then('verify user can click through colors')
def select_product_colors(context):
    #context.driver.find_element(*color_options).click()
    all_elements = context.driver.find_elements(*color_options)
    expected_colors = ['012-20', '012-21', '012-22', '012-23', '012-25']

    actual_color = []
    for one_color_element in all_elements[:5]:
        one_color_element.click()
        current_color_selection = context.driver.find_element(*current_color).text
        print('current color:', current_color_selection)
        actual_color += [current_color_selection]
        print('Actual color', actual_color)

    assert expected_colors == actual_color, f"Expected {expected_colors}, but got{actual_color}"
