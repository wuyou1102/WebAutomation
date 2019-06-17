import sys
from os.path import abspath, dirname
import os
from time import strftime, localtime
import ParseConfig
import re


def join(path, *paths):
    path = os.path.join(path, *paths)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


work_dir = abspath(dirname(sys.argv[0]))
work_dir = 'D:\Profile\Desktop\WebAutomation'
log_dir = join(work_dir, 'Log')
report_dir = join(work_dir, 'Report')
tc_dir = join(work_dir, 'TestCase')
resource_dir = join(work_dir, 'Resource')

default_log_path = os.path.join(log_dir, '%s.log' % strftime("%Y-%m-%d_%H-%M-%S", localtime()))
default_html_path = os.path.join(report_dir, '%s.html' % strftime("%Y-%m-%d_%H-%M-%S", localtime()))
default_config_path = os.path.join(resource_dir, 'Config.xls')


class Web(object):
    headers = {'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Connection': 'keep-alive',
               'Referer': 'http://www.baidu.com/'
               }
    csrf_pattern = re.compile(r'<input name="_csrf" type="hidden" id="_csrf" value="(.*)">')
    access_token_pattern = re.compile(r'{"access_token":"(.*?)",')
    openid_pattern = re.compile(r',"openid":"(.*?)","uuid"')
    url_basic = 'http://a.senseplay.cn/system/web'
    part_index = '/index.php'
    part_login = '/index.php?r=user/login'
    part_welcome = '/index.php?r=common/welcome'
    account_oauth_url = "http://test.adminsso.senseplay.cn/oauth/authorize?response_type=code&client_id=523D3B1F64BE05AFD50DE46FCE34297A&state=senseplay_admin&redirect_uri=http://test.a.senseplay.cn/rbac/web/index.php?r=client/oauth&language=en"


class Config(object):
    case_parameters = ParseConfig.from_excel(default_config_path)
