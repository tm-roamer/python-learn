#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 只要把一个列表生成式的[]改成()，就创建了一个generator：
# generator保存的是算法
# g = (x * x for x in range(10))

# print(next(g))
# print(next(g))
# print(next(g))
# for n in g:
#     print(n)

# 斐波拉契数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# fib(6)

# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：

# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)

# o = odd()

# next(o)
# next(o)
# next(o)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# for n in fib(6):
#     print(n)

g = fib(6)
while True:
     try:
         x = next(g)
         print('g:', x)
     except StopIteration as e:
         print('Generator return value:', e.value)
         break
