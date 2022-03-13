# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestDaftarInput(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_daftar_input(self):
        driver = self.driver
        driver.get("https://www.populix.co/login")
        driver.find_element_by_id("btn_to-register").click()
        driver.get("https://www.populix.co/register")
        driver.find_element_by_name("firstName").click()
        driver.find_element_by_name("firstName").clear()
        driver.find_element_by_name("firstName").send_keys("test")
        driver.find_element_by_name("lastName").clear()
        driver.find_element_by_name("lastName").send_keys("aaaaa")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("aaa@yahoo.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("111222333444")
        driver.find_element_by_xpath("//button[@id='submit_login']/span").click()
        driver.get("https://www.populix.co/confirm")
        driver.find_element_by_xpath("//input[@value='1']").clear()
        driver.find_element_by_xpath("//input[@value='1']").send_keys("1")
        driver.find_element_by_xpath("//div[@id='root']/div/div/div/div[2]/div/div/div/div/form/div/div/div[2]/input").clear()
        driver.find_element_by_xpath("//div[@id='root']/div/div/div/div[2]/div/div/div/div/form/div/div/div[2]/input").send_keys("1")
        driver.find_element_by_xpath("//div[@id='root']/div/div/div/div[2]/div/div/div/div/form/div/div/div[3]/input").clear()
        driver.find_element_by_xpath("//div[@id='root']/div/div/div/div[2]/div/div/div/div/form/div/div/div[3]/input").send_keys("1")
        driver.find_element_by_xpath("//div[@id='root']/div/div/div/div[2]/div/div/div/div/form/div/div/div[4]/input").clear()
        driver.find_element_by_xpath("//div[@id='root']/div/div/div/div[2]/div/div/div/div/form/div/div/div[4]/input").send_keys("1")
        driver.find_element_by_xpath("//div[@id='root']/div/div/div/div[2]/div/div/div/div/form/div/div/div[5]/input").clear()
        driver.find_element_by_xpath("//div[@id='root']/div/div/div/div[2]/div/div/div/div/form/div/div/div[5]/input").send_keys("1")
        driver.find_element_by_xpath("//div[@id='root']/div/div/div/div[2]/div/div/div/div/form/div/div/div[6]/input").clear()
        driver.find_element_by_xpath("//div[@id='root']/div/div/div/div[2]/div/div/div/div/form/div/div/div[6]/input").send_keys("1")
        driver.find_element_by_xpath("//button[@id='btn_submit']/span").click()
        driver.get("https://accounts.google.com/o/oauth2/v2/auth/identifier?client_id=53702542894-tq5aa12g8bmpj0gnnkeffrg3ul8i2pn6.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fpopulix.auth.ap-southeast-1.amazoncognito.com%2Foauth2%2Fidpresponse&scope=profile%20email%20openid&response_type=code&state=ZXlKMWMyVnlVRzl2YkVsa0lqb2lZWEF0YzI5MWRHaGxZWE4wTFRGZk0zaFRXRlIwY25waUlpd2ljSEp2ZG1sa1pYSk9ZVzFsSWpvaVIyOXZaMnhsSWl3aVkyeHBaVzUwU1dRaU9pSTNjbVJ0Y3pVNWFHVjBjbVZyYUdKdlkyeHRZekkzTTJkaGFTSXNJbkpsWkdseVpXTjBWVkpKSWpvaWFIUjBjSE02THk5M2QzY3VjRzl3ZFd4cGVDNWpieTl6ZEhWa2VUOWpZV3hzWW1GamF5SXNJbkpsYzNCdmJuTmxWSGx3WlNJNkluUnZhMlZ1SWl3aWNISnZkbWxrWlhKVWVYQmxJam9pUjI5dloyeGxJaXdpYzJOdmNHVnpJanBiSW1GM2N5NWpiMmR1YVhSdkxuTnBaMjVwYmk1MWMyVnlMbUZrYldsdUlpd2laVzFoYVd3aUxDSnZjR1Z1YVdRaUxDSndhRzl1WlNJc0luQnliMlpwYkdVaVhTd2ljM1JoZEdVaU9pSnhiVGMyWnpsalpGcHpZV3QzV21sbGRqaFFVRzV4Y0U5RVlYcHhaMVZwZENJc0ltTnZaR1ZEYUdGc2JHVnVaMlVpT201MWJHd3NJbU52WkdWRGFHRnNiR1Z1WjJWTlpYUm9iMlFpT201MWJHd3NJbTV2Ym1ObElqb2lVV0ozTTNkTGVtbzJSREZtVDJoMlRuUmZYeTF0VmpCQ1ZXcHRXRU5YYVhGcVh6WmhUMmRNWW1zNWVtMTRkRmhuUjB0MlEzVllTV2xzUTNacVREUmxXVUZ4TTFCVlJsTmhTMGhLVHpCbk9VeDBia05CY1RaUWMxWmlYMm95UTNoeFpETjFSMWRpU21kWFNGcGpabEpGZEZKc1pFbFFkRUZ4WlVaRFVsQTRXbFJSZUVVNE5uQlRORll5YzFoRWVFcHZkV1l5YXpreVdrOUhUbVZrTm5wcFUyZDNhbXg2YVc1eU1tUkZJaXdpYzJWeWRtVnlTRzl6ZEZCdmNuUWlPaUp3YjNCMWJHbDRMbUYxZEdndVlYQXRjMjkxZEdobFlYTjBMVEV1WVcxaGVtOXVZMjluYm1sMGJ5NWpiMjBpTENKamNtVmhkR2x2YmxScGJXVlRaV052Ym1Seklqb3hOalEzTVRVNU5qWXhMQ0p6WlhOemFXOXVJanB1ZFd4c0xDSjFjMlZ5UVhSMGNtbGlkWFJsY3lJNmJuVnNiQ3dpYzNSaGRHVkdiM0pNYVc1cmFXNW5VMlZ6YzJsdmJpSTZabUZzYzJWOTpncHY5QmZHUktnOVN4enExNEZWbVRuM1Uxei96KzI3ZkhpNUVMVGU0ZVRjPToz&flowName=GeneralOAuthFlow")
        driver.find_element_by_xpath("//body[@id='yDmH0d']/div/div[2]").click()
    
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
