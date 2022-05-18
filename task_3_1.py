result = {}
for i in range(2, 100):
    on_lst = []
    for dl in range(2, 10):
        if i % dl == 0:
            on_lst.append(dl)
    if on_lst:
        result[i] = on_lst
for key, value in result.items():
    print(f'Число {key} кратно {", ".join([str(k) for k in value])}')
print(f'В диапазоне натуральных чисел от 2 до 99 всего {len(result)} кратны каждому из чисел в диапазоне от 2 до 9')
