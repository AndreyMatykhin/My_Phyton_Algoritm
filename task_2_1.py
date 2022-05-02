act = ''
while act != '0':
    var1 = float(input('Введите первую переменную'))
    var2 = float(input('Введите вторую переменную'))
    act = input('Введите действие (-, + , /, *) или ноль для выхода')
    if act == '+':
        print(f'Результат {var1} + {var2} = {var1 + var2}')
    elif act == '-':
        print(f'Результат {var1} - {var2} = {var1 - var2}')
    elif act == '*':
        print(f'Результат {var1} * {var2} = {var1 * var2}')
    elif act == '/':
        print(f'Результат {var1} / {var2} = {var1 / var2}' if var2 else 'Деление невозможно')
