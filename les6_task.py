import sys
import random

print(sys.version, sys.platform)

# 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] win32


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__},size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x,'__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level+1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level+1)


# 1. Определить, какое число в массиве встречается чаще всего.

def most_common_1(n):
    lst = [random.randint(1, 100) for _ in range(n)]
    most_common = lst[0]
    for el in lst:
        if lst.count(lst[0]) < lst.count(el):
            most_common = el
    return lst, most_common


# print(show_size(most_common_1(10)))


# type = <class 'tuple'>,size = 56, object = ([4, 63, 1, 69, 32, 6, 49, 12, 28, 93], 4)
# # 	 type = <class 'list'>,size = 184, object = [4, 63, 1, 69, 32, 6, 49, 12, 28, 93]
# # 		 type = <class 'int'>,size = 28, object = 4
# # 		 type = <class 'int'>,size = 28, object = 63
# # 		 type = <class 'int'>,size = 28, object = 1
# # 		 type = <class 'int'>,size = 28, object = 69
# # 		 type = <class 'int'>,size = 28, object = 32
# # 		 type = <class 'int'>,size = 28, object = 6
# # 		 type = <class 'int'>,size = 28, object = 49
# # 		 type = <class 'int'>,size = 28, object = 12
# # 		 type = <class 'int'>,size = 28, object = 28
# # 		 type = <class 'int'>,size = 28, object = 93
# # 	 type = <class 'int'>,size = 28, object = 4


def most_common_2(n):
    lst = [random.randint(1, 100) for _ in range(n)]
    num_dict = {}
    most_common = 0
    for el in lst:
        if el in num_dict:
            num_dict[el] += 1
        else:
            num_dict[el] = 1
    max_freq = 1
    for el in num_dict.keys():
        if num_dict.get(el) > max_freq:
            max_freq = num_dict.get(el)
            most_common = el

    return num_dict, lst, most_common


# print(show_size(most_common_2(10)))


# type = <class 'tuple'>,size = 64, object = ({61: 1, 98: 1, 75: 1, 86: 1, 9: 1, 99: 1, 5: 1, 92: 1, 35: 1, 54: 1},
# [61, 98, 75, 86, 9, 99, 5, 92, 35, 54], 0)
# 	 type = <class 'dict'>,size = 360, object = {61: 1, 98: 1, 75: 1, 86: 1, 9: 1, 99: 1, 5: 1, 92: 1, 35: 1, 54: 1}
# 		 type = <class 'tuple'>,size = 56, object = (61, 1)
# 			 type = <class 'int'>,size = 28, object = 61
# 			 type = <class 'int'>,size = 28, object = 1
# 		 type = <class 'tuple'>,size = 56, object = (98, 1)
# 			 type = <class 'int'>,size = 28, object = 98
# 			 type = <class 'int'>,size = 28, object = 1
# 		 type = <class 'tuple'>,size = 56, object = (75, 1)
# 			 type = <class 'int'>,size = 28, object = 75
# 			 type = <class 'int'>,size = 28, object = 1
# 		 type = <class 'tuple'>,size = 56, object = (86, 1)
# 			 type = <class 'int'>,size = 28, object = 86
# 			 type = <class 'int'>,size = 28, object = 1
# 		 type = <class 'tuple'>,size = 56, object = (9, 1)
# 			 type = <class 'int'>,size = 28, object = 9
# 			 type = <class 'int'>,size = 28, object = 1
# 		 type = <class 'tuple'>,size = 56, object = (99, 1)
# 			 type = <class 'int'>,size = 28, object = 99
# 			 type = <class 'int'>,size = 28, object = 1
# 		 type = <class 'tuple'>,size = 56, object = (5, 1)
# 			 type = <class 'int'>,size = 28, object = 5
# 			 type = <class 'int'>,size = 28, object = 1
# 		 type = <class 'tuple'>,size = 56, object = (92, 1)
# 			 type = <class 'int'>,size = 28, object = 92
# 			 type = <class 'int'>,size = 28, object = 1
# 		 type = <class 'tuple'>,size = 56, object = (35, 1)
# 			 type = <class 'int'>,size = 28, object = 35
# 			 type = <class 'int'>,size = 28, object = 1
# 		 type = <class 'tuple'>,size = 56, object = (54, 1)
# 			 type = <class 'int'>,size = 28, object = 54
# 			 type = <class 'int'>,size = 28, object = 1
# 	 type = <class 'list'>,size = 184, object = [61, 98, 75, 86, 9, 99, 5, 92, 35, 54]
# 		 type = <class 'int'>,size = 28, object = 61
# 		 type = <class 'int'>,size = 28, object = 98
# 		 type = <class 'int'>,size = 28, object = 75
# 		 type = <class 'int'>,size = 28, object = 86
# 		 type = <class 'int'>,size = 28, object = 9
# 		 type = <class 'int'>,size = 28, object = 99
# 		 type = <class 'int'>,size = 28, object = 5
# 		 type = <class 'int'>,size = 28, object = 92
# 		 type = <class 'int'>,size = 28, object = 35
# 		 type = <class 'int'>,size = 28, object = 54
# 	 type = <class 'int'>,size = 24, object = 0


def most_common_3(n):
    lst = [random.randint(1, 100) for _ in range(n)]
    most_common = max(set(lst), key=lst.count)

    return set(lst), most_common


# print(show_size(most_common_3(10)))


# type = <class 'tuple'>,size = 56, object = ({32, 38, 6, 72, 14, 85, 86, 59}, 72)
# 	 type = <class 'set'>,size = 728, object = {32, 38, 6, 72, 14, 85, 86, 59}
# 		 type = <class 'int'>,size = 28, object = 32
# 		 type = <class 'int'>,size = 28, object = 38
# 		 type = <class 'int'>,size = 28, object = 6
# 		 type = <class 'int'>,size = 28, object = 72
# 		 type = <class 'int'>,size = 28, object = 14
# 		 type = <class 'int'>,size = 28, object = 85
# 		 type = <class 'int'>,size = 28, object = 86
# 		 type = <class 'int'>,size = 28, object = 59
# 	 type = <class 'int'>,size = 28, object = 72


def most_common_4(n):
    lst = [random.randint(1, 100) for _ in range(n)]
    number = 0
    most_common = 0
    for el in lst:
        b = el
        c = 0
        for i in lst:
            if i == b:
                c += 1
        if c > number:
            number = c
            most_common = b
    return b, c, lst, most_common


# print(show_size(most_common_4(10)))


# type = <class 'tuple'>,size = 72, object = (46, 1, [96, 57, 30, 83, 5, 33, 69, 42, 76, 46], 96)
# 	 type = <class 'int'>,size = 28, object = 46
# 	 type = <class 'int'>,size = 28, object = 1
# 	 type = <class 'list'>,size = 184, object = [96, 57, 30, 83, 5, 33, 69, 42, 76, 46]
# 		 type = <class 'int'>,size = 28, object = 96
# 		 type = <class 'int'>,size = 28, object = 57
# 		 type = <class 'int'>,size = 28, object = 30
# 		 type = <class 'int'>,size = 28, object = 83
# 		 type = <class 'int'>,size = 28, object = 5
# 		 type = <class 'int'>,size = 28, object = 33
# 		 type = <class 'int'>,size = 28, object = 69
# 		 type = <class 'int'>,size = 28, object = 42
# 		 type = <class 'int'>,size = 28, object = 76
# 		 type = <class 'int'>,size = 28, object = 46
# 	 type = <class 'int'>,size = 28, object = 96


# Вывод: меньше всего памяти задействуется в первом варианте, так как во втором используется словарь,
# в третьем - множество, а в четвертом - дополнительные переменные.
