from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class App():
    App_button= (By.XPATH,"//h3[text()='Apps']")
    Xpath_toggle= (By.XPATH,"//span[contains(text(),'Autocomplete Fields')]")
    Appearance= (By.XPATH,"//h3[text()='Appearance']")
    Template= (By.XPATH,"//h3[text()='Select template']")
    Template4=(By.XPATH,"//div[text()='Template 4']")
    Background = (By.XPATH, "(//div[normalize-space(@class)='w-6 h-6 rounded cursor-pointer transition-transform hover:scale-110'])[1]")
    Background_color= (By.XPATH, "//button[contains(@class,'w-6 h-6 rounded-md border')][1]")
    Foreground=(By.CSS_SELECTOR,".w-6.h-6.rounded.cursor-pointer")
    Foreground_Color=(By.CSS_SELECTOR,".w-6.h-6.rounded-md")
    Language_font=(By.CSS_SELECTOR, ".-ml-15")
    #Language_type= (By.CSS_SELECTOR, "div.flex.items-center.gap-2.cursor-pointer")
    Language_type= (By.XPATH,"//div[text()='Arial']")
    #Color_Template=(By.CSS_SELECTOR,".ring-2.ring-\\[#00FFB2\\]")
    Appname= (By.CSS_SELECTOR,"input[name='Appname']")
    AppDeveloperCompany = (By.CSS_SELECTOR,"input[name='AppDeveloperCompany']") 
    Appdescription=(By.CSS_SELECTOR,"textarea[name='Appdescription']")
    Appwebsite= (By.CSS_SELECTOR,"input[name='Appwebsite']")
    Amazon_Store= (By.XPATH,"//button[text()='Amazon Store']")
    appsAmazonStoreLink= (By.CSS_SELECTOR, "input[name='appsAmazonStoreLink']")
    #image= (By.CSS_SELECTOR,".relative")
    image = (By.CSS_SELECTOR, "input[name='Applogo']")
    next= (By.XPATH,"//p[text()='Next']")
    complete= (By.XPATH,"//p[text()='Complete']")
    

    def __init__ (self,driver):
     self.driver=driver


    def Test_App(self):
     self.ActionsChain = ActionChains(self.driver)
     Button= self.driver.find_element(*self.App_button)
     
     self.ActionsChain.move_to_element(Button).perform()
     Button.click()
     time.sleep(5)

    def Test_Manual_Form(self):
     self.driver.find_element(*self.Xpath_toggle).click()
     self.driver.find_element(*self.Appearance).click()
     self.driver.find_element(*self.Template).click()
     time.sleep(8)
     self.driver.find_element(*self.Template4).click()
     time.sleep(4)
     self.driver.execute_script("window.scrollBy(0,400);")

     self.driver.find_element(*self.Background).click()
     self.driver.find_element(*self.Background_color).click()

     Foreground= self.driver.find_elements(*self.Foreground)
     Foreground[1].click()
     Fcolor= self.driver.find_elements(*self.Foreground_Color)
     Fcolor[2].click()
     
     self.driver.execute_script("window.scrollBy(0,200);")
     ele=self.driver.find_elements(*self.Language_font)
     ele[0].click()
     self.driver.find_element(*self.Language_type).click()

     ele=self.driver.find_elements(*self.Language_font)
     ele[1].click()
     self.driver.find_element(*self.Language_type).click()

     self.driver.find_element(*self.Appname).send_keys("hello")
     self.driver.find_element(*self.AppDeveloperCompany).send_keys("hello")
     img = self.driver.find_element(*self.image)
     img.send_keys("C:/Users/usman/OneDrive/Pictures/error.png")
     time.sleep(7)
     self.driver.find_element(*self.Appdescription).send_keys("hello9")
     self.driver.find_element(*self.Appwebsite).send_keys("https://www.google.com")
     self.driver.find_element(*self.Amazon_Store).click()
     self.driver.find_element(*self.appsAmazonStoreLink).send_keys("https://www.google.com")
     self.driver.find_element(*self.next).click()
     time.sleep(6)
     self.driver.find_element(*self.complete).click()

     #for image_element in img_elements:
        #try:
            #img = image_element.find_element(By.TAG_NAME, "img")
            #src = img.get_attribute("src")
            #if (src=='data:image/webp;base64,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'):
             #img.click()
             #img.send_keys("C:/Users/usman/OneDrive/Pictures/error.png")
        #except:
            #print("Image not available")
      
     

   



     
