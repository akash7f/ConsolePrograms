def MergeSort(A):
    if len(A) <= 1:
        return A
    mid = len(A)//2
    left = A[:mid]
    right = A[mid:]
    left = MergeSort(left)
    right = MergeSort(right)
    return Merge(left, right)

def Merge(left, right):
    A = []
    i, j = 0, 0
    while(i < len(left) and j < len(right)):
        if (left(i) < right(j)):
            A.append(left(i))
            i += 1
        else:
            A.append(right(j))
            j += 1

    while(i < len(left)):
        A.append(left(i))
        i += 1

    while(j < len(right)):
        A.append(right(j))
        j += 1
    return A