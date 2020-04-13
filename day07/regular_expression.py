#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************
# @File          : regular_expression.py
# @Author        : Ge丶
# @Time          : 2020/4/13 22:20
# @software      : PyCharm
# ******************************

import re

"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""


def checkQQ():
    username = input("请输入用户名:")
    qq = input("请输入QQ号:")
    m1 = re.match(r'^[A-Za-z0-9_]{6,20}', username)
    m2 = re.match(r'^[1-9]\d[0-9]{4,11}', qq)
    if not m1:
        print('用户名有误！！')

    if not m2:
        print('QQ号错误！！')

    if not m1 and not m2:
        print('账号有误！！')


def findTeleNum():
    sentence = '''
        重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
        不是15600998765，也是110或119，王大锤的手机号才是15600998765。
        '''
    pattern = r'(?<=\D)1[3456789]\d{9}(?=\D)'
    p = re.compile(pattern)
    num = re.findall(p, sentence)
    print(num)


if __name__ == '__main__':
    # checkQQ()

   findTeleNum()