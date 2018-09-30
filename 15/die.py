#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/9/30 16:26
# @File    : die.py

from random import randint


class Die:
    """"一个表示骰子的类"""

    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回骰子随机掷出的值，在1到num_sides之间"""
        return randint(1, self.num_sides)
