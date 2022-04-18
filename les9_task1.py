# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1()
# или любой другой из модуля hashlib задача считается не решённой.

import hashlib


def subs_count(s: str):
    assert len(s) > 0, 'Строка не может быть пустой'
    len_str = len(s)
    hash_set = set()

    for i in range(len_str + 1):
        for j in range(i + 1, len_str + 1):
            h = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)

    return len(hash_set)


my_str = input('Введите строку: ')
substr = subs_count(my_str)
print(f'Количество подстрок в строке "{my_str}" равно {substr}')
