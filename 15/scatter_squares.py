#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/9/30 15:13
# @File    : scatter_squares.py
import matplotlib.pyplot as plt

x_values = [x for x in range(1, 1001)]
y_values = [x**2 for x in x_values]
# 参数s设定点的尺寸为200，c设定点的颜色，edgecolor设定点的轮廓的颜色，cmp指定颜色映射，默认值越小颜色越浅
plt.scatter(x_values, y_values, c=y_values, edgecolors="none", s=40, cmap=plt.cm.Blues)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both", which="major", labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
# 保存图标，bbox_inches参数指定将图标多余的空白区域剪掉
plt.savefig("square_plot.png", bbox_inches="tight")
plt.show()