#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/9/30 15:35
# @File    : random_walk.py
from random import choice


class RandomWalk:
    """一个生成随机漫步数据的类"""
    def __init__(self, num_points=50000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        # 所有的随机漫步都始于点(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step==0 and y_step==0:
                continue
            # 计算下一个点的坐标
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        """计算每次移动的距离"""
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step
