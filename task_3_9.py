def max_in_min(task):
    result = False
    for t in range(0, len(task[0])):
        res_min = task[0][t]
        for i in range(0, len(task)):
            if res_min > task[i][t]:
                res_min = task[i][t]
        if result < res_min or result == False:
            result = res_min
    return result


matrix = [[8, 13, 6, 15, 6, 34, 4, 25],
          [15, 6, 3, 4, 25, 8, 346, 6],
          [5, 6, 3, 4, 25, 6, 15, 6],
          [3, 4, 258, 3, 6, 15, 6, 3]]
print(max_in_min(matrix))
