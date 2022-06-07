# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая
# только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
import hashlib


def numb_different_substrings(s=''):
    result = set()
    for i in range(len(s)):
        for m in range(1, (len(s) - i) // 2 + 1):
            h_subs = hashlib.sha1(s[i:i + m].encode('utf-8')).hexdigest()
            for k in range(i + m, len(s) + 1 - m):
                if h_subs != hashlib.sha1(s[k:k + m].encode('utf-8')).hexdigest():
                    result.add(h_subs)
                    break
    return len(result)


print(numb_different_substrings('dffgdfgdfg'))
print(numb_different_substrings('dffgdf'))
print(numb_different_substrings())
