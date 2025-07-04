from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QRlogin:
    username_locator = (By.CSS_SELECTOR, "input[placeholder='name@example.com']")
    password_locator = (By.CSS_SELECTOR, "input[placeholder='********']")
    button_locator = (By.XPATH, "//button[text()='Sign In']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):

        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.username_locator))
        wait.until(EC.element_to_be_clickable(*self.username_locator)).send_keys(username)

        #self.driver.find_element(*self.username_locator).send_keys(username)
        #time.sleep(8)
        
        self.driver.find_element(*self.password_locator).send_keys(password)
        time.sleep(8)
        
        self.driver.find_element(*self.button_locator).click()
       
        time.sleep(7)