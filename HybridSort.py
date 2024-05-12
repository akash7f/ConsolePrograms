from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt

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


def _hybrid_sort(array, start, end):
    if start >= end:
        return

    if end - start <10:
        for i in range(start + 1, end + 1):
            key = array[i]
            j = i - 1
            while j >= start and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
    else:
        pivot = array[end]
        i = start
        for j in range(start, end):
            if array[j] <= pivot:
                array[i], array[j] = array[j], array[i]
                i = i + 1
        array[i], array[end] = array[end], array[i]
        _hybrid_sort(array, start, i-1)
        _hybrid_sort(array, i+1, end)

def hybrid_sort(array):
    _hybrid_sort(array, 0, len(array)-1)

if __name__ == "__main__":
    def tester(sorting_func):
        result=[]
        for i in range(10,200):
            x=[random.randint(0,10000) for j in range(0,i)]
            start_time = timer()
            sorting_func(x)
            run_time = timer() - start_time
            result.append((i,run_time))
        return result

    q_sort = tester(quick_sort)
    h_sort = tester(hybrid_sort)

    x_axis = [d[0] for d in q_sort]
    y1_axis = [d[1] for d in q_sort]
    y2_axis = [d[1] for d in h_sort]

    plt.plot(x_axis,y1_axis,label = "Quick sort")
    plt.plot(x_axis,y2_axis,label = "Hybri sort")

    plt.xlabel("Array size")
    plt.ylabel("Time Elapsed(seconds)")
    plt.title('Algorithm Performance')

    plt.legend()
    plt.show()
