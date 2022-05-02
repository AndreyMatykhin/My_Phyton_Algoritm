n = int(input('Введите число n'))
sum1 = 0
n1 = n
while n1:
    sum1 += n1
    n1 -= 1
if sum1 == n * (n + 1) / 2:
    print("Результат 1+2+...+n = n(n+1)/2 и равны ", sum1)
else:
    print("Парадокс!!!")
