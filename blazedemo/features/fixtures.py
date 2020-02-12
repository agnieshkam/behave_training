from selenium import webdriver
from behave.fixture import fixture
from web.web import Web


@fixture
def browser_chrome(context, timeout=30, **kwargs):
    browser = webdriver.Chrome("C:/chromedriver.exe")
    web = Web(browser)
    context.web = web
    yield context.web
    browser.quit()
