#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************
# @File          : person.py
# @Author        : Ge丶
# @Time          : 2020/4/12 15:02
# @software      : PyCharm
# ******************************

class Person(object):
    __slots__ = {"_name", "_age", "gender"} #仅允许类绑定限定的属性，对子类无效！除非子类也实现__slots__,这样就可以继承父类的限定
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property #不让外部直接访问私有属性，通过@propery，外部可以通过getter和setter来访问属性
    def name(self):
        return self._name

    @property #相当于getter
    def age(self):
        return self._age

    @age.setter #相当于setter
    def age(self, age):
        self._age = age

    def playgame(self):
        if self._age < 18:
            print('Minors are prohibited from playing games!!')
        else:
            print('playing LOL!!!')

    def __str__(self):
        return "Person(%s, %d)" % (self._name, self._age)

    __repr__ = __str__


if __name__ == "__main__":
    person = Person('xiaoming',18)
    print('person(%s, %d)'%(person.name, person.age))
    person.playgame()
    # person.name = 'xiaohua' #AttributeError: can't set attribute
    person.age = 16
    print('person(%s, %d)' % (person.name, person.age))
    person.playgame()
    person.gender = "man"
    print(person.gender)
