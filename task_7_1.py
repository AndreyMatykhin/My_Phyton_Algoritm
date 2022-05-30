# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).
import random
from sys import getsizeof


def bubble_sort_reverse(spisok):
    swapped = False
    for i in range(0, len(spisok)):
        for j in range(len(spisok) - 1, i, -1):
            if spisok[j] > spisok[j - 1]:
                spisok[j - 1], spisok[j] = spisok[j], spisok[j - 1]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return spisok


task_list = [random.randint(0, 200) - 100 for k in range(20)]
print(f'Неотсортированный список: {task_list}')
print(f'Отсортированный по убыванию список: {bubble_sort_reverse(task_list)}')
print('Временная сложность O(n)=n**2')

