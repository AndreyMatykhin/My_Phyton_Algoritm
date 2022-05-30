# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random
from sys import getsizeof


def merge_sort(spisok):
    if len(spisok) < 2:
        return spisok
    else:
        a = merge_sort(spisok[0:len(spisok) // 2])
        b = merge_sort(spisok[len(spisok) // 2:])
        i = j = 0
        temp = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                temp.append(a[i])
                i += 1
            else:
                temp.append(b[j])
                j += 1
        while i < len(a):
            temp.append(a[i])
            i += 1
        while j < len(b):
            temp.append(b[j])
            j += 1
        return temp


task_list = [random.random() * 50 for k in range(20)]
print(f'Неотсортированный список: {task_list}')
print(f'Отсортированный по убыванию список: {merge_sort(task_list)}')
print('Временная сложность O(n)=nlogn')
