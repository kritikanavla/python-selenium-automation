from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PRIVACY_NOTICE = By.CSS_SELECTOR, "[href='https://www.amazon.com/privacy']"


@given('Open Amazon T&C page')
def open_t_and_c(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_current_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on Amazon Privacy Notice link')
def privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()


@when('Switch to the newly opened window')
def switch_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    windows = context.driver.window_handles[1]
    context.driver.switch_to.window(windows)
    context.current_window = context.driver.current_window_handle
    print("After switch")
    print(context.current_window)

@then('Verify Amazon Privacy Notice page is opened')
def privacy_notice_page_open(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ'), message="Amazon Privacy Notice page did not open")


@then('User can close new window and switch back to original')
def close_new_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)

