from random import randint


def max_neg_element(task):
    if task:
        temp = -1
        for i in range(0, len(task)):
            if task[i] < 0 and temp == -1:
                temp = i
            elif task[temp] < task[i] < 0:
                temp = i
        return task[temp] if temp != -1 else None
    else:
        return False


print(max_neg_element([1]))
print(max_neg_element([randint(-100, 100) for i in range(10)]))
