import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    # Automatically downloads and installs correct ChromeDriver version
    chromedriver_autoinstaller.install()

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    context.browser = webdriver.Chrome(options=options)


def after_all(context):
    context.browser.quit()
