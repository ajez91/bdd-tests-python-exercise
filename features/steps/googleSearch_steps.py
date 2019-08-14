from behave import given, when, then


@given('a web browser is at the Google home page')
def step_start_page(context):
    context.driver.get('http://poczta.onet.pl/')


@given('Google search results for "panda" are shown')
def step_start_page(context):
    context.driver.get('http://poczta.onet.pl/')


@when('the user enters "panda" into the search bar')
def step_set_login_in(context):
    context.driver.get('http://poczta.onet.pl/')


@when('the user clicks on the "Images" link at the top of the results page')
def step_set_login_in(context):
    context.driver.get('http://poczta.onet.pl/')


@then('links related to "panda" are shown on the results page')
def step_valid_login(context):
    context.driver.get('http://poczta.onet.pl/')


@then('images related to "panda" are shown on the results pag')
def step_valid_login(context):
    context.driver.get('http://poczta.onet.pl/')