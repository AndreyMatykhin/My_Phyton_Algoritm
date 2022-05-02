import random

var = random.randint(0, 100)
print('Попробуйте угадать загаданное число за 10 попыток')
for i in range(1, 11):
    temp = int(input(f'Попытка № {i}. Введите число'))
    if temp > var:
        print(f'Загаданное число меньше {temp}. Попробуйте еще раз.')
    elif temp < var:
        print(f'Загаданное число больше {temp}. Попробуйте еще раз.')
    else:
        print('Поздравляем!!! Вы угадали!')
        break
else:
    print('Вы проиграли')
