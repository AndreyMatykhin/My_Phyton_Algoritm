char1 = input("Введите первую букву")
if len(char1) ==1 and char1.isalpha():
    pos1 = int(ord(char1.upper()))
    char2 = input("Введите вторую букву")
    if len(char2) == 1 and char2.isalpha():
        pos2 = ord(char2.upper())
        pos1 = pos1 - 64
        pos2 = pos2 - 64
        print(f'Вы ввели одинаковые буквы {char1}, расположенные на {pos1} месте в алфавите' if pos1 == pos2 else
                  f'Вы ввели букву {char1}, расположенную на {pos1} месте в алфавите, и букву {char2}, расположенную '
                  f'на {pos2} месте в алфавите. Между ними {abs(pos1 - pos2) - 1} букв(а,ы)')
    else:
        print("Вы ввели не букву")
else:
    print("Вы ввели не букву")







