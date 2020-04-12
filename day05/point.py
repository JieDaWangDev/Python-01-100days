#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************
# @File          : point.py
# @Author        : Ge丶
# @Time          : 2020/4/12 10:57
# @software      : PyCharm
# ******************************
from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return 'Point(%d, %d)' % (self.x, self.y)

    __repr__ = __str__


if __name__ == "__main__":
    p1 = Point()
    p2 = Point(3, 5)
    print(p1)
    p1.move_to(2, 8)
    print('p1 to p2 distance: %.2f' % p1.distance_to(p2))
