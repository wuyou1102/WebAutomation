# coding=utf-8
import re
import unittest
from selenium import webdriver
from Libs.GlobalVariable import Web
from time import sleep


class Test(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_login_success(self):
        self.browser.get(Web.url_basic)
        username = self.browser.find_element_by_id("username")
        password = self.browser.find_element_by_id("pwd1")
        username.send_keys("admin")
        password.send_keys("Password01!")
        btn = self.browser.find_element_by_class_name("login_b")
        btn.click()
        sleep(2)
        self.assertEquals(self.browser.current_url, Web.url_basic + Web.part_welcome)

    # def test_incorrect_password(self):
    #     csrf_token = self.get_csrf_token()
    #     form_data = {
    #         '_csrf': csrf_token,
    #         'username': 'admin',
    #         'pwd': 'Password02!'
    #     }
    #     resp = self.session.post(url=Web.url_basic + Web.part_login, data=form_data)
    #     code, content = resp.status_code, resp.content
    #     self.assertEquals(200, code)
    #     self.assertEquals('{"code":100220,"message":"LOGIN ERROR OR PWD ERRER","data":[]}', content)
    #     resp = self.session.get(url=Web.url_basic + Web.part_welcome)
    #     code, content = resp.status_code, resp.content
    #     self.assertEquals(302, code)
    #     # self.assertRegexpMatches(content, 'LOGIN OUT')
    #
    # def test_incorrect_username(self):
    #     csrf_token = self.get_csrf_token()
    #     form_data = {
    #         '_csrf': csrf_token,
    #         'username': 'username',
    #         'pwd': 'Password01!'
    #     }
    #     resp = self.session.post(url=Web.url_basic + Web.part_login, data=form_data)
    #     code, content = resp.status_code, resp.content
    #     self.assertEquals(200, code)
    #     self.assertEquals('{"code":100221,"message":"LOGIN ERROR OR PWD ERRER","data":[]}', content)
    #     resp = self.session.get(url=Web.url_basic + Web.part_welcome)
    #     code, content = resp.status_code, resp.content
    #     self.assertEquals(302, code)
    #
    # def test_csrf_is_open(self):
    #     #csrf_token = self.get_csrf_token()
    #     form_data = {
    #         '_csrf': "suibianshudianshenmeba",
    #         'username': 'admin',
    #         'pwd': 'Password01!'
    #     }
    #     resp = self.session.post(url=Web.url_basic + Web.part_login, data=form_data)
    #     code, content = resp.status_code, resp.content
    #     self.assertNotEquals(200, code)
    #
    #
    # def get_csrf_token(self):
    #     resp = self.session.get(url=Web.url_basic + Web.part_index)
    #     return re.findall(Web.csrf_pattern, resp.content)[0]


if __name__ == '__main__':
    unittest.main()
