#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 开始索引 结束索引
# print(L[0:3])

# 前三个
# L[:3]

# 第一个 到 第三个
# L[1:3]

# 倒数 倒数第二个 到 最后一个
# L[-2:]
# ['Bob', 'Jack']

# 倒数 第二个
# L[-2:-1]
# ['Bob']

# 倒数第一个元素的索引是-1

L = list(range(100))

# 前10个数，每两个取一个：
# print(L[:10:2])
# [0, 2, 4, 6, 8]

# 所有数，每5个取一个：
print(L[::5])
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# 只写[:]就可以原样复制一个list：

# 可以针对 list, tuple, str

