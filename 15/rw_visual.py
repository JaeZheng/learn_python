#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/9/30 15:42
# @File    : rw_visual.py
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    # 设置窗口尺寸
    plt.figure(figsize=(10, 6))
    # 散点图
    plt.scatter(rw.x_values, rw.y_values, c=list(range(rw.num_points)), s=1, cmap=plt.cm.Blues)
    # 折线图
    # plt.plot(rw.x_values, rw.y_values, linewidth=5)
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("再跑一次？(y/n):")
    if keep_running == "n":
        break
