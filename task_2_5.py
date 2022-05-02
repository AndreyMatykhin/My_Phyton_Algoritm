temp = ''
for k in range(32, 128, 1):
    if not ((k - 32) % 10) and temp:
        print(temp)
        temp = ''
    temp += f'{k} - {chr(k)} ,'.rjust(9, ' ')
else:
    print(temp)
