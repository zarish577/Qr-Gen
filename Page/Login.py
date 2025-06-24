from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QRlogin:
    username_locator = (By.CSS_SELECTOR, "input[placeholder='name@example.com']")
    password_locator = (By.CSS_SELECTOR, "input[placeholder='********']")
    button_locator = (By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(9)")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*self.username_locator).send_keys(username)
        time.sleep(6)
        self.driver.find_element(*self.password_locator).send_keys(password)
        time.sleep(5)
        wait = WebDriverWait(self.driver,50)
        button= wait.until(EC.element_to_be_clickable(self.button_locator))
        button.click()
        time.sleep(7)