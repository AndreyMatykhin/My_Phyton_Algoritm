def dubl_min(task=[]):
    if task:
        temp = []
        for i in range(0, len(task)):
            temp_ind = -1
            for k in range(0, len(temp)):
                if temp[k] <= task[i] and temp_ind == -1:
                    temp_ind = k
                elif temp[temp_ind] <= temp[k] <= task[i]:
                    temp_ind = k
            if temp_ind == -1:
                temp = [task[i]] + temp
            else:
                temp = temp[0:temp_ind + 1] + [task[i]] + temp[temp_ind + 1:]
        return temp[0:2]
    else:
        return False


print(dubl_min())
print(dubl_min([1]))
print(dubl_min([8, 3, 15, 6, 4, 2]))
print(dubl_min([8, 3, 6, 15, 6, 3, 4, 25]))
