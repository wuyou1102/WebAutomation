import unittest
from Libs.GlobalVariable import tc_dir, default_html_path
from Libs import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf8')
if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover(tc_dir, pattern='test*.py')
    stream = file(default_html_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=stream, title='SensePlay', verbosity=2)
    runner.run(discover)
    stream.close()
