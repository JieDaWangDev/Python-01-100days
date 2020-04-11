#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************
# @File          : check_code.py
# @Author        : Ge丶
# @Time          : 2020/4/11 17:14
# @software      : PyCharm
# ******************************

from random import randint
import  string


charset = string.digits + string.ascii_letters
def gen_checkCode(num = 4):
    code = ''
    length = len(charset) - 1
    for _ in range(num):
        index = randint(0, length)
        code += charset[index]

    return code


if __name__ == "__main__":
    check_code = gen_checkCode()
    print(check_code)