from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class MyQRCode:
 sidebutton= (By.XPATH,"//p[text()='My QR Code']")
 #ClickLink = (By.XPATH, "//a[contains(@href,'https://qr-gen.com/p/M9ZqOZF')]")
 classlink = (By.XPATH, "(//div[contains(@class, 'flex items-center gap-2 p-2 text-sm')])[1]")



 def __init__(self,driver):
   self.driver=driver

 def link(self):
   self.driver.find_element(*self.sidebutton).click()
   time.sleep(9)
   window= self.driver.current_window_handle

   cls= self.driver.find_element(*self.classlink)
   a= cls.find_element(By.TAG_NAME,'a')
   a.click()

   windows=self.driver.window_handles
   for win in windows:
     if(win!=window):
       self.driver.switch_to.window(win)
       self.driver.close()
       self.driver.switch_to.window(window)
       break
     
    
     
       
       