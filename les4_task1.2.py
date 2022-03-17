import random
import cProfile


def most_common_2(n):
    lst = [random.randint(1, 100) for _ in range(n)]
    num_dict = {}
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

            return lst, most_common

# 1000 loops, best of 5: 23.6 usec per loop   n = 10
# 1000 loops, best of 5: 112 usec per loop    n = 50
# 1000 loops, best of 5: 212 usec per loop    n = 100
# 1000 loops, best of 5: 1.05 msec per loop   n = 500
# 1000 loops, best of 5: 2.25 msec per loop   n = 1000


cProfile.run('most_common_2(1000)')

# 64 function calls in 0.000 seconds    n = 10
# 268 function calls in 0.000 seconds   n = 50
# 532 function calls in 0.001 seconds   n = 100
# 2673 function calls in 0.002 seconds  n = 500
# 5280 function calls in 0.007 seconds  n = 1000

# Линейная сложность алгоритма(время увеличивается пропорционально увеличению числа n)


