def _countZeros(arr, left, right):
    
    if right < left:
        return None
    mid = (right + left)//2

    if arr[mid] == 1:
        if arr[mid - 1] == 0:
            return mid
        return _countZeros(arr, left, mid - 1)
    else:
        if arr[mid + 1] == 1:
            return mid + 1
        return _countZeros(arr, mid+1, right)
    
def countZeros(arr):
    return _countZeros(arr, 0, len(arr))

if __name__ == "__main__":
    arr = [0,0,0,0,0,0,0,1,1,1,1,1]
    print("No of zeroes : ", countZeros(arr))