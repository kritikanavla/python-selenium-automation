from selenium.webdriver.common.by import By
from behave import when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

sign_in_button = (By.CSS_SELECTOR, "#nav-signin-tooltip a.nav-action-button")

@then('Verify Sign In page opens')
def sign_in_page_open(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin?'))

@then('Verify signin popup appears')
def signin_popup_appears(context):
    #context.driver.wait.until(EC.visibility_of_element_located(sign_in_button), message= 'Sign in button did not appear.')
    context.app.header.verify_signin_appears()

@when('wait for {sec} seconds')
def wait_sec(context, sec):
    sleep(int(sec))


@then ('verify signin popup disappears')
def signin_disappears(context):
    #context.driver.wait.until(EC.invisibility_of_element_located(sign_in_button), message='Sign in button did not disappear.')
    context.app.header.verify_signin_disappears()
