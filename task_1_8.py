yer = int(input("Введите год "))
print("Год високосный" if not (yer % 400) or (not (yer % 4) and yer % 100) else "Год невисокосный")
