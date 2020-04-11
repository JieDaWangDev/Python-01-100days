#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************
# @File          : lotteryticket.py
# @Author        : Ge丶
# @Time          : 2020/4/11 20:35
# @software      : PyCharm
# ******************************
from random import sample, randint


def select_balls():
    red_balls = [x for x in range(1, 34)]
    sele_balls = []
    sele_balls = sample(red_balls, 6)
    sele_balls.sort()
    sele_balls.append(randint(1, 16))
    return sele_balls


def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print("|", end=' ')
        print("%02d" % ball, end=' ')
    print()


if __name__ == "__main__":
    count = int(input("请输入注数："))
    for _ in range(count):
        display(select_balls())
