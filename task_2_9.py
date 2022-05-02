n = int(input('Сколько будет чисел? '))
target = 0
result = 0
for i in range(1, n + 1):
    temp_var = int(input(f'Введите {i} число '))
    temp = temp_var
    temp_result = 0
    while temp // 1:
        temp_result += temp % 10
        temp //= 10
    if temp_result > result:
        target = temp_var
        result = temp_result
print(f'Число {target} наибольшее по сумме цифр среди введенных. Сумма цифр составляет {result}.')
