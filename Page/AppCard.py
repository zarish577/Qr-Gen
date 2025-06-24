from selenium.webdriver.common.by import By
import time

class App():
    App_button= (By.CSS_SELECTOR,".flex.flex-col.mt-1")
    Xpath_toggle= (By.XPATH,"//span[contains(text(),'Autocomplete Fields')]")

    def __init__ (self,driver):
     self.driver=driver

    def Toggle_click(self):
     Buttons= self.driver.find_elements(*self.App_button)
     for btn in Buttons:
      print(btn.text)
     if btn.text=="Apps":
       btn.clicl
     #self.driver.find_element(*self.App_button).click()
     #time.sleep(5)
     #self.driver.find_element(*self.Xpath_toggle).click()