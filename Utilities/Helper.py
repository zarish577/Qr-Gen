import random
import string
from Page.Login import QRlogin
import pytest
import configparser
config=configparser.ConfigParser()
config.read("Utilities/config.ini")
#--html=report.html

def generate_unique_emails():
    username=''.join(random.choices(string.ascii_lowercase+string.digits,k=8))
    return f"{username}@example.com"


def generate_complex_passwords(length=9):
    characters=string.ascii_letters+string.digits+string.punctuation
    random_password= ''.join(random.choices(characters,k=length))
    return random_password

def login1(driver):
       driver = QRlogin(driver)
       driver.login(config.get("credentials","user_name"),config.get("credentials","pass_word"))
   
