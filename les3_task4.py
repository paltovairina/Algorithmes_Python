# 4. Определить, какое число в массиве встречается чаще всего.

import random

a = [random.randint(1, 100) for _ in range(30)]
print(a)
most_common = a[0]
for el in a:
    if a.count(a[0]) < a.count(el):
        most_common = el

print(f'Число {most_common} встречается {a.count(most_common)} раз(а)')