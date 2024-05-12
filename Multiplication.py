from timeit import default_timer as timer
import matplotlib.pyplot as plt
import random

def naive_multiply(x, y):
    count = 0
    if y < x:
        x, y = y, x
    for i in range(0, x):
        count += y

def Karatsuba(x, y):
    if x<10 or y<10:
        return x*y
    n = max(len(str(x)), len(str(y)))
    n2 = n//2
    t = 10**n2

    a = x//t
    b = x%t
    c = y//t
    d = y%t

    ac = Karatsuba(a, c)
    bd = Karatsuba(b, d)
    ad_bc = Karatsuba(a + b, c + d) - (ac + bd)
    return ac*t*t + ad_bc*t + bd


if __name__ == "__main__":

    x = []
    y1 = []
    y2 = []

    for i in range(5):
        a = random.randint(0, 10000)
        x.append(a)

        start_time = timer()
        naive_result = naive_multiply(a, a)
        time = timer() - start_time
        y1.append(time)

        start_time = timer()
        naive_result = Karatsuba(a, a)
        time = timer() - start_time
        y2.append(time)
  
    bar_width = 0.35

    r1 = range(len(x))
    r2 = [x + bar_width for x in r1]

    plt.bar(r1, y1, color='b', width=bar_width, edgecolor='grey', label='Naive Multiplication')
    plt.bar(r2, y2, color='r', width=bar_width, edgecolor='grey', label='Karatsuba (D&C) Multiplication')

    plt.xlabel('X')
    plt.ylabel('Values')
    plt.xticks([r + bar_width/2 for r in range(len(x))], x)

    plt.legend()
    plt.show()
