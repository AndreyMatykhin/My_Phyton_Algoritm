ab1 = float(input("Введите координаты x первой точки"))
or1 = float(input("Введите координаты y первой точки"))
ab2 = float(input("Введите координаты x второй точки"))
or2 = float(input("Введите координаты y второй точки"))
k = (or1 - or2) / (ab1 - ab2)
b = or2 - k * ab2
print(f'Уравнение прямой y = {k} x {"+" if b > 0 else "-"} {abs(b)}')

