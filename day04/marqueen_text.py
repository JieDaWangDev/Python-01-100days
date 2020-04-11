#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************
# @File          : marqueen_text.py
# @Author        : Ge丶
# @Time          : 2020/4/11 17:01
# @software      : PyCharm
# ******************************
import os
import time


def main():
    content = r'I Love China...'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.5)
        content = content[1:] + content[0]


if __name__ == "__main__":
    main()
