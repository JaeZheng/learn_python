#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/9/30 16:52
# @File    : 15-8.py
from die import Die
import pygal

# 创建三个6面骰子
die_1 = Die()
die_2 = Die()
die_3 = Die()
# 掷几次骰子，并把每次的值记录下来
results = [die_1.roll()+die_2.roll()+die_3.roll() for i in range(1000)]

# 分析结果
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result+1)]

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling three D6 1000 times"
hist.x_labels = [x for x in range(3, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file("15-8.svg")