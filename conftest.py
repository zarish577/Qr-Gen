import pytest
import os
import warnings
import configparser
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
config = configparser.ConfigParser()
config.read("Utilities/config.ini")

@pytest.fixture(scope="class", autouse=True)
def driver(request):
    warnings.filterwarnings("ignore", category=UserWarning)

    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--ignore-certificate-errors")

    # 🧠 Detect CI or local run
    is_ci = os.getenv("CI") == "true" or os.getenv("RUN_ENV") == "ci"

    if is_ci:
        # ✅ Headless mode for GitHub Actions / CI
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = uc.Chrome(options=options)
        driver.set_window_size(1920, 1080)
    else:
        # ✅ Visible Chrome for local automation
        service = Service("chromedriver.exe")  # ✅ Local exe
        driver = uc.Chrome(service=service, options=options, version_main=138)
        driver.maximize_window()

    driver.get(config.get("URL", "base_url"))
    request.cls.driver = driver
    yield
    driver.quit()
