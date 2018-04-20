# -*- encoding:UTF-8 -*-
import MySQLdb


class DataBase(object):
    def __init__(self, db, host="106.75.122.206", user="root", passwd="Aa123.321aA", charset='utf8'):
        self.__db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db,
                                    charset=charset)
        self.__cursor = self.__db.cursor()

    @property
    def date_base(self):
        return self.__db

    @property
    def cursor(self):
        return self.__cursor

    def query_game_info_log(self, log_id):
        cmd = 'SELECT `logid`, `openid`, `ts`, `RSN`, `DSN`, `mode`, `time`, `distance` FROM `gameinfo_log` WHERE `logid` = \'%s\'' % log_id
        self.__db.commit()
        self.__cursor.execute(cmd)
        return self.__cursor.fetchall()

    def close(self):
        self.__db.close()
