# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий,чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

n = int(input('Введите количество предприятий: '))
company = namedtuple('Company', ['p1', 'p2', 'p3', 'p4'])
companies = {}
for i in range(n):
    name = input('Введите наименование предприятия: ')
    profit1 = int(input('Введите прибыль предприятия за 1 квартал: '))
    profit2 = int(input('Введите прибыль предприятия за 2 квартал: '))
    profit3 = int(input('Введите прибыль предприятия за 3 квартал: '))
    profit4 = int(input('Введите прибыль предприятия за 4 квартал: '))
    profit_year = profit1 + profit2 + profit3 + profit4
    companies[name] = company(p1=profit1, p2=profit2, p3=profit3, p4=profit4)

total_profit = ()

for name, profit in companies.items():
    total_profit += profit

average_year_profit = sum(total_profit) / len(companies)
print(f'Средняя прибыль за год для всех предприятий {average_year_profit}')

for name, profit in companies.items():
    if sum(profit) > average_year_profit:
        print(f'Годовая прибыль предприятия {name} выше среднего и равна: {sum(profit)}')

for name, profit in companies.items():
    if sum(profit) < average_year_profit:
        print(f'Годовая прибыль предприятия {name} ниже среднего и равна: {sum(profit)}')
