from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

BASE_URL = 'http://127.0.0.1:8000'


@given('I am in "Home" page')
def step_impl(context):
    context.browser.get(f'{BASE_URL}')


@when('I click on "Add New Task"')
def step_impl(context):
    add_task_button = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button[contains(text(), "Add New Task")]'))
    )
    add_task_button.click()


@then('I should see "Create Task" listed on the dashboard')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), "Create Task")
    )


@given('I am in "Create Task" page')
def step_impl(context):
    context.browser.get(f'{BASE_URL}/create')


@when('I fill in "Title" with "{title}"')
def step_impl(context, title):
    title_input = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'title'))
    )
    title_input.send_keys(title)


@when('I fill in "Description" with "{description}"')
def step_impl(context, description):
    description_input = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'description'))
    )
    description_input.clear()
    description_input.send_keys(description)


@when('I fill in "Due date" with "{due_date}"')
def step_impl(context, due_date):
    due_date_input = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'due_date'))
    )
    due_date_input.send_keys(due_date)


@when('I click on "Save"')
def step_impl(context):
    save_button = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button[contains(text(), "Save")]'))
    )
    save_button.click()


@then('I should be redirected to "Home" page')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), "Task Manager")
    )


@then('I should see "{title}" in the Home page')
def step_impl(context, title):
    WebDriverWait(context.browser, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), title)
    )


@when('I click on "Edit" for "{task}"')
def step_impl(context, task):
    edit_button = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            f'//tr[td[contains(text(), "{task}")]]//button[contains(text(), "Edit")]'
        ))
    )
    edit_button.click()


@then('I should be redirected to "Edit Task" page')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), "Edit Task")
    )


@when('I select the tasks "{task1}" and "{task2}"')
def step_impl(context, task1, task2):
    for task_title in [task1, task2]:
        checkbox = WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                f'//tr[td[contains(text(), "{task_title}")]]//input[@type="checkbox"]'
            ))
        )
        checkbox.click()


@when('I click on "Mark as Complete"')
def step_impl(context):
    save_button = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button[contains(text(), "Mark as Complete")]'))
    )
    save_button.click()


@then('I should "✔ Completed" statuses for tasks "{task1} and "{task2}"')
def step_impl(context, task1, task2):
    for task in [task1, task2]:
        row_xpath = f'//tr[td[contains(text(), "{task}")]]'
        status_xpath = f'{row_xpath}/td[contains(text(), "✔ Completed")]'
        WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, status_xpath))
        )


@when('I click on "Delete" for "{task}"')
def step_impl(context, task):
    edit_button = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            f'//tr[td[contains(text(), "{task}")]]//button[contains(text(), "Delete")]'
        ))
    )
    edit_button.click()


@then('I should be redirected to "Delete Task" page')
def step_impl(context):
    # TODO: Redirect to the dashboard url
    WebDriverWait(context.browser, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), "Delete Task")
    )


@when('I click on "Yes, Delete"')
def step_impl(context):
    save_button = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button[contains(text(), "Yes, Delete")]'))
    )
    save_button.click()


@when('I click on "Delete Selected"')
def step_impl(context):
    delete_button = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button[contains(text(), "Delete Selected")]'))
    )
    delete_button.click()


@then('I should not see "{task1}" and "{task2}" in "Home" page')
def step_impl(context, task1, task2):
    def not_present(task):
        try:
            sleep(10)
            WebDriverWait(context.browser, 10).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), task)
            )
            return False
        except TimeoutException:
            return True

    assert not_present(task1), f'"{task1}" still visible on page'
    assert not_present(task2), f'"{task2}" still visible on page'
