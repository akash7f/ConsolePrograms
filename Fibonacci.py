def Fibonacci(a):
    if a < 0:
        return None
    if a == 0:
        return 0
    elif a == 1:
        return 1
    return Fibonacci(a - 1) + Fibonacci(a - 2)

if __name__ == "__main__":
    k = 5
    print(f"Fibonacci of {k} is : {Fibonacci(k)}")