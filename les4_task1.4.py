import random
import cProfile


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
    return lst, most_common

# 1000 loops, best of 5: 29.3 usec per loop   n = 10
# 1000 loops, best of 5: 217 usec per loop    n = 50
# 1000 loops, best of 5: 661 usec per loop    n = 100
# 1000 loops, best of 5: 12.4 msec per loop   n = 500
# 1000 loops, best of 5: 47.4 msec per loop   n = 1000


cProfile.run('most_common_4(1000)')

# 60 function calls in 0.000 seconds    n = 10
# 260 function calls in 0.001 seconds   n = 50
# 534 function calls in 0.001 seconds   n = 100
# 2638 function calls in 0.015 seconds  n = 500
# 5265 function calls in 0.060 seconds  n = 1000


# Экспоненциальная сложность алгоритма
