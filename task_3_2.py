def index_chet(task=[]):
    result = [i for i in range(0, len(task)) if not (task[i] % 2)]
    if result:
        return result
    else:
        return -1


print(index_chet())
print(index_chet([8, 3, 15, 6, 4, 2]))
