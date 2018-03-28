# coding=utf-8

import unittest
from Libs.GlobalVariable import tc_dir, default_html_path
from Libs import HTMLTestRunner

if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover(tc_dir, pattern='test_*_interface.py')
    stream = file(default_html_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=stream, title='SensePlay', verbosity=2)
    runner.run(discover)
    stream.close()
