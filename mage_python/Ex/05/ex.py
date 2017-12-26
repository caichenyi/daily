# encoding: utf-8
# Author: Cai Chenyi

# def say_hello():
#     print('Hello, World')

# say_hello()

# def re_func():
#     return 'Hello, World'

# a = re_func()
# print(a)

# def rt_multi():
#     return 1, 2, 3

# a, b, c = rt_multi()
# print(a, b, c)

# def say_hello2(name):
#     return 'hello, {}'.format(name)
#
# print(say_hello2('kk'))

# def add(a, b):
#     return a + b
#
# print(add(1, 2))

# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
#
# print(fact(0))

# def fact(n):
#     '''
#     n! = 1 * 2 * ... * n (n > 0)
#     n! = 1 (n = 0)
#     :param n:
#     :type n:
#     :return:
#     :rtype:
#     '''
#     if n ==0:
#         return 1
#     elif n > 0:
#         rt_value = 1
#         for i in range(1, n + 1):
#             rt_value *= i
#         return rt_value
#     else:
#         return None
#
# print(fact(5))

# def add(a, b):
#     print('a={}, b={}'.format(a, b))
#     return a + b
#
# print(add(1, 2))
# print(add(100, 2))
#
# print(add(b=1, a=2))
# print(add(b=100, a=2))

# def add(a, b, c=4):
#     print('a={}, b={}, c={}'.format(a, b, c))
#     return a + b + c
#
# print(add(1, b=2))
# print(add(1, c=2, b=3))

# g_a = 1
# g_b = 2
# g_c = []
# g_d = []
# g_e = [1]
#
# def test_scope(p_a, p_b=3):
#     global g_a
#     l_a =4
#     g_a =5
#     g_c.append(1)
#     g_d = [1]
#     g_e[0] = 2
#     print(g_a, g_b, p_a, p_b, l_a, g_c, g_d, g_e)
#     print(max([g_a,g_b, p_a, p_b, l_a]))
#
# test_scope(g_b)
# print(g_a, g_b, g_c, g_d, g_e)

# g_a = 1
# g_b = []
#
# def test_params(p_a, p_b):
#     p_a = 2
#     p_b.append(2)
#
# test_params(g_a, g_b)
# print(g_a, g_b)

# def add(a, b, *args):
#     print(a, b, args)
#
# add(1, 2)
# add(1, 2, 3)
# add(1, 2, 3, 4, 5)

# def add(*args):
#     _sum = 0
#     for arg in args:
#         _sum += arg
#     return _sum
#
# print(add(1, 2, 3, 4, 5, 6))

# def test(a, b, *args, **kwargs):
#     print(a, b, args, kwargs)
#
# test(1, 2)
# test(1, 2, c=1, d=2)
# test(1, 2, 3, 4, 5, c=1, d=2)

# def test(a, b, *args, f, g, h=1, **kwargs):
#     print(a, b, f, g, h, args, kwargs)
#
# test(1, 2, 3, 4, 5, f=+1, g=2, h=2, c=1, d=2)

# nums = list(range(5))
#
# a, *b, e = nums
# print(a, b, e)
# *a, b, e = nums
# print(a, b, e)

# def add(a, b):
#     return a + b
#
# def test(a, b, f):
#     return f(a, b)
#
# print(test(1, 2, add))

# def maopao(list):
#     for i in range(len(list) - 1):
#         for j in range(len(list) - 1 - i):
#             if list[j] < list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#     print(list)
#
# list = [2, 5, 74, 0, 4, 1, 3, 5]
# maopao(list)

# add = lambda x, y, z: x + y + z
# print(add(1, 2, 3))

# nums = [6, 3, 4, 5, 1, 2]
# print(sorted(nums))

# age = input('请输入年龄：')
# age = int(age) if age.isdigit() else 22
# print(age)
#
# age = input('请输入年龄：')
# age = age.isdigit() and int(age) or 22
# print(age)

# rt_list = []
# for i in range(10):
#     if i % 2 == 0:
#         rt_list.append(i * i)
# print(rt_list)
#
# print([ i * i for i in range(10) if i % 2 == 0 ])
#
# print([(i, j) for i in range(1, 10) for j in range(10) if i <= j])
#
# stat = {'a': 2, 'b': 3, 'e': 4, 'f': 5}
# rt_dict = {}
# for k, v in stat.items():
#     if v % 2 == 0:
#         rt_dict = v * 2
# print({ k:v*2 for k, v in stat.items() if v% 2 == 0 })

import json
users = {'kk': {'name': 'kk', 'age': 29}}
print(users)

print(json.dumps(users))
