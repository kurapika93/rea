# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class LoginBerhasilGoogle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_berhasil_google(self):
        driver = self.driver
        driver.get("https://www.populix.co/login")
        driver.find_element_by_xpath("//button[@id='login_google']/span").click()
        driver.get("https://accounts.google.com/o/oauth2/v2/auth?client_id=53702542894-tq5aa12g8bmpj0gnnkeffrg3ul8i2pn6.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fpopulix.auth.ap-southeast-1.amazoncognito.com%2Foauth2%2Fidpresponse&scope=profile+email+openid&response_type=code&state=ZXlKMWMyVnlVRzl2YkVsa0lqb2lZWEF0YzI5MWRHaGxZWE4wTFRGZk0zaFRXRlIwY25waUlpd2ljSEp2ZG1sa1pYSk9ZVzFsSWpvaVIyOXZaMnhsSWl3aVkyeHBaVzUwU1dRaU9pSTNjbVJ0Y3pVNWFHVjBjbVZyYUdKdlkyeHRZekkzTTJkaGFTSXNJbkpsWkdseVpXTjBWVkpKSWpvaWFIUjBjSE02THk5M2QzY3VjRzl3ZFd4cGVDNWpieTl6ZEhWa2VUOWpZV3hzWW1GamF5SXNJbkpsYzNCdmJuTmxWSGx3WlNJNkluUnZhMlZ1SWl3aWNISnZkbWxrWlhKVWVYQmxJam9pUjI5dloyeGxJaXdpYzJOdmNHVnpJanBiSW1GM2N5NWpiMmR1YVhSdkxuTnBaMjVwYmk1MWMyVnlMbUZrYldsdUlpd2laVzFoYVd3aUxDSnZjR1Z1YVdRaUxDSndhRzl1WlNJc0luQnliMlpwYkdVaVhTd2ljM1JoZEdVaU9pSmxiVWRhVm1sNFZrWmlkM0Y0YzIweU5GSjNOVkZEU0ZSeU5XWk5kbUp4UlNJc0ltTnZaR1ZEYUdGc2JHVnVaMlVpT201MWJHd3NJbU52WkdWRGFHRnNiR1Z1WjJWTlpYUm9iMlFpT201MWJHd3NJbTV2Ym1ObElqb2lNR05DYzBsQlJHeFFSSFJwZGtoMWVUUmFXR3hwT1hGUUxYTlBRemRGTW5WRmJWQlJjMUJuYW1wU2VHNUVZV0ZyWlZKd1RFTk1ZM0F0WlhGbVNHdDBjMnBuV0Y5VllXRk5RbVZOWVhjelR6Qm1WRVo2T0cwdFNsTmlTelJuYW0xbGNYQk9PRTUyVURGRlVFOTVZVU5ETUc5RVVXaEVXblpOUldSM1UyWldPV0UwWDJoUlZrOVZPVVJyY25OQlgwcFRjVmRMZEVKVE5saFFkMFZOZDJ4NFJtMHpNalZsV2pneU5VZFZJaXdpYzJWeWRtVnlTRzl6ZEZCdmNuUWlPaUp3YjNCMWJHbDRMbUYxZEdndVlYQXRjMjkxZEdobFlYTjBMVEV1WVcxaGVtOXVZMjluYm1sMGJ5NWpiMjBpTENKamNtVmhkR2x2YmxScGJXVlRaV052Ym1Seklqb3hOalEzTVRVMk16TXpMQ0p6WlhOemFXOXVJanB1ZFd4c0xDSjFjMlZ5UVhSMGNtbGlkWFJsY3lJNmJuVnNiQ3dpYzNSaGRHVkdiM0pNYVc1cmFXNW5VMlZ6YzJsdmJpSTZabUZzYzJWOTptZkZ4SEVoTUVDeFZsMzZwSTF1ZnN6eWtXRERUcTV5YVdzTUJHRGlxQ1VrPToz")
        driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?client_id=53702542894-tq5aa12g8bmpj0gnnkeffrg3ul8i2pn6.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Fpopulix.auth.ap-southeast-1.amazoncognito.com%2Foauth2%2Fidpresponse&scope=profile%20email%20openid&response_type=code&state=ZXlKMWMyVnlVRzl2YkVsa0lqb2lZWEF0YzI5MWRHaGxZWE4wTFRGZk0zaFRXRlIwY25waUlpd2ljSEp2ZG1sa1pYSk9ZVzFsSWpvaVIyOXZaMnhsSWl3aVkyeHBaVzUwU1dRaU9pSTNjbVJ0Y3pVNWFHVjBjbVZyYUdKdlkyeHRZekkzTTJkaGFTSXNJbkpsWkdseVpXTjBWVkpKSWpvaWFIUjBjSE02THk5M2QzY3VjRzl3ZFd4cGVDNWpieTl6ZEhWa2VUOWpZV3hzWW1GamF5SXNJbkpsYzNCdmJuTmxWSGx3WlNJNkluUnZhMlZ1SWl3aWNISnZkbWxrWlhKVWVYQmxJam9pUjI5dloyeGxJaXdpYzJOdmNHVnpJanBiSW1GM2N5NWpiMmR1YVhSdkxuTnBaMjVwYmk1MWMyVnlMbUZrYldsdUlpd2laVzFoYVd3aUxDSnZjR1Z1YVdRaUxDSndhRzl1WlNJc0luQnliMlpwYkdVaVhTd2ljM1JoZEdVaU9pSmxiVWRhVm1sNFZrWmlkM0Y0YzIweU5GSjNOVkZEU0ZSeU5XWk5kbUp4UlNJc0ltTnZaR1ZEYUdGc2JHVnVaMlVpT201MWJHd3NJbU52WkdWRGFHRnNiR1Z1WjJWTlpYUm9iMlFpT201MWJHd3NJbTV2Ym1ObElqb2lNR05DYzBsQlJHeFFSSFJwZGtoMWVUUmFXR3hwT1hGUUxYTlBRemRGTW5WRmJWQlJjMUJuYW1wU2VHNUVZV0ZyWlZKd1RFTk1ZM0F0WlhGbVNHdDBjMnBuV0Y5VllXRk5RbVZOWVhjelR6Qm1WRVo2T0cwdFNsTmlTelJuYW0xbGNYQk9PRTUyVURGRlVFOTVZVU5ETUc5RVVXaEVXblpOUldSM1UyWldPV0UwWDJoUlZrOVZPVVJyY25OQlgwcFRjVmRMZEVKVE5saFFkMFZOZDJ4NFJtMHpNalZsV2pneU5VZFZJaXdpYzJWeWRtVnlTRzl6ZEZCdmNuUWlPaUp3YjNCMWJHbDRMbUYxZEdndVlYQXRjMjkxZEdobFlYTjBMVEV1WVcxaGVtOXVZMjluYm1sMGJ5NWpiMjBpTENKamNtVmhkR2x2YmxScGJXVlRaV052Ym1Seklqb3hOalEzTVRVMk16TXpMQ0p6WlhOemFXOXVJanB1ZFd4c0xDSjFjMlZ5UVhSMGNtbGlkWFJsY3lJNmJuVnNiQ3dpYzNSaGRHVkdiM0pNYVc1cmFXNW5VMlZ6YzJsdmJpSTZabUZzYzJWOTptZkZ4SEVoTUVDeFZsMzZwSTF1ZnN6eWtXRERUcTV5YVdzTUJHRGlxQ1VrPToz&flowName=GeneralOAuthFlow")
        driver.find_element_by_xpath("//div[@id='view_container']/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/ul/li[2]/div/div/div/div[2]/div[2]").click()
        driver.get("https://www.populix.co/study?callback#access_token=eyJraWQiOiJwTk4rZlNLSWlkaXUzb3NDd1Qwejg3cHhIK3dFWnhnMlNyTzZySng1RGtZPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIyNGI2ODA5My04MmZiLTQyYjctYmViOC1hYWEzOTY1MTE0MjAiLCJjb2duaXRvOmdyb3VwcyI6WyJhcC1zb3V0aGVhc3QtMV8zeFNYVHRyemJfR29vZ2xlIl0sInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4gcGhvbmUgb3BlbmlkIHByb2ZpbGUgZW1haWwiLCJhdXRoX3RpbWUiOjE2NDcxNTYzNjUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMS5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMV8zeFNYVHRyemIiLCJleHAiOjE2NDcxNTk5NjUsImlhdCI6MTY0NzE1NjM2NSwidmVyc2lvbiI6MiwianRpIjoiMzhhMWFiMGItNjFjNi00NzBlLWE1OWYtZDQyYzk2MWRiZjk5IiwiY2xpZW50X2lkIjoiN3JkbXM1OWhldHJla2hib2NsbWMyNzNnYWkiLCJ1c2VybmFtZSI6Ikdvb2dsZV8xMDk1MjAyMzExNjY3MTg5OTA1NDIifQ.R2PMqtIi_OR6XyySye2xNze_k298tRs3dNiDc3L9XBTHUpuXOcwzh1XmJAV-NMi2-M6VE2dMsZgtXxj6DwTfgeuBgXIQ-748O8XR32ywT_JoqAd4lQ8DDFo91GJaLdGsRcZ1hfNX4M_NUuZQKJrg2kHJli7ng-nsTJ49YwIvPCq_litC1Okz6X3bPQCdFyIETfu_ALebdbsftRNIeqTLvRXEKdV9uXWr0f_pn1bHMomSan5ybqo-tVTiNhUrPTqHsM5ErPfGup4MrsYx4_y4z4lZAmjvHqlEcB3KfSsP7tnemM3-gYONka8BRgDjcx1WP1VfSTvvvQYlHzAJsAD5Jw&id_token=eyJraWQiOiJDOXZJMGMwRktDZnIxdmtkVCt1dGpcL2JNTTMzUlUyMTZiTithWGxRazNhZz0iLCJhbGciOiJSUzI1NiJ9.eyJhdF9oYXNoIjoiU0EwVXU1eVc1dHJOeXhoeXEtWHFWZyIsInN1YiI6IjI0YjY4MDkzLTgyZmItNDJiNy1iZWI4LWFhYTM5NjUxMTQyMCIsImNvZ25pdG86Z3JvdXBzIjpbImFwLXNvdXRoZWFzdC0xXzN4U1hUdHJ6Yl9Hb29nbGUiXSwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtc291dGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtc291dGhlYXN0LTFfM3hTWFR0cnpiIiwiY29nbml0bzp1c2VybmFtZSI6Ikdvb2dsZV8xMDk1MjAyMzExNjY3MTg5OTA1NDIiLCJub25jZSI6IjBjQnNJQURsUER0aXZIdXk0WlhsaTlxUC1zT0M3RTJ1RW1QUXNQZ2pqUnhuRGFha2VScExDTGNwLWVxZkhrdHNqZ1hfVWFhTUJlTWF3M08wZlRGejhtLUpTYks0Z2ptZXFwTjhOdlAxRVBPeWFDQzBvRFFoRFp2TUVkd1NmVjlhNF9oUVZPVTlEa3JzQV9KU3FXS3RCUzZYUHdFTXdseEZtMzI1ZVo4MjVHVSIsImF1ZCI6IjdyZG1zNTloZXRyZWtoYm9jbG1jMjczZ2FpIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiMTA5NTIwMjMxMTY2NzE4OTkwNTQyIiwicHJvdmlkZXJOYW1lIjoiR29vZ2xlIiwicHJvdmlkZXJUeXBlIjoiR29vZ2xlIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoidHJ1ZSIsImRhdGVDcmVhdGVkIjoiMTY0NzE1NjM2NTE2MyJ9XSwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE2NDcxNTYzNjUsIm5hbWUiOiJBdW5pIEZhZGlsYWgiLCJleHAiOjE2NDcxNTk5NjUsImlhdCI6MTY0NzE1NjM2NSwiZmFtaWx5X25hbWUiOiJGYWRpbGFoIiwiZW1haWwiOiJmYWRpbGFoYXVuaUBnbWFpbC5jb20ifQ.TQxnh0CzRCVLDX72zEo9aaFbgpnJCFkdgBvvn5NihadAieFfxHy9AkWRkw5dJrA7XkrLAdX2vUOxPCcg8yxMEgGDPY4CWLHhfs5XLRPa0dZCeT-x-FG8yoqwdRBZhx1WSz_XFh_ndpHnQoPU916I1BK8eZsGLvcIMRMzAVpSxAMU5g555oRuz1s29XJfqGtvUL2u5G-Go_MmFch1vfQBI3XJqzCdWhqAEl6PQAUTHhugS3BT9DGE63PrNH9N6j3bu3CIyfFYR4rYl3h707oTo5QHvhHZhwvXUUwK0UomA2BrI2V-Mbb2-UpjOmFNXUGULSGJ86xNBciwfOjZhC8yYg&state=emGZVixVFbwqxsm24Rw5QCHTr5fMvbqE&token_type=Bearer&expires_in=3600")
    
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
