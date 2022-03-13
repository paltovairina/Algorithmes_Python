# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

a = [random.randint(-100, 100) for _ in range(30)]
print(a)

index_a = -1
for el in a:
    if el < 0:
        if index_a == -1:
            index_a = a.index(el)
        else:
            if el > a[index_a]:
                index_a = a.index(el)

print(f'Максимальный отрицательный элемент в массиве : {a[index_a]}, он находится под индексом {index_a}')