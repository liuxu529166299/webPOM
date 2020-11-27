# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @File     :base_page
# @Date     :2020/11/10 19:00
# @Author   :刘旭
-------------------------------------------------
"""
from logger.logger import LoggerInfo


# 定义基类：提供各个PO对象来调用的公共类方法
class BasePage:
    # 定义构造函数：所有内容都是基于driver操作，所以要传递driver
    # 定义构造函数：每一个页面都有url，定义好url，在类中直接可以调用
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # 访问指定的URL
    def get(self):
        self.driver.get(self.url)

    # 元素定位
    def find_el(self, loc):
        try:
            return self.driver.find_element(*loc)
        except Exception as e:
            LoggerInfo().get_logger().error('元素定位失败......信息{},定位元素:{}'.format(e, *loc))

    # 关闭浏览器
    def quit(self):
        self.driver.quit()
