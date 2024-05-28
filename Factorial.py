def Factorial(a):
    if a < 0:
        return None
    elif a == 0:
        return 1
    return a*Factorial(a - 1)

if __name__ == "__main__":
    k = 5
    print(f"Factorial of {k} is : {Factorial(k)}")