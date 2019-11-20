#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式即List Comprehensions

# list(range(1, 11))

# [x * x for x in range(1, 11)]

# [x * x for x in range(1, 11) if x % 2 == 0]

# 还可以使用两层循环，可以生成全排列：
# [m + n for m in 'ABC' for n in 'XYZ']

# import os
# # os.listdir可以列出文件和目录
# print([d for d in os.listdir('.')])

# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# print([ k + '-' + v for k, v in d.items()])


# d = [1, 2, 4, '3', '5']
# print([ x for x in d if isinstance(x, (int, float))])

