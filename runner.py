import unittest
from HTMLTestRunner import HTMLTestRunner
from HTMLTestReportCN import HTMLTestRunner

from cases_unit.test_cases_unit import Test1Case
from send_email.send_email import sendEmail
from send_email.send_mail import send_mail


def runner():
    test_dir = './cases_unit'  # 当前用例路径
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')  # test*.py表示test开头的所有测试用例
    fp = open("./report.html", "wb")  # 报告存放的路径
    runner = HTMLTestRunner(stream=fp, title='自动化测试报告',
                            description='测试用例情况描述:', tester='刘旭')
    # 执行用例
    runner.run(discover)
    fp.close()
    # 发送html格式的测试报告邮件
    # sendEmail().send()
    send_mail("./report.html")

# 修改
if __name__ == '__main__':
    runner()
    # suite=unittest.TestSuite()
    # suite.addTest(Test1Case('test_1'))
    # runner=unittest.TextTestRunner()
    # runner.run(suite)
