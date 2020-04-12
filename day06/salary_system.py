#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************
# @File          : salary_system.py
# @Author        : Ge丶
# @Time          : 2020/4/12 20:03
# @software      : PyCharm
# ******************************

from abc import abstractmethod, ABCMeta

# 通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类
class Employee(object, metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def getSalary(self):
        pass


class Manager(Employee):

    def getSalary(self):
        return 15000.0


class Programmer(Employee):

    def __init__(self, name, hour=0):
        super().__init__(name)
        self.__hour = hour

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, h):
        self.__hour = h

    def getSalary(self):
        return 150.0 * self.hour


class Seller(Employee):

    def __init__(self, name, sales=0):
        super().__init__(name)
        self.__sales = sales

    @property
    def sales(self):
        return self.__sales

    @sales.setter
    def sales(self, sales):
        self.__sales = sales

    def getSalary(self):
        return 1200.0 + self.sales * 0.05


if __name__ == "__main__":

    emps = [Manager('xiaoming'), Programmer('xiaohua'), Seller('xiaohong')]

    for emp in emps:
        if isinstance(emp, Programmer):
            hours = int(input("请输入%s的工作时长：" % emp.name))
            emp.hour = hours
        elif isinstance(emp, Seller):
            sales = int(input("请输入%s的销售额：" % emp.name))
            emp.sales = sales

        print('%s的薪资是%.2f' % (emp.name, emp.getSalary()))
