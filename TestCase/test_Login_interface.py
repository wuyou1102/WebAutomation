# coding=utf-8
import re
import unittest
import Libs.CommonFunction as CF
from Libs.GlobalVariable import Web, Config
import requests
from ddt import data, ddt, file_data, unpack

case_parameters = Config.case_parameters.get('Login')



@ddt
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.session.headers = Web.headers

    def tearDown(self):
        self.session.close()

    @data(*case_parameters)
    def test_login(self, case_parameter):
        case_parameter = CF.print_dict(case_parameter)
        username = case_parameter.get('Username')
        password = case_parameter.get('Password')
        except_code = case_parameter.get('Code')
        except_content = case_parameter.get('Content')
        csrf_token = self.get_csrf_token()
        form_data = {
            '_csrf': csrf_token,
            'username': username,
            'pwd': password,
        }
        resp = self.session.post(url=Web.url_basic + Web.part_login, data=form_data)
        code, content = resp.status_code, resp.content
        self.assertEquals(except_code, code)
        self.assertEquals(except_content, content)


    def test_csrf_is_open(self):
        form_data = {
            '_csrf': "An_Invalid_CSRF_Value==",
            'username': 'admin',
            'pwd': 'Password01!'
        }
        resp = self.session.post(url=Web.url_basic + Web.part_login, data=form_data)
        code, content = resp.status_code, resp.content
        self.assertNotEquals(200, code)

    def get_csrf_token(self):
        resp = self.session.get(url=Web.url_basic + Web.part_index)
        return re.findall(Web.csrf_pattern, resp.content)[0]


if __name__ == '__main__':
    unittest.main()
