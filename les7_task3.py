# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.


import random

m = int(input('Введите целое положительное число: '))
len_arr = 2 * m + 1
my_array = [random.randint(0, 100) for _ in range(len_arr)]
random.shuffle(my_array)
print(my_array)


for el in my_array:
    a = el
    lst = my_array.copy()
    lst.remove(a)
    small = []
    large = []
    for i in lst:
        if i <= a:
            small.append(i)
        elif i >= a:
            large.append(i)
    if len(small) == len(large) and len(small) != 0:
        print(f'Медиана массива {my_array}: {a}')










