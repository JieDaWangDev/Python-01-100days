#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************
# @File          : pet_inst.py
# @Author        : Ge丶
# @Time          : 2020/4/12 16:29
# @software      : PyCharm
# ******************************

from day06.pet import Pet

class Dog(Pet):

    def makevoice(self):
        print('%s 汪汪汪...'%self.get_name())

class Cat(Pet):
    def makevoice(self):
        print('%s 喵喵喵...'%self.get_name())

class Pig(Pet):


    def makevoice(self):
        print('%s 哼哼哼...'%self.get_name())

if __name__ == "__main__":
    dog = Dog('金毛')
    cat = Cat('大脸猫')
    pig = Pig('乔治')

    L = [dog, cat, pig]

    for obj in  L:
        obj.makevoice()