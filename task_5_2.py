# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


class HexDigit:
    items = {'0': ['F', '1'], '1': ['0', '2'], '2': ['1', '3'], '3': ['2', '4'], '4': ['3', '5'], '5': ['4', '6'],
             '6': ['5', '7'], '7': ['6', '8'], '8': ['7', '9'], '9': ['8', 'A'], 'A': ['9', 'B'], 'B': ['A', 'C'],
             'C': ['B', 'D'], 'D': ['C', 'E'], 'E': ['D', 'F'], 'F': ['E', '0']}

    def __init__(self, value='0', next_dg=None):
        self.value = value
        self.next_digit = next_dg

    def __str__(self):
        return self.value


class HexNumber:
    def __init__(self, value='0'):
        value = [k for k in value[::-1]]
        self.head = HexDigit(value[0])
        self.size = 1
        now_dig = self.head
        for el in value[1:]:
            now_dig.next_digit = HexDigit(el)
            now_dig = now_dig.next_digit
            self.size += 1

    def __str__(self):
        result = [self.head.value]
        now_dig = self.head
        while now_dig.next_digit:
            now_dig = now_dig.next_digit
            result.append(now_dig.value)
        return ''.join(result[::-1])

    def __len__(self):
        return self.size

    def __add__(self, other):
        other_dig = other.head
        self_dig = self.head
        self_dig_value = self_dig.value
        other_dig_value = other_dig.value
        result_head = HexDigit('0')
        result_dig = result_head
        while self_dig or other_dig:
            while self_dig and self_dig_value != '0':
                result_dig.value = HexDigit.items[result_dig.value][1]
                self_dig_value = HexDigit.items[self_dig_value][0]
                if result_dig.value == '0':
                    result_dig.next_digit = HexDigit('1')
            while other_dig and other_dig_value != '0':
                result_dig.value = HexDigit.items[result_dig.value][1]
                other_dig_value = HexDigit.items[other_dig_value][0]
                if result_dig.value == '0':
                    result_dig.next_digit = HexDigit('1')
            if self_dig:
                self_dig = self_dig.next_digit
                self_dig_value = self_dig.value if self_dig else '0'
            if other_dig:
                other_dig = other_dig.next_digit
                other_dig_value = other_dig.value if other_dig else '0'
            if result_dig.next_digit is None and (self_dig or other_dig):
                result_dig.next_digit = HexDigit('0')
                result_dig = result_dig.next_digit
            else:
                result_dig = result_dig.next_digit
        result = [result_head.value]
        now_dig = result_head
        while now_dig.next_digit:
            now_dig = now_dig.next_digit
            result.append(now_dig.value)
        return HexNumber(''.join(result[::-1]))


a = HexNumber('ABF')
print(a, len(a))
b = HexNumber('1F')
print(f'{a} + {b} = {a + b}')

## Для того чтобы реализовать умножение не хватает времени. Извенити, но думаю что это вполне реально