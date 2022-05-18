def input_matrix():
    temp = []
    for st in range(0, 4):
        temp_str = []
        summ = 0
        for i in range(0, 4):
            var = int(input(f'Введите {i + 1} элемент {st + 1} строки: '))
            temp_str.append(var)
            summ += var
        temp_str.append(summ)
        temp.append(temp_str)
    return temp


def output_matrix(matrix):
    for k in matrix:
        print(" ".join([str(el).center(5, " ") for el in k[0:4]]) + " | " + str(k[4]).center(5, " "))


output_matrix(input_matrix())
