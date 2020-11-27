# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @File     :logger
# @Date     :2020/11/11 16:24
# @Author   :刘旭
-------------------------------------------------
"""

import logging


# 日志类
class LoggerInfo:
    def get_logger(self):
        # 创建日志对象
        logger = logging.getLogger('logger')
        # 设置日志等级
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            # 设置日志显示的格式
            fmt = logging.Formatter(
                fmt='%(asctime)s [%(filename)s] <函数:%(funcName)s>行数:%(lineno)d -%(levelname)s- %(message)s')
            # 创建处理器，输出到控制台
            sh = logging.StreamHandler()
            # 把格式器放入控制台
            sh.setFormatter(fmt)
            sh.setLevel(logging.DEBUG)
            # 把控制器加载到日志器
            logger.addHandler(sh)
            # 创建处理器，输出文本中
            fh = logging.FileHandler('log.log', encoding='utf-8')
            fh.setFormatter(fmt)
            logger.addHandler(fh)
        return logger

def input_log():
    LoggerInfo().get_logger().info('日志打印中......')

input_log()