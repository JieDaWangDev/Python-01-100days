#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************
# @File          : day03.py
# @Author        : Ge丶
# @Time          : 2020/4/9 22:39
# @software      : PyCharm
# ******************************
'''
100~999的水仙花数
'''


def lily():
    for x in range(100, 1000):
        low = x % 10
        mid = x // 10 % 10
        high = x // 100
        if x == low ** 3 + mid ** 3 + high ** 3:
            print('\n', x)


'''
《百钱百鸡》问题
'''


def chicken():
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print('公鸡:{}, 母鸡:{}, 小鸡:{}'.format(x, y, z))


'''
CRAPS赌博游戏
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
'''
import random


def craps_game():
    money = 1000
    first = 0
    is_first = True
    while money > 0:
        while True:
            bet = int(input("请下注:"))
            if 0 < bet <= money:
                break
        needs_to_go = False
        if (is_first):
            is_first = False
            first = random.randint(1, 6) + random.randint(1, 6)
            print('玩家第一次摇出了%d点' % first)
            if first == 7 or first == 11:
                money += bet
                print('玩家胜！')
            elif first == 2 or first == 3 or first == 12:
                money -= bet
                print('庄家胜！')
            else:
                needs_to_go = True
        else:
            needs_to_go = True
        print("剩余金额：%d" % money)
        while needs_to_go:
            needs_to_go = False
            current = random.randint(1, 6) + random.randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                money -= bet
                print('庄家胜！')
            elif current == first:
                money += bet
                print('玩家胜！')
            else:
                needs_to_go = True
            print("剩余金额->：%d" % money)
    print('no money!!!')

if __name__ == '__main__':
    # lily()
    # chicken()

    craps_game()
