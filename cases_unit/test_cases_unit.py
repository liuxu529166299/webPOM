# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @File     :cases_unit
# @Date     :2020/11/10 20:23
# @Author   :刘旭
-------------------------------------------------
"""
import unittest
from page_object.login_page import LoginPage
from selenium import webdriver
from time import sleep
from chrome_options.options import Options

class Test1Case(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(options=Options().conf_option())
        self.driver.implicitly_wait(10)

    # 登录用例
    def test_login(self):
        lp = LoginPage(self.driver, LoginPage.url)
        self.assertTrue(lp.assert_text('liuxu', '111111'))

    def tearDown(self) -> None:
        sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
