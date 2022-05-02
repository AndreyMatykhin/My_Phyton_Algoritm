n = int(input('Сколько чисел будет в последовательности? '))
target = int(input('Какую цифру будем отслеживать? '))
result = 0
for i in range(1, n + 1):
    temp = int(input(f'Введите {i} число последовательности '))
    if target == 0 and temp == 0:
        result += 1
    else:
        while temp // 1:
            if temp % 10 == target:
                result += 1
            temp //= 10
print(f'В введенной последовательности цифра {target} встречается {result} раз.')
