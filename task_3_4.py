from random import randint


def max_fr_element(task):
    if task:
        temp = {}
        for k in task:
            if k in temp:
                temp[k] += 1
            else:
                temp[k] = 1
        max_fr = [0, 0]
        for key, value in temp.items():
            if max_fr[1] < value:
                max_fr[0] = key
                max_fr[1] = value
        return max_fr[0]
    else:
        return False


print(max_fr_element([1]))
print(max_fr_element([randint(-100, 100) for i in range(100000)]))
