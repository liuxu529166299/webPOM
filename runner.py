import unittest
from HTMLTestRunner import HTMLTestRunner
from send_email.send_email import sendEmail


def runner():
    test_dir = './cases_unit'  # 当前用例路径
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')  # test*.py表示test开头的所有测试用例
    fp = open("./report.html", "wb")  # 报告存放的路径
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试用例情况:')
    # 执行用例
    runner.run(discover)
    fp.close()
    # 发送html格式的测试报告邮件
    sendEmail().send()


if __name__ == '__main__':
    runner()
