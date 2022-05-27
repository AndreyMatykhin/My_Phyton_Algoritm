# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.
import collections

n = int(input("Сколько будет предпрриятий? "))
company = collections.defaultdict(list)
for i in range(0, n):
    temp_name = input(f"Введите название {i + 1} предприятия ")
    temp_list = []
    for k in range(0, 4):
        temp_list.append(int(input(f'Введите доход компании {temp_name} за {k + 1} квартал ')))
    company[temp_name] = temp_list
avg_income = sum([sum(k) for k in company.values()]) / len(company) if len(company) != 0 else 0
top_avg = []
low_avg = []
for k, i in company.items():
    if sum(i) < avg_income:
        low_avg.append(k)
    elif sum(i) > avg_income:
        top_avg.append(k)
print(f'Предприятие(я) {", ".join(low_avg)} с доходом ниже общего среднегодовго {avg_income}' if len(low_avg) else
      f'Предприятий с доходом ниже общего среднегодового {avg_income} нет')
print(f'Предприятие(я) {", ".join(top_avg)} с доходом выше общего среднегодового {avg_income}' if len(top_avg) else
      f'Предприятий с доходом выше общего среднегодового {avg_income} нет')
