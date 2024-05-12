from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt

def bubble_sort(array):
    n = len(array)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


def merge_sort(array):
    n = len(array)
    if n <= 1:
        return
    mid = n//2

    left = array[:mid]
    right = array[mid:]
    l_len = mid
    r_len = n-mid
    merge_sort(left)
    merge_sort(right)

    m, n = 0, 0

    while(m < l_len and n < r_len):
        if(left[m] < right[n]):
            array[m+n] = left[m]
            m += 1
        else:
            array[m+n] = right[n]
            n += 1
    
    while(m < l_len):
        array[m+n] = left[m]
        m += 1

    while(n < r_len):
        array[m+n] = right[n]
        n += 1

def _quick_sort(array, start, end):
    if start >= end:
        return
    pivot = array[end]
    i = start
    for j in range(start, end):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i = i + 1
    array[i], array[end] = array[end], array[i]
    _quick_sort(array, start, i-1)
    _quick_sort(array, i+1, end)

def quick_sort(array):
    _quick_sort(array, 0, len(array) - 1)


if __name__ == "__main__":
    def tester(sorting_func):
        result=[]
        for i in range(10,100):
            x=[random.randint(0,100000000) for j in range(0,i)]
            start_time = timer()
            sorting_func(x)
            run_time = timer() - start_time
            result.append((i,run_time))
        return result

    b_sort = tester(bubble_sort)
    s_sort = tester(selection_sort)
    m_sort = tester(merge_sort)
    q_sort = tester(quick_sort)

    x_axis = [d[0] for d in b_sort]
    y1_axis = [d[1] for d in b_sort]
    y2_axis = [d[1] for d in s_sort]
    y3_axis = [d[1] for d in m_sort]
    y4_axis = [d[1] for d in q_sort]

    plt.plot(x_axis,y1_axis,label = "Bubble sort")
    plt.plot(x_axis,y2_axis,label = "Selection sort")
    plt.plot(x_axis,y3_axis,label = "Merge sort")
    plt.plot(x_axis,y4_axis,label = "Quick sort")

    plt.xlabel("Array size")
    plt.ylabel("Time Elapsed(seconds)")
    plt.title('Algorithm Performance')

    plt.legend()
    plt.show()
