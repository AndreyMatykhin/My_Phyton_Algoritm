var = int(input('Введите число '))
rav = ''
if var == 0:
    rav = '0'
else:
    while var // 1:
        rav += str(var % 10)
        var //= 10
print(f'Введенное число наоборот: {rav}')
