#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/9/30 15:05
# @File    : mpl_squares.py
import matplotlib.pyplot as plt

input_values = [x for x in range(1, 6)]
squares = [x**2 for x in input_values]

plt.plot(input_values, squares, linewidth=5)  # 指定线条粗细
plt.title("Square Numbers", fontsize=24)  # 指定图标题以及字体大小
# 指定横纵坐标轴标题以及字体大小
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14)
plt.show()
