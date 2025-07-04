import pytest
from selenium import webdriver

from page_object.pages.main_page import MainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    return main_page