# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

multiple_2 = 0
multiple_3 = 0
multiple_4 = 0
multiple_5 = 0
multiple_6 = 0
multiple_7 = 0
multiple_8 = 0
multiple_9 = 0
for el in range(2,100):
    if el % 2 == 0:
        multiple_2 += 1
    if el % 3 == 0:
        multiple_3 += 1
    if el % 4 == 0:
        multiple_4 += 1
    if el % 5 == 0:
        multiple_5 += 1
    if el % 6 == 0:
        multiple_6 += 1
    if el % 7 == 0:
        multiple_7 += 1
    if el % 8 == 0:
        multiple_8 += 1
    if el % 9 == 0:
        multiple_9 += 1
print(f'В диапазоне чисел от 2 до 99 {multiple_2} чисел,кратных 2.')
print(f'В диапазоне чисел от 2 до 99 {multiple_3} чисел,кратных 3.')
print(f'В диапазоне чисел от 2 до 99 {multiple_4} чисел,кратных 4.')
print(f'В диапазоне чисел от 2 до 99 {multiple_5} чисел,кратных 5.')
print(f'В диапазоне чисел от 2 до 99 {multiple_6} чисел,кратных 6.')
print(f'В диапазоне чисел от 2 до 99 {multiple_7} чисел,кратных 7.')
print(f'В диапазоне чисел от 2 до 99 {multiple_8} чисел,кратных 8.')
print(f'В диапазоне чисел от 2 до 99 {multiple_9} чисел,кратных 9.')


# 2 вариант решения

final = {}
for n in range(2, 10):
    final[n] = []
    for el in range(2, 100):
        if el % n == 0:
            final[n].append(el)
    print(f'Для числа {n} кратны - {len(final[n])}. Кратные числа: {final[n]}.')
