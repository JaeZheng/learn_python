#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : JaeZheng
# @Time    : 2018/9/30 16:28
# @File    : die_visual.py

from die import Die
import pygal

# 创建一个6面骰子
die = Die()
# 掷几次骰子，并把每次的值记录下来
results = [die.roll() for i in range(1000)]

# 分析结果
frequencies = [results.count(value) for value in range(1, die.num_sides)]

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = [x for x in range(1, die.num_sides)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6", frequencies)
hist.render_to_file("die_visual.svg")