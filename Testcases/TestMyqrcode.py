from Utilities.Helper import login1
from Page.MyQRcode import MyQRCode
import pytest
import time

@pytest.mark.fixture("driver")
class TestApp02:
    def test_myqrcode(self):
      login1(self.driver)
      time.sleep(5)
      myqrcode = MyQRCode(self.driver)
      myqrcode.link()

      input("Press Enter to close the browser...")