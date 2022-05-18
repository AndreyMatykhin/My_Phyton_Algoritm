def max_min_change(task=[]):
    if task:
        index_max = 0
        index_min = 0
        for i in range(0, len(task)):
            if task[index_max] < task[i]:
                index_max = i
            if task[index_min] > task[i]:
                index_min = i
        temp = task[index_min]
        task[index_min] = task[index_max]
        task[index_max] = temp
        return task
    else:
        return False


print(max_min_change())
print(max_min_change([1]))
print(max_min_change([8, 3, 15, 6, 4, 2]))
