import pytest
from selenium import webdriver
from data import Urls as u


@pytest.fixture()
def driver():

    driver = webdriver.Firefox()
    driver.get(u.samokat_url)
    yield driver

    driver.quit()