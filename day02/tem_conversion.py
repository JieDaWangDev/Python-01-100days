#!/usr/bin/env python3
# -*- coding: utf-8-*-
# ******************************
# @File    : tem_conversion.py
# @Author  : Ge丶
# @Time    : 2020/4/8 21:59
# @SW      : PyCharm
# ******************************
from math import pi

'''
华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。
'''


def temperature_change():
    f = float(input('请输入华氏温度：'))
    c_temperature = (f - 32) // 1.8
    print('华氏温度{} = 摄氏度{}'.format(f, c_temperature))
    # print(f'华氏温度{f:.1f} 摄氏度{c_temperature:1f}')


'''
输入半径计算圆的周长和面积
'''


def calculation_circle():
    radius = int(input("请输入圆的半径:"))
    permiter = 2 * pi * radius
    area = pi * radius ** 2
    print("周长：{0:.2f}，面积：{1:.2f}".format(permiter, area))


'''
判断是否是闰年
'''


def check_leap():
    year = int(input("请输入年份:"))
    is_leap = year % 4 == 0 and year % 100 != 0 \
              or year % 400 == 0
    print('闰年：%r' % is_leap)


if __name__ == "__main__":
    temperature_change()
    # calculation_circle()
    # check_leap()
