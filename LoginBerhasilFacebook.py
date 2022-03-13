# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LoginBerhasilFacebook(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_berhasil_facebook(self):
        driver = self.driver
        driver.get("https://www.populix.co/login")
        driver.find_element_by_xpath("//button[@id='login_facebook']/span").click()
        driver.get("https://web.facebook.com/login/reauth.php?app_id=2250584668517054&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D2250584668517054%26redirect_uri%3Dhttps%253A%252F%252Fpopulix.auth.ap-southeast-1.amazoncognito.com%252Foauth2%252Fidpresponse%26scope%3Dpublic_profile%252Cemail%26response_type%3Dcode%26state%3DZXlKMWMyVnlVRzl2YkVsa0lqb2lZWEF0YzI5MWRHaGxZWE4wTFRGZk0zaFRXRlIwY25waUlpd2ljSEp2ZG1sa1pYSk9ZVzFsSWpvaVJtRmpaV0p2YjJzaUxDSmpiR2xsYm5SSlpDSTZJamR5Wkcxek5UbG9aWFJ5Wld0b1ltOWpiRzFqTWpjeloyRnBJaXdpY21Wa2FYSmxZM1JWVWtraU9pSm9kSFJ3Y3pvdkwzZDNkeTV3YjNCMWJHbDRMbU52TDNOMGRXUjVQMk5oYkd4aVlXTnJJaXdpY21WemNHOXVjMlZVZVhCbElqb2lkRzlyWlc0aUxDSndjbTkyYVdSbGNsUjVjR1VpT2lKR1lXTmxZbTl2YXlJc0luTmpiM0JsY3lJNld5SmhkM011WTI5bmJtbDBieTV6YVdkdWFXNHVkWE5sY2k1aFpHMXBiaUlzSW1WdFlXbHNJaXdpYjNCbGJtbGtJaXdpY0dodmJtVWlMQ0p3Y205bWFXeGxJbDBzSW5OMFlYUmxJam9pUW5aS1FXSnlWSGhyUTNCMFRqSXhZMk0xYWxwdU5VeFRSR2RTYkhGbWVUWWlMQ0pqYjJSbFEyaGhiR3hsYm1kbElqcHVkV3hzTENKamIyUmxRMmhoYkd4bGJtZGxUV1YwYUc5a0lqcHVkV3hzTENKdWIyNWpaU0k2SWtsVllWVkJTMjFKUkU5V2VTMUtYMlZuUlhsdFEyWkZaRUV3Wms5dVpsSkNSVWxXTFd0a2NXNHRiVUZ4WWpWQ2RXd3hTMlV4VVVOaVpWbEJiMmhLZUcxZk9GUlBORUZyTVd3MVlYSkNha3hYZDNobU1uRmpSMHBNVlcwM1VsTlRjVXBpZFdsUVRrUjFhV2QxV0U1aWExZHpTVEZKTmtGclRqRldkMjFXUldGQlFWSXRRalp1UVZRdFpFZFZVVWx5WVZNMk5HWnhNbEJPTjI1V05rcHhWMDVKVDBobmFVeENTWEY0U1NJc0luTmxjblpsY2todmMzUlFiM0owSWpvaWNHOXdkV3hwZUM1aGRYUm9MbUZ3TFhOdmRYUm9aV0Z6ZEMweExtRnRZWHB2Ym1OdloyNXBkRzh1WTI5dElpd2lZM0psWVhScGIyNVVhVzFsVTJWamIyNWtjeUk2TVRZME56RTFOakV4Tml3aWMyVnpjMmx2YmlJNmJuVnNiQ3dpZFhObGNrRjBkSEpwWW5WMFpYTWlPbTUxYkd3c0ltWmhZMlZpYjI5clZtVnljMmx2YmlJNkluWTFMakFpTENKemRHRjBaVVp2Y2t4cGJtdHBibWRUWlhOemFXOXVJanBtWVd4elpYMD06cTNZeUc3R0NXR2hrYmp1TGIxS3dIWlNnTEFtRFJ2QTNkRzU4eVRid09FYz06Mw%253D%253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D37999c05-317e-4519-affc-d6fe8eaea1ed%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fpopulix.auth.ap-southeast-1.amazoncognito.com%2Foauth2%2Fidpresponse%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DZXlKMWMyVnlVRzl2YkVsa0lqb2lZWEF0YzI5MWRHaGxZWE4wTFRGZk0zaFRXRlIwY25waUlpd2ljSEp2ZG1sa1pYSk9ZVzFsSWpvaVJtRmpaV0p2YjJzaUxDSmpiR2xsYm5SSlpDSTZJamR5Wkcxek5UbG9aWFJ5Wld0b1ltOWpiRzFqTWpjeloyRnBJaXdpY21Wa2FYSmxZM1JWVWtraU9pSm9kSFJ3Y3pvdkwzZDNkeTV3YjNCMWJHbDRMbU52TDNOMGRXUjVQMk5oYkd4aVlXTnJJaXdpY21WemNHOXVjMlZVZVhCbElqb2lkRzlyWlc0aUxDSndjbTkyYVdSbGNsUjVjR1VpT2lKR1lXTmxZbTl2YXlJc0luTmpiM0JsY3lJNld5SmhkM011WTI5bmJtbDBieTV6YVdkdWFXNHVkWE5sY2k1aFpHMXBiaUlzSW1WdFlXbHNJaXdpYjNCbGJtbGtJaXdpY0dodmJtVWlMQ0p3Y205bWFXeGxJbDBzSW5OMFlYUmxJam9pUW5aS1FXSnlWSGhyUTNCMFRqSXhZMk0xYWxwdU5VeFRSR2RTYkhGbWVUWWlMQ0pqYjJSbFEyaGhiR3hsYm1kbElqcHVkV3hzTENKamIyUmxRMmhoYkd4bGJtZGxUV1YwYUc5a0lqcHVkV3hzTENKdWIyNWpaU0k2SWtsVllWVkJTMjFKUkU5V2VTMUtYMlZuUlhsdFEyWkZaRUV3Wms5dVpsSkNSVWxXTFd0a2NXNHRiVUZ4WWpWQ2RXd3hTMlV4VVVOaVpWbEJiMmhLZUcxZk9GUlBORUZyTVd3MVlYSkNha3hYZDNobU1uRmpSMHBNVlcwM1VsTlRjVXBpZFdsUVRrUjFhV2QxV0U1aWExZHpTVEZKTmtGclRqRldkMjFXUldGQlFWSXRRalp1UVZRdFpFZFZVVWx5WVZNMk5HWnhNbEJPTjI1V05rcHhWMDVKVDBobmFVeENTWEY0U1NJc0luTmxjblpsY2todmMzUlFiM0owSWpvaWNHOXdkV3hwZUM1aGRYUm9MbUZ3TFhOdmRYUm9aV0Z6ZEMweExtRnRZWHB2Ym1OdloyNXBkRzh1WTI5dElpd2lZM0psWVhScGIyNVVhVzFsVTJWamIyNWtjeUk2TVRZME56RTFOakV4Tml3aWMyVnpjMmx2YmlJNmJuVnNiQ3dpZFhObGNrRjBkSEpwWW5WMFpYTWlPbTUxYkd3c0ltWmhZMlZpYjI5clZtVnljMmx2YmlJNkluWTFMakFpTENKemRHRjBaVVp2Y2t4cGJtdHBibWRUWlhOemFXOXVJanBtWVd4elpYMD06cTNZeUc3R0NXR2hrYmp1TGIxS3dIWlNnTEFtRFJ2QTNkRzU4eVRid09FYz06Mw%253D%253D%23_%3D_&display=page&locale=en_GB&pl_dbl=0&_rdc=1&_rdr")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
