import sys
from os.path import join, abspath, dirname
from time import strftime, localtime
import ParseConfig
import re

work_dir = abspath(dirname(sys.argv[0]))
log_dir = join(work_dir, 'Log')
report_dir = join(work_dir, 'Report')
tc_dir = join(work_dir, 'TestCase')
resource_dir = join(work_dir, 'Resource')

default_log_path = join(log_dir, '%s.log' % strftime("%Y-%m-%d_%H-%M-%S", localtime()))
default_html_path = join(report_dir, '%s.html' % strftime("%Y-%m-%d_%H-%M-%S", localtime()))
default_config_path = join(resource_dir, 'Config.xls')


class Web(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/51.0.2704.103 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    csrf_pattern = re.compile(r'<input name="_csrf" type="hidden" id="_csrf" value="(.*)">')
    url_basic = 'http://dev.a.senseplay.com/system/web'
    part_index = '/index.php'
    part_login = '/index.php?r=user/login'
    part_welcome = '/index.php?r=common/welcome'


class Config(object):
    case_parameters = ParseConfig.from_excel(default_config_path)
