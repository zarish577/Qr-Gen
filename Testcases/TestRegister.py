from selenium.webdriver.chrome.webdriver import WebDriver
from Page.Login import Login_Page
from selenium.webdriver.common.by import By
import time
import pytest
import configparser
config=configparser.ConfigParser()
config.read("Utilities/config.ini")
from Utilities.Helper import generate_unique_emails,generate_complex_passwords

@pytest.mark.usefixtures("driver")
class Test_Login:   
    def setup_method(self):
        self.login_page = Login_Page(self.driver)
        self.email=generate_unique_emails()
        self.password=generate_complex_passwords()

    #Valid Login
    def test_login_with_valid_credentials_01(self):
     try:
        self.login_page.username(self.email)
        self.login_page.password(self.password)
        self.login_page.login()
        time.sleep(6)
        dashboard_title=self.driver.title
        assert "My QR codes" in dashboard_title
     except:
        self.driver.save_screenshot("Screenshots/failure_test_01.png")
        print("Test case fail")

    #Email Already exist 
    @pytest.mark.skip
    def test_already_exist_email_02(self):
     try:
        time.sleep(6)
        self.login_page.username(config.get("credentials","user_name"))
        self.login_page.password(self.password)
        self.login_page.login()
        time.sleep(3)
        Text= self.login_page.Email_Already_Exist_Message()
        print(Text)
        assert "The email is already registered" in Text
     except Exception as e:
        self.driver.save_screenshot("Screenshots/failure_test_02.png")
        print("Test case fail")
        raise e

    #Test with the invalid format of email
    @pytest.mark.skip
    def test_invalid_Email_03(self):
     try:
        self.login_page.username(config.get("credentials","Incorrect_Email"))
        self.login_page.password(self.password)
        Text_Two= self.login_page.Invalid_Email_Format()
        print(Text_Two)
        assert "Email not valid." in Text_Two
     except Exception as e:
        self.driver.save_screenshot("Screenshots/failure_test_03.png")
        print("Test case fail")
        raise e
    
    #Test with empty email
    @pytest.mark.skip
    def test_Empty_Email_04(self):
     try:
        self.login_page.password(self.password)
        self.login_page.username("")
        self.login_page.password(self.password)
        text=self.login_page.Email_Required()
        print(text)
        assert "Required field" in text
        Sign_up= self.login_page.disable_login_button()
        Sign_up is not None # Sign_up button should be disable
        time.sleep(6)
     except Exception as e:
        self.driver.save_screenshot("Screenshots/failure_test_04.png")
        print("Test case fail")
        raise e
    
    #password should be min 3 digits length having atleast one alphabet,number and special character, checking with 2 digits
    @pytest.mark.skip
    def test_invalid_password_limitation_05(self):
     try:
      self.login_page.username(self.email)
      self.login_page.password(config.get("credentials","incorrect_pass_word"))
      self.login_page.login()
      time.sleep(5)
      Validation_Message=self.login_page.Invalid_password()
      print(Validation_Message)
      assert "Must have at least 3 characters" in Validation_Message
     except Exception as e:
       self.driver.save_screenshot("Screenshots/failure_test_05.png")
       print("Test case fail")
       raise e

    
    #Test with three digit values of passwords[Boundary checking]
    @pytest.mark.skip
    def test_password_boundary_value_06(self):
     try:
        self.login_page.username(self.email)
        self.login_page.password(config.get("credentials","Three_digit_password"))
        self.login_page.login()
        time.sleep(6)
     except Exception as e:
          self.driver.save_screenshot("Screenshots/failure_test_06.png")
          print("Test case fail")
          raise e

     #Fail Test case
    @pytest.mark.skip
    def test_password_empty_password_07(self):
         try:
          self.login_page.username(self.email)
          self.login_page.login()
          time.sleep(6)
          text=self.login_page.Email_Required()
          print(text)
          assert "Required field" in text
         except Exception as e:
            self.driver.save_screenshot("Screenshots/failure_test_07.png")
            print("Test case fail")
            raise e
    @pytest.mark.skip    
    def test_invalid_email_password(self):
     try:
       self.login_page.username(config.get("credentials","Incorrect_Email"))
       self.login_page.password(config.get("credentials","incorrect_pass_word"))
       self.login_page.username(config.get("credentials","Incorrect_Email"))

       Text_Two= self.login_page.Invalid_Email_Format()
       print(Text_Two)
       assert "Email not valid." in Text_Two
       Validation_Message=self.login_page.Invalid_password()
       print(Validation_Message)
       assert "Must have at least 3 characters" in Validation_Message

     except Exception as e:
        self.driver.save_screenshot("Screenshots/failure_test_03.png")
        print("Test case fail")
        raise e
       




        





        




  
