#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************
# @File          : find_max.py
# @Author        : Ge丶
# @Time          : 2020/4/11 17:27
# @software      : PyCharm
# ******************************
'''
找出给定集合的第一大跟第二大数据
'''


def find(L):
    m1, m2 = (L[0], L[1]) if L[0] > L[1] else (L[1], L[0])
    print(L)
    for index in range(2, len(L)):
        if L[index] > m1:
            m2 = m1
            m1 = L[index]

        elif L[index] > m2:
            m2 = L[index]

    return m1, m2


if __name__ == "__main__":
    l = [x for x in range(10)]
    max1, max2 = find(l)
    print(f'最大{max1} 次大{max2}')
