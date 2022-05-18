def max_min_sum(task=[]):
    if task:
        index_max = 0
        index_min = 0
        result = 0
        k = 0
        lim = 0
        for i in range(0, len(task)):
            if task[index_max] < task[i]:
                index_max = i
            if task[index_min] > task[i]:
                index_min = i
        if index_min < index_max:
            k = index_min + 1
            lim = index_max
        elif index_max < index_min:
            k = index_max + 1
            lim = index_min
        for i in range(k, lim):
            result += task[i]
        return result
    else:
        return False


print(max_min_sum())
print(max_min_sum([1]))
print(max_min_sum([8, 3, 15, 6, 4, 2]))
print(max_min_sum([8, 3, 15, 6, 4, 25]))
