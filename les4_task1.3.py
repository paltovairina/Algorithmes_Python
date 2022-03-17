import random
import cProfile


def most_common_3(n):
    lst = [random.randint(1, 100) for _ in range(n)]
    most_common = max(set(lst), key=lst.count)

    return lst, most_common

# 1000 loops, best of 5: 26 usec per loop    n = 10
# 1000 loops, best of 5: 142 usec per loop   n = 50
# 1000 loops, best of 5: 357 usec per loop   n = 100
# 1000 loops, best of 5: 2.1 msec per loop   n = 500
# 1000 loops, best of 5: 4.34 msec per loop  n = 1000


cProfile.run('most_common_3(1000)')

# 58 function calls in 0.000 seconds    n = 10
# 269 function calls in 0.000 seconds   n = 50
# 538 function calls in 0.001 seconds   n = 100
# 2639 function calls in 0.004 seconds  n = 500
# 5281 function calls in 0.009 seconds  n = 1000

# Линейная сложность алгоритма
