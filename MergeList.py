def Kth_smallest_element(list_m, list_n, k):

    m, n = len(list_m), len(list_n)

    if k < 1 or k > m+n+1:
        return
    k = k-1

    a, b = 0, 0
    while( a < m and b < n):

        if k == a + b:
            if(list_m[a] < list_n[b]):
                return list_m[a]
            else:
                return list_n[b]
                    
        elif(list_m[a] < list_n[b]):
            a += 1
        else:
            b += 1

    while( a < m):
        if k == a+b:
            return list_m[a]
        a += 1

    while(b < n):
        if k == a+b:
            return list_n[b]
        b += 1

def Kth_smallest_element_unsorted(list_m, list_n, k):
    if k < 1 or k > len(list_m) + len(list_n) + 1:
        return
    list_m.sort()
    list_n.sort()
    return Kth_smallest_element(list_m, list_n, k)

if __name__ == "__main__":

    list_m=[2,5,7,3,9]
    list_n=[6,4,10,8,1]

    k = 1
    print(f"{k}th smallest element in {list_m} and {list_n}")
    print(Kth_smallest_element_unsorted(list_m, list_n, k))

    k = 5
    print(f"{k}th smallest element in {list_m} and {list_n}")
    print(Kth_smallest_element_unsorted(list_m, list_n, k))

    k = 10
    print(f"{k}th smallest element in {list_m} and {list_n}")
    print(Kth_smallest_element_unsorted(list_m, list_n, k))
