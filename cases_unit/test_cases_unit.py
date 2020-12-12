# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @File     :test_cases_unit
# @Date     :2020/11/10 20:23
# @Author   :刘旭
-------------------------------------------------
"""
import unittest

import ddt
from page_object.login_page import LoginPage
from selenium import webdriver
from time import sleep
from chrome_options.options import Options
import yaml


@ddt.ddt()
class Test1Case(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(options=Options().conf_option())
        self.driver.implicitly_wait(10)

    # 登录用例
    def test_login(self):
        lp = LoginPage(self.driver, LoginPage.url)
        self.assertTrue(lp.assert_text('liuxu', '111111'))

    @ddt.file_data(r'./data/data.yaml')
    def test_1(self, **data):
        # file = open('./data/data.yaml','r')
        # data = yaml.load(file, Loader=yaml.FullLoader)
        print(data['name'], data['pwd'])
        self.assertEqual(1, 2)

    def test_2(self):
        file = open('./data/data.yaml', 'r')
        data = yaml.load(file, Loader=yaml.FullLoader)
        for i in data:
            print(i['name'], i['pwd'])
        self.assertEqual(1, 2)

    def tearDown(self) -> None:
        sleep(2)
        self.driver.quit()
