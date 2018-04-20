import sys
from os.path import join, abspath, dirname
from time import strftime, localtime
import ParseConfig
import re

work_dir = abspath(dirname(sys.argv[0]))
work_dir = 'C:\Users\dell\PycharmProjects\WebAutomation'
log_dir = join(work_dir, 'Log')
report_dir = join(work_dir, 'Report')
tc_dir = join(work_dir, 'TestCase')
resource_dir = join(work_dir, 'Resource')

default_log_path = join(log_dir, '%s.log' % strftime("%Y-%m-%d_%H-%M-%S", localtime()))
default_html_path = join(report_dir, '%s.html' % strftime("%Y-%m-%d_%H-%M-%S", localtime()))
default_config_path = join(resource_dir, 'Config.xls')


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
    url_basic = 'http://dev.a.senseplay.com/system/web'
    part_index = '/index.php'
    part_login = '/index.php?r=user/login'
    part_welcome = '/index.php?r=common/welcome'
    account_oauth_url = "http://test.auth.senseplay.com/oauth/authorize?response_type=code&client_id=44E7F9DC2DE558BFBC5D808E38299999&state=developer&redirect_uri=http://test.account.senseplay.com/game/oauth"


class Config(object):
    case_parameters = ParseConfig.from_excel(default_config_path)
