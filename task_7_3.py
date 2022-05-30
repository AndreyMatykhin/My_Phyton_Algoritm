# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
# сложно, то используйте метод сортировки, который не рассматривался на уроках
import random
from sys import getsizeof


def max_m(temp, t):
    drop = 0
    for i in range(len(temp)):
        if temp[drop] < temp[i]:
            drop = i
    if t:
        return max_m(temp[:drop] + temp[drop + 1:], t - 1)
    else:
        return temp[drop]


def med_list(mas):
    return max_m(mas, (len(mas) - 1) / 2)


m = int(input('Введите значение m, определяющее размер массива (2m + 1): '))
task_list = [random.randint(0, 200) - 100 for k in range(2 * m + 1)]
print(f'Случайно заполненый массив размером (2m + 1): {task_list}')
print(f'Медианное значение заданного массива: {med_list(task_list)}')
print('Временная сложность O(n)=((n**2)/2)+n')
