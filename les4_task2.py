# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

import cProfile


def erat(n):
    sieve = list(range(n * 20))
    sieve[1] = 0

    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0

    lst = [i for i in sieve if i != 0]
    return lst[n-1]

# 1000 loops, best of 5: 63.8 usec per loop   n = 10
# 1000 loops, best of 5: 354 usec per loop    n = 50
# 1000 loops, best of 5: 754 usec per loop    n = 100
# 1000 loops, best of 5: 4.1 msec per loop    n = 500
# 1000 loops, best of 5: 8.2 msec per loop    n = 1000


cProfile.run('erat(1000)')


# 51 function calls in 0.000 seconds    n = 10
# 173 function calls in 0.001 seconds   n = 50
# 308 function calls in 0.001 seconds   n = 100
# 1234 function calls in 0.020 seconds  n = 500
# 2267 function calls in 0.009 seconds  n = 1000

# Линейная сложность алгоритма с использованием "решета Эратосфена"

def my_func(n):
    count = 1
    number = 1
    prime = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    return number


# 1000 loops, best of 5: 7.36 usec per loop   n = 10
# 1000 loops, best of 5: 122 usec per loop    n = 50
# 1000 loops, best of 5: 458 usec per loop    n = 100
# 1000 loops, best of 5: 11.1 msec per loop   n = 500
# 1000 loops, best of 5: 44.7 msec per loop   n = 1000


cProfile.run('my_func(1000)')


# 13 function calls in 0.000 seconds    n = 10
# 53 function calls in 0.000 seconds    n = 50
# 103 function calls in 0.001 seconds   n = 100
# 503 function calls in 0.012 seconds   n = 500
# 1003 function calls in 0.055 seconds  n = 1000


# В данном алгоритме время значительно возрастает даже при небольшом увеличении n.
# Сложность не линейная,скорее экспоненциальная.

# Вывод: если сравнивать оба алгоритма, то второй лучше показывает себя при небольших объемах данных,
# а первый - при больших. При n = от 10 до 100 меньше времени затрачивается у второго алгоритма,
# но начиная с n = 500 быстрее работает первый алгоритм, и это несмотря на то,
# что число вызова функции у него почти в 2 раза больше,чем у второго.
