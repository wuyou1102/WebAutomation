# coding=utf-8
import re
import unittest
import Libs.CommonFunction as CF
from Libs.GlobalVariable import Web
from Libs.GlobalVariable import Config
import requests
from ddt import data, ddt
from Libs.DataBase import DataBase
from time import sleep
import time

case_parameters = Config.case_parameters.get('H5_GameInfo')


@ddt
class H5_GameInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DataBase(db="racing_log")

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    def setUp(self):
        self.session = requests.Session()
        self.session.headers = Web.headers

    def tearDown(self):
        self.session.close()

    @data(*case_parameters)
    def test_log_gameinfo(self, case_parameters):
        CF.print_dict(case_parameters)
        if case_parameters.get("Skip"):
            print 'Skipped By Config.'
            return True
        access_from_web, access_from_config = self.__get_access_token_and_openid(case_parameters)
        timestamp = self.__get_timestamp(case_parameters)
        logid = self.__get_attr(case_parameters, "LogId")
        RSN = self.__get_attr(case_parameters, "RSN")
        DSN = self.__get_attr(case_parameters, "DSN")
        mode = self.__get_attr(case_parameters, "Mode")
        client_id = self.__get_attr(case_parameters, "ClientId")
        spend_time = self.__get_spend_time(case_parameters)
        distance = self.__get_distance(case_parameters)
        except_exist = self.__get_attr(case_parameters, "ExceptExist")

        list_log, string_data = self.__get_convert_data(logid=logid, openid=access_from_config[1], ts=timestamp,
                                                        RSN=RSN, DSN=DSN,
                                                        mode=mode, time=spend_time, distance=distance)

        form_data = {
            "client_id": client_id,
            'token': access_from_config[0],
            "data": string_data
        }
        resp = self.session.post(url="http://test.h5.racing.senseplay.com/api/log", data=form_data)
        self.assertEquals(case_parameters.get('ExceptResponse'), resp.content)
        sleep(1)
        self.assertTrue(self.__judege_result(except_exist, list_log))

    def __judege_result(self, except_exist, list_log):
        for log in list_log:
            db_logs = self.db.query_game_info_log(log[0])
            print "Excel data:%s " % str(db_logs)
            print "Data  base:%s " % str(log)
            if len(db_logs) > 1:
                print "Query in data base:"
                for db_log in db_logs:
                    print db_log
                return False
            elif len(db_logs) == 0:
                if except_exist:
                    print "I expect %s ,but I find no data in data base."
                    return False
            else:
                if db_logs[0] == log:
                    if not except_exist:
                        return False
                else:
                    if except_exist:
                        return False
        return True

    def __get_convert_data(self, logid, openid, ts, RSN, DSN, mode, time, distance):
        # 'SELECT `logid`, `openid`, `ts`, `RSN`, `DSN`, `mode`, `time`, `distace` FROM `gameinfo_log` WHERE `logid` = \'%s\'' % log_id)
        list_log = list()
        list_data = list()
        for d in distance:
            log_id = CF.generate_random_string(length=32,
                                               random_range=CF.hexdigits) if logid.upper() == "AUTO" else logid
            tuple_tmp = (log_id, openid, ts, RSN, DSN, mode, time, d)
            string_tmp = '{"logid":"%s",' \
                         '"ts":"%s",' \
                         '"uid":"%s",' \
                         '"act":"gameinfo",' \
                         '"data":' \
                         '{' \
                         '"RSN":"%s",' \
                         '"DSN":"%s","' \
                         'mode":"%s",' \
                         '"time":"%s",' \
                         '"distance":"%s"' \
                         '}' \
                         '}' % (log_id,
                                ts,
                                openid,
                                RSN,
                                DSN,
                                mode,
                                time,
                                d
                                )

            list_data.append(string_tmp)
            list_log.append(tuple_tmp)
        return list_log, '\n'.join(list_data)

    def __get_access_token_and_openid(self, parameters):
        form_data = {
            'authorized': "yes",
            'username': parameters.get('Username'),
            'pwd': parameters.get('Password')
        }
        for x in range(5):
            try:
                resp = self.session.post(url=Web.account_oauth_url, data=form_data)
                web_access_token = re.findall(Web.access_token_pattern, resp.content)[0]
                web_openid = re.findall(Web.openid_pattern, resp.content)[0]
                break
            except IndexError:
                pass

        config_access_token = parameters.get('Token')
        config_openid = parameters.get('OpenId')
        config_access_token = web_access_token if config_access_token.upper() == "AUTO" else config_access_token
        config_openid = web_openid if config_openid.upper() == "AUTO" else config_openid
        return (web_access_token, web_openid), (config_access_token, config_openid)

    def __get_timestamp(self, parameters):
        ts = parameters.get('TS')
        if ts.upper() == "AUTO":
            return int(time.time())
        try:
            return int(time.time() + int(ts))
        except ValueError:
            return ts

    def __get_attr(self, parameters, name):
        return parameters.get(name)

    def __get_spend_time(self, parameters):
        st = parameters.get('Time')
        if st.upper() == "AUTO":
            return '60'
        return st

    def __get_distance(self, parameters):
        distance = parameters.get('Distance')
        if ',' in distance:
            return distance.split(',')
        return [distance]

    def __get_display(self, parameters):
        display = parameters.get('Display')
        display_items = display.split('\n')
        return display_items


if __name__ == '__main__':
    unittest.main()
