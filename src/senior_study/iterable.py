#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from collections.abc import Iterable

# isinstance([], Iterable)
# # True
# isinstance({}, Iterable)
# # True
# isinstance('abc', Iterable)
# # True

# # 生成器 generator
# isinstance((x for x in range(10)), Iterable)
# # True

# isinstance(100, Iterable)
# # False



# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator

# from collections.abc import Iterator

# isinstance((x for x in range(10)), Iterator)
# # True

# isinstance([], Iterator)
# # False

# isinstance({}, Iterator)
# # False

# isinstance('abc', Iterator)
# # False

# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# Python的for循环本质上就是通过不断调用next()函数实现的

