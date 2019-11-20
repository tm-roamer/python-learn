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

def my_abs(x):
  if x >= 0:
    return x
  else:
    return -x

def my_abs2(x):
  if (not isinstance(x, (int, float))):
    raise TypeError('bad operand type')
  if x >= 0:
    return x
  else:
    return -x

# print(my_abs(10)) 