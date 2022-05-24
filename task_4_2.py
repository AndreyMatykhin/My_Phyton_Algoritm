import time


def simpl_prime(i=1):
    k = 0
    result = 1
    while k != i:
        result += 1
        for n in range(2, result):
            if not (result % n):
                break
        else:
            k += 1
    return result


def erast_prime(i=1):
    prime = [2]
    result = 2
    while len(prime) < i:
        result += 1
        for n in prime:
            if not (result % n):
                break
        else:
            prime.append(result)
    return result


time_start = time.time()
number = simpl_prime(10000)
time_stop = time.time()
print(number, time_stop - time_start)
time_start = time.time()
number = erast_prime(10000)
time_stop = time.time()
print(number, time_stop - time_start)

