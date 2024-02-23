import time
import numpy as np
import random

#no of iterations
n = 10000000

list_1 = []*n
array_1 = np.ndarray(n, dtype=int)

for i in range(n):
    list_1.append(random.randint(0, n))
    array_1[i] = random.randint(0, n)

start_time = time.time()
list_1.sort()
end_time = time.time()

print(f"Time taken by python list to sort {n} values : {end_time - start_time}")

start_time = time.time()
np.sort(array_1)
end_time = time.time()

print(f"Time taken by numpy array to sort {n} values : {end_time - start_time}")
