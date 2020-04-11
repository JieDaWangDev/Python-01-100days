#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************
# @File          : dayofyear.py
# @Author        : Ge丶
# @Time          : 2020/4/11 18:02
# @software      : PyCharm
# ******************************


def is_leap_y(y):
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0


def day_of_year(year, m, d):
    num_of_day = \
        [[-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
         [-1, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]][is_leap_y(year)]

    total = 0
    for index in range(1, m):
        total += num_of_day[index]

    return total + d


def yanghui():
    L = [1]
    while True:
        yield L
        L = [1] + [L[x] + L[x + 1] for x in range(len(L) - 1)] + [1]


if __name__ == "__main__":
    day = day_of_year(2020, 10, 10)
    print('一年中的第%d天' % day)
    count = 0
    for x in yanghui():
        print(x)
        count += 1
        if count == 10:
            break

