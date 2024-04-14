import numpy as np


def primeNo(x):
    if x < 1:
        return
    prime = np.ndarray(x, dtype=int)
    prime[0] = 2
    size = 1
    i = 3
    while True:
        if size == x:
            return prime
        if checkPrime(i, prime, size):
            prime[size] = i
            size = size + 1
        i = i+2

def checkPrime(x, prime, size)->bool:
    for i in range(0, size):
        if x%prime[i] == 0:
            return False
    return True

print(primeNo(10000))