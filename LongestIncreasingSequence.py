import numpy as np
def LISS(array):
    n = len(array)
    dm = np.ones(n)

    max_index = -1
    max_length = 0
    for i in range(1, n):
        for j in range(i):
            if array[i] > array[j]:
                dm[i] = max(dm[i], dm[j] + 1)
                if dm[i] > max_length:
                        max_length = dm[i]
                        max_index = i
    
    selected_nums = [array[max_index]]
    current_length = max_length
    for i in range(max_index - 1, -1, -1):
        if array[i] < array[max_index] and dm[i] == current_length - 1:
            selected_nums.append(array[i])
            current_length -= 1

    selected_nums.reverse()
    return selected_nums

if __name__ == "__main__":
    array = [6, 2, 9, 5, 1, 4, 1, 3]
    array.reverse()
    print(LISS(array))