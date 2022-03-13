# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

a = [random.randint(1, 100) for _ in range(30)]
print(f'Массив до изменения: {a}')

max_num = a[0]
min_num = a[0]

for el in a:
    if el > max_num:
        max_num = el
    elif el < min_num:
        min_num = el
min_index = a.index(min_num)
max_index = a.index(max_num)
a[min_index], a[max_index] = a[max_index], a[min_index]
print(f'Массив после замены местами элементов под индексами {min_index} и {max_index}: {a}')

