#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ******************************
# @File          : pet.py
# @Author        : Ge丶
# @Time          : 2020/4/12 16:26
# @software      : PyCharm
# ******************************

from abc import abstractmethod, ABCMeta



class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self.__nickname = nickname

    @abstractmethod
    def makevoice(self):
        pass


    def get_name(self):
        return self.__nickname
