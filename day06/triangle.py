#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************
# @File          : triangle.py
# @Author        : Ge丶
# @Time          : 2020/4/12 15:53
# @software      : PyCharm
# ******************************
from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @staticmethod #静态方法，不属于对象，属于类
    def is_valid(a, b, c):
        return a + b > c and a + c > b \
               and b + c > a

    '''
    周长
    '''

    def perimeter(self):
        return self.__a + self.__b + self.__c

    '''
    面积
    '''

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self.__a) \
                    * (half - self.__b) * (half - self.__c))


if __name__ == "__main__":
    a = 3
    b = 4
    c = 5

    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print('周长:%d' % t.perimeter())
        print('面积:%d' % t.area())
    else:
        print('无法构成三角形')
