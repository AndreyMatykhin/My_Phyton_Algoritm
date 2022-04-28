ab = int(input("Введите длину стороны AB"))
bc = int(input("Введите длину стороны BC"))
ac = int(input("Введите длину стороны AC"))
if ab + bc < ac or bc + ac < ab or ac + ab < bc:
    print("Треугольника не существует")
elif ab == ac and ab == bc:
    print("Треугольник равносторонний")
elif ab == ac or ab == bc or ac == bc:
    print("Треугольник равнобедренный")
else:
    print("Треугольник разносторонний")
