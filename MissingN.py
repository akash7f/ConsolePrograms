def MissingN(array):
    n = len(array)    #n-1 integers from range 1 - n

    e_sum = ((n+1)*(n+2))/2       #expected sum if missing value have been in int
    a_sum = 0                     #actual sum of the list
    for i in range(0, n):
        a_sum += array[i]
    return e_sum - a_sum

if __name__ == "__main__":
    array = [1,2,8,4,9,3,6,7]
    print("Missing integer : ",MissingN(array))