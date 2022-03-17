# 1. Определить, какое число в массиве встречается чаще всего.

import random
import cProfile


def most_common_1(n):
    lst = [random.randint(1, 100) for _ in range(n)]
    most_common = lst[0]
    for el in lst:
        if lst.count(lst[0]) < lst.count(el):
            most_common = el
    return lst, most_common

# 1000 loops, best of 5: 26.7 usec per loop   n = 10
# 1000 loops, best of 5: 230 usec per loop    n = 50
# 1000 loops, best of 5: 688 usec per loop    n = 100
# 1000 loops, best of 5: 12.8 msec per loop   n = 500
# 1000 loops, best of 5: 49 msec per loop     n = 1000


cProfile.run('most_common_1(1000)')

# 77 function calls in 0.000 seconds    n = 10
# 371 function calls in 0.001 seconds   n = 50
# 746 function calls in 0.002 seconds   n = 100
# 3648 function calls in 0.020 seconds  n = 500
# 7261 function calls in 0.056 seconds  n = 1000

# Экспоненциальная сложность алгоритма(при незначительном увеличении n время сильно возрастает)




