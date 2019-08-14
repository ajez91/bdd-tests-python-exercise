from pytest_bdd import given, when, then
# from selenium.common.exceptions import ElementClickInterceptedException
import allure


# password ="autografy666"


@given('user is on Poczta Onet website')
def step_start_page(context):
    context.driver.get('http://poczta.onet.pl/')


@when('user fills valid username {username} and valid password {password} and submits it')
def step_set_login_in(context, username, password):
    context.driver.find_element_by_xpath('//span[contains(@class,"cmp-closebutton")]').click()
    context.driver.find_element_by_id('f_login').send_keys(username)
    context.driver.find_element_by_id('f_password').send_keys(password)
    context.driver.find_element_by_class_name('loginButton').click()


@when('user fills invalid username {username} and invalid password {password} and submits it')
def step_set_login_in(context, username, password):
    context.driver.find_element_by_xpath('//span[contains(@class,"cmp-closebutton")]').click()
    context.driver.find_element_by_id('f_login').send_keys(username)
    context.driver.find_element_by_id('f_password').send_keys(password)
    context.driver.find_element_by_class_name('loginButton').click()


@then('user can see email list')
def step_valid_login(context):
    context.driver.save_screenshot("screenshot-login.png")
    allure.attach.file('screenshot-login.png', 'Opening url')
    assert context.driver.find_element_by_id('mailList')


@then('user can see alert about invalid date')
def step_valid_login(context):
    try:
        alert_content = context.driver.find_element_by_css_selector("div.messageContent")
        assert alert_content.text == "Wprowadź poprawny adres e-mail" or "Niepoprawny e-mail lub hasło"
        print(alert_content)
        context.driver.save_screenshot("screenshot-invalidlogin.png")

    except:
        print("Alert not found!")
        print(alert_content)
        context.driver.save_screenshot("screenshot-invalidlogin.png")