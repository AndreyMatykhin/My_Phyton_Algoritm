# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность
# вашей ОС.

# Версия Python 3.10.0
# ОС Windows 10 x64

# Возьмем задачу 1 к уроку 3
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
from sys import getsizeof

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

total_size = getsizeof(i) + getsizeof(on_lst) + getsizeof(dl) + getsizeof(key) + getsizeof(value) + getsizeof(result)
print(f'Переменные занимают {total_size}')


# Возьмем задачу 2 к уроку 4
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»


def simpl_prime(i=1):
    k = 0
    result = 1
    while k != i:
        result += 1
        for n in range(2, result):
            if not (result % n):
                break
        else:
            k += 1
    total_size = getsizeof(result) + getsizeof(k) + getsizeof(n)
    print(f'Переменные занимают {total_size}')
    return result


print(simpl_prime(100))


def erast_prime(i=1):
    prime = [2]
    result = 2
    while len(prime) < i:
        result += 1
        for n in prime:
            if not (result % n):
                break
        else:
            prime.append(result)
    total_size = getsizeof(result) + getsizeof(prime) + getsizeof(n)
    print(f'Переменные занимают {total_size}')
    return result


print(erast_prime(100))

# На примере 2 задачи к уроку 4 видно, что применения решета Эратосфена сокращает временные затраты, но увеличивает
# затрачиваемый объем памяти.