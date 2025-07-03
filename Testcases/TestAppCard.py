from Page.AppCard import App
from Utilities.Helper import login1
import pytest
import time


@pytest.mark.usefixtures("driver")
class TestApp01:
    def testapp(self):
        login1(self.driver)
        time.sleep(5)
        
        app_page = App(self.driver) 
        app_page.Test_App()
        app_page.Test_Manual_Form()

        input("Press Enter to close the browser...")