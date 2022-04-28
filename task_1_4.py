import random

bor1 = input("Введите первую границу диапазона генерации")
bor2 = input("Введите вторую границу диапазона генерации")
if (bor1.count('.') == 1 and ''.join(bor1.split('.')).isdigit() or bor1.isdigit()) and \
        (bor2.count('.') == 1 and ''.join(bor2.split('.')).isdigit() or bor2.isdigit()):
    if "." in bor1:
        bor1 = float(bor1)
    else:
        bor1 = int(bor1)
    if "." in bor2:
        bor2 = float(bor2)
    else:
        bor2 = int(bor2)
    if type(bor1) == float or type(bor2) == float:
        res = random.uniform(bor1, bor2)
    else:
        res = random.randint(bor1, bor2) if bor2 > bor1 else random.randint(bor2, bor1)
    print(f'Сгенерированное значение = {res}')
else:
    if len(bor1) == 1 and bor1.isalpha() and len(bor1) == 1 and bor1.isalpha() and ord(bor1.upper()) > 64 and ord(
            bor1.upper()) < 91 and ord(bor2.upper()) > 64 and ord(bor2.upper()) < 91:
        res = chr(random.randint(ord(bor1.upper()), ord(bor2.upper())) if ord(bor2.upper()) > ord(
            bor1.upper()) else random.randint(ord(bor2.upper()), ord(bor1.upper())))
        print(f'Сгенерированное значение = {res}')
    else:
        print("Задан неправильный диапазон")
