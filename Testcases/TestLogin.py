from Page.Login import QRlogin
import pytest
import configparser
config=configparser.ConfigParser()
config.read("Utilities/config.ini")
@pytest.mark.usefixtures("driver")
class Test_login01():
      def test_login(self):
       self.driver = QRlogin(self.driver)
       self.driver.login(config.get("credentials","user_name"),config.get("credentials","pass_word"))
       #input("Press Enter to close the browser...") 