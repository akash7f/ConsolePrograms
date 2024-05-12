def max_val_cont(arr):
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0 

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            end = i

        if current_sum < 0:
            current_sum = 0
            start = i + 1

    return arr[start:end + 1], max_sum


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -3, 4]
    print(max_val_cont(arr))