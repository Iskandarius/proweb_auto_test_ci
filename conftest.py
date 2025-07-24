import pytest
from selenium import webdriver

@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver


@pytest.fixture
def driver_edge():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver


# @pytest.fixture
# def driver_firefox():
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.implicitly_wait(10)

#     yield driver
