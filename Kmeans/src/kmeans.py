#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateOn : 2017/4/26 0:01
# @Author   : joyesjiang@tencent.com
# @File     : kmeans.py


import numpy as np
import matplotlib.pyplot as plt
INT_MAX = 99999999


def get_min_distance_point(v_x, v_y, point_list_x, point_list_y):
    distance = INT_MAX
    result_idx = 0
    for idx in range(len(point_list_x)):
        point_x = point_list_x[idx]
        point_y = point_list_y[idx]
        value = (v_x - point_x) ** 2 + (v_y - point_y) ** 2
        if value < distance:
            distance = value
            result_idx = idx
    return result_idx

RANGE = 50
N = 30  # 总的点个数
# x = np.random.rand(N) * RANGE  # 由于随机数的大小小于1,这里乘以Range使得范围为0~Range
# y = np.random.rand(N) * RANGE
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
y = [3, 4, 1, 2, 9, 3, 7, 4, 7, 7, 25, 19, 27, 18, 29, 20, 22, 27, 16, 20, 20, 11, 9, 13, 10, 15, 16, 17, 15, 19]
colors = np.array([np.random.rand(1)] * N)  # 随机产生50个颜色值
area = np.pi * 3**2  # 点的半径范围：3

# 画散点图
plt.scatter(x, y, s=area, c=colors)
plt.show()

K = 3
class_x = np.random.rand(K) * RANGE  # 初始化K个分类中心点x坐标值
class_y = np.random.rand(K) * RANGE  # 初始化K个分类中心点y坐标值
k_colors = np.random.rand(K).tolist()  # 为K个分类中心分配颜色
class_area = np.pi * 10 ** 2  # 点的半径范围：8

for i in range(10):
    class_points_map = {}
    print "start calc all_point class"
    for index, value in enumerate(x):
        class_idx = get_min_distance_point(x[index], y[index], class_x, class_y)
        colors[index] = k_colors[class_idx]
        print "cur_point: (%s, %s) --> %s" % (x[index], y[index], class_idx)
        if not class_points_map.has_key(class_idx):
            class_points_map[class_idx] = list()
        class_points_map[class_idx].append((x[index], y[index]))

    print "start calc new_class_point"
    for class_idx in class_points_map:
        size = len(class_points_map[class_idx])
        sum_x = 0
        sum_y = 0
        for point_item in class_points_map[class_idx]:
            sum_x += point_item[0]
            sum_y += point_item[1]
        sum_x /= size
        sum_y /= size
        class_x[class_idx] = sum_x
        class_y[class_idx] = sum_y

    print "end calc new_class_point"
    print colors
    plt.figure(i)
    plt.scatter(x, y, s=area, c=colors)
    plt.scatter(class_x, class_y, s=class_area, c=k_colors)
    plt.show()








