from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt

def linear_search(array, x):
    for i in range(0, len(array)):
        if array[i] == x:
            return i
    
def _binary_search(array, x, start, end):
    mid = (start+end)//2
    if x == array[mid]:
        return mid
    elif x < array[mid]:
        return _binary_search(array, x, start, mid - 1)
    else:
        return _binary_search(array, x, mid + 1, end)
    
def binary_search(array, x):
    return _binary_search(array, x, 0, len(array) - 1)

if __name__ == "__main__":
    def tester(searching_func):
        result=[]

        for i in range(10,100):

            end = i
            array = [j for j in range(0, end)]

            start_time = timer()
            searching_func(array, random.randint(0, end - 1))
            run_time = timer() - start_time
            result.append((i,run_time))

        return result

    l_search = tester(linear_search)
    b_search = tester(binary_search)

    x_axis = [d[0] for d in l_search]
    y1_axis = [d[1] for d in l_search]
    y2_axis = [d[1] for d in b_search]

    plt.plot(x_axis,y1_axis,label = "Linear Search")
    plt.plot(x_axis,y2_axis,label = "Binary Search")

    plt.ylabel("Time Elapsed(seconds)")
    plt.title('Algorithm Performance')

    plt.legend()
    plt.show()

