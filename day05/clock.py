#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************
# @File          : clock.py
# @Author        : Ge丶
# @Time          : 2020/4/11 21:12
# @software      : PyCharm
# ******************************

from time import sleep
import os
from datetime import datetime


class Clock(object):

    def __init__(self, h, m, s):
        print("__init__")
        self._h = h
        self._m = m
        self._s = s

    @classmethod #类方法
    def now(cls):
        return cls(datetime.now().hour, datetime.now().minute, \
                   datetime.now().second)

    def run(self):
        self._s += 1
        if self._s == 60:
            self._m += 1
            self._s = 0
            if self._m == 60:
                self._h += 1
                self._m = 0
                if self._h == 24:
                    self._h = 0

    def showTime(self):
        # print(f'{self._h:02%d}:{self._m:02%d}:{self._s:02%d}')
        print('%02d:%02d:%02d' % (self._h, self._m, self._s))


if __name__ == "__main__":
    # hour = datetime.now().hour
    # min = datetime.now().minute
    # sec = datetime.now().second
    c = Clock.now();

    while True:
        os.system("cls")
        c.showTime()
        sleep(1)
        c.run()
