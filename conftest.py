# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import configparser
config= configparser.ConfigParser()
config.read("Utilities/config.ini")
import time
import undetected_chromedriver as uc
import warnings


@pytest.fixture(scope="class",autouse=True)
def driver(request):
    warnings.filterwarnings("ignore",category=UserWarning)
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled") 
    options.add_argument("--ignore-certificate-errors")
    service = Service("chromedriver.exe")  # Update path if needed
    request.cls.driver = uc.Chrome(service=service, options=options,version_main=138)
    request.cls.driver.maximize_window()
    request.cls.driver.get(config.get("URL","base_url"))
    time.sleep(15)
    yield 
    request.cls.driver.quit()
 
