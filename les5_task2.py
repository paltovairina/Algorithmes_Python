# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict
from collections import deque

num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')
num_1 = deque()
num_2 = deque()
for i in num1:
    num_1.append(i)
for i in num2:
    num_2.append(i)


def my_dex(num):
    dex = 0
    num.reverse()
    for el in range(len(num)):
        dex += my_int[num[el]] * 16 ** el
    return dex


def my_hex(num):
    number = deque()
    while num > 0:
        d = num % 16
        for el in my_int:
            if my_int[el] == d:
                number.append(el)
        num //= 16
    number.reverse()
    return list(number)


symbols = '0123456789ABCDEF'
my_int = defaultdict(int)
counter = 0
for key in symbols:
    my_int[key] += counter
    counter += 1

num_1_dex = my_dex(num_1)
num_2_dex = my_dex(num_2)
sum_hex = my_hex(num_1_dex + num_2_dex)
prod_hex = my_hex(num_1_dex * num_2_dex)

print(f"Сумма чисел {num1} и {num2} равна {sum_hex}")
print(f"Произведение чисел {num1} и {num2} равно {prod_hex}")
