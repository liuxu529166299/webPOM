# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @File     :login_page
# @Date     :2020/11/10 19:27
# @Author   :刘旭
-------------------------------------------------
"""
from base_page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from logger.logger import LoggerInfo

class LoginPage(BasePage):
    '''
        1.指定url
        2.输入账号
        3.输入密码
        4.点击登录
    '''

    # 元素定位
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    login = (By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/a[1]')
    us = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[1]/input')
    pwd = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[2]/input')
    login_button = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')
    # 断言元素
    asst = (By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/a')

    # 进入登录页
    def get_login(self):
        self.find_el(self.login)

    # 输入账号
    def send_us(self, text):
        self.find_el(self.us).send_keys(text)

    # 输入密码
    def send_pwd(self, text):
        self.find_el(self.pwd).send_keys(text)

    # 点击登录
    def login_click(self):
        self.find_el(self.login_button).click()

    # 登录流程
    def test_login(self, us, pwd):
        self.get()
        # self.get_login()
        self.send_us(us)
        self.send_pwd(pwd)
        self.login_click()
        LoggerInfo().get_logger().info('帐号登录中......帐号:{}密码{}'.format(us,pwd))

    # 断言函数：设置成功返回true，失败返回false
    def assert_text(self, us, pwd):
        self.test_login(us, pwd)
        text = self.find_el(self.asst).text
        if text == '退出':
            LoggerInfo().get_logger().info('登录断言中......返回状态：{}'.format(True))
            return True
        else:
            LoggerInfo().get_logger().info('登录断言中......返回状态：{}'.format(False))
            return False


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    lg = LoginPage(driver, LoginPage.url)
    print(lg.assert_text('liuxu', '111111'))
