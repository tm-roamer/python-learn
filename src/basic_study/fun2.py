#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print(abs(10))
# print(abs(-10))
# print(abs(10.12))

# print(min(1,2))
# print(max(2,3))

# print(int(1.22))
# print(int(100))
# print(int('100'))

# print(float('100.44'))
# print(float(100.44))
# print(float('100'))

# print(str(100))
# print(str(100.12))
# print(str(True))


# b = '100' * 1

# print(str('100'))
# print(b + 1)

# def my_abs(x):
#   if x >= 0:
#     return x
#   else:
#     return -x

# print(my_abs(10)) 

# from fun import my_abs

# print(my_abs(-10))

# int float list str list, dict, tuple  !!! 很好用 !!!
# print(isinstance(('1.2', 2), (tuple)))

# import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny

# x, y = move(100, 100, 60, math.pi / 6)

# print(x, y)

# import math

# def quadratic(a, b, c):
#   return -b + math.sqrt( b * b - 4 * a * c) / 2 * a

# print(quadratic(2,3,1))

# 定义默认参数要牢记一点：默认参数必须指向不变对象！

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L

# n = 1
# n += 1
# print(n)

# 如果利用可变参数，调用函数的方式可以简化成这样
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum

# print(calc(1, 3, 5, 7))

# 太他妈的优雅了 # 所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
# nums = [1, 2, 3]
# calc(*nums)

# def person(name, age, **kw):
#     kw['job'][1] = '123123'
#     print('name:', name, 'age:', age, 'other:', kw)

# # 牛逼 关键字参数
# list = [1, 3, 4]
# extra = {'city': 'Beijing', 'job': list}
# person('Jack', 24, **extra)

# # 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。(浅copy)
# print(extra)

# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)

# enroll('Bob', 'M', 7, 'shanghai')
# enroll('Adam', 'M', city='Tianjin')

# 定义默认参数要牢记一点：默认参数必须指向不变对象！


# def calc(*args):
#     sum = 0
#     for n in args:
#         sum = sum + n * n
#     return sum


# nums = [1, 2, 3]
# calc(*nums)

# 关键字参数
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)

# person('Michael', 30)
# person('Bob', 35, city='Beijing')
# person('Adam', 45, gender='M', job='Engineer')

# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, **extra)

# 限制关键字参数
# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)

# 命名关键字参数
# def person(name, age, *, city, job):
#     print(name, age, city, job)

# person('Jack', 24, city='Beijing', job='Engineer')


# 命名关键字参数
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)

# person('Jack', 24, ('a', 'b'), city='Beijing', job='Engineer')
# person('Jack', 24, ['a', 'b'], city='Beijing', job='Engineer')

# person('Jack', 24, 'Beijing', 'Engineer')

# def person(name, age, *, city='Beijing', job):
#     print(name, age, city, job)

# person('Jack', 24, job='Engineer')

# def person(name, age, city, job):
#     # 缺少 *，city和job被视为位置参数
#     pass

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f2(1, 2, d=99, ext=None)