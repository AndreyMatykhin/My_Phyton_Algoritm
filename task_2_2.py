var = int(input('Введите число '))
even = 0
odd = 0
if var == 0:
    even = 1
else:
    while var // 1:
        if (var % 10) % 2:
            odd += 1
        else:
            even += 1
        var //= 10
print(f'В заданном числе {even} четных цифр и {odd} - нечетных')
