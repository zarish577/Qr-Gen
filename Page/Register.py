from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

class Login_Page:
    User_name = (By.CSS_SELECTOR, "#create-account-email")
    Pass_word = (By.CSS_SELECTOR, "#create-account-password")  
    SignUp_Button = (By.CSS_SELECTOR, "button[type='submit']")
    Email_Already_exist_message= (By.CSS_SELECTOR,".MuiTypography-root.MuiTypography-body2.css-g4qpks")
    Validation_Messages=(By.CSS_SELECTOR,"div.MuiStack-root p.MuiTypography-body2")
    
    
    def __init__(self, driver):
        self.driver = driver

    def username(self, user_name):
        username_one = self.driver.find_element(*self.User_name)
        username_one.clear()
        username_one.send_keys(user_name) 
        time.sleep(9)        

    def password(self, pass_word):
        password = self.driver.find_element(*self.Pass_word)
        password.clear()
        password.send_keys(pass_word)
        time.sleep(6)

    def login(self):
     try:
        #Wait untill the captcha box gets selected and signUp button gets visible
        wait= WebDriverWait (self.driver,50)
        button= wait.until(EC.element_to_be_clickable(self.SignUp_Button))
        button.click()
     except:
        print("Element is not clickable until you click on the captcha check box manually")

    def disable_login_button(self):
        button= self.driver.find_element(*self.SignUp_Button)
        is_disabled=button.get_attribute("disabled")
        return is_disabled
        
    def Email_Already_Exist_Message(self):
        time.sleep(5)
        Message_one= self.driver.find_element(*self.Email_Already_exist_message).text
        return Message_one
    
    def Invalid_Email_Format(self):
        Message_two=self.driver.find_elements(*self.Validation_Messages)
        for message in Message_two:
            if (message.text)=="Email not valid.":
               return message.text 
    
    def Email_Required(self):
        Message_three=self.driver.find_elements(*self.Validation_Messages)
        for message in Message_three:
           if (message.text)=="Required field":
               return message.text
              
    def Invalid_password(self):
        Message_three=self.driver.find_elements(*self.Validation_Messages)
        for message in Message_three:
           if (message.text)=="Must have at least 3 characters":
               return message.text   

   

      

    #def captcha(self):
    
# Wait until the shadow host element is visible (assuming it's the div with ID 'cf-turnstile-widget')
      #shadow_host = WebDriverWait(self.driver, 10).until(
    #EC.presence_of_element_located((By.CSS_SELECTOR, '#cf-turnstile-widget'))
#)

# Use JavaScript to access the shadow root (closed shadow DOM) and get the shadow root
      #print(shadow_host)
      #shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)
      #print(shadow_root)





        #self.driver.switch_to.frame(self.driver.find_element(*self.iframe))
        #time.sleep(8)
        #self.driver.find_element(*self.checkbox).click()
        
        
    #def login(self, username01, password01):
        #self.username(username01)
        #self.password(password01)
        #self.driver.find_element(*self.Button).click()

    #def invalid_error(self):
        #return self.driver.find_element(*self.message).text
