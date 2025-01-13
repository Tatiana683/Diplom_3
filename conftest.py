import pytest
from selenium import webdriver
from data import Constants

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        Constants.DRIVER_NAME = 'chrome'
        driver = webdriver.Chrome()
    else:
        Constants.DRIVER_NAME = 'firefox'
        driver = webdriver.Firefox()
    yield driver
    driver.quit()
