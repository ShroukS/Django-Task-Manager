from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Chrome()  # Open a Chrome browser
    context.browser.implicitly_wait(1)   # Wait up to 10 seconds for elements to appear

def after_all(context):
    context.browser.quit()  # Close browser after all tests