from Page.AppCard import App
from Utilities.Helper import login1
import pytest


@pytest.mark.usefixtures("driver")
class TestApp01:
    def testapp(self):
        login1(self.driver)
        app_page = App(self.driver)  # Don't overwrite self.driver
        app_page.Toggle_click()  # Method names should be lowercase
        input("Press Enter to close the browser...")