from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np

def Strassen(A, B):
    if len(A) == 1:
        return A*B
    
    if len(A)% 2 != 0:
        A = np.pad(A, ((0, 1), (0, 1)), mode='constant')
        B = np.pad(B, ((0, 1), (0, 1)), mode='constant')

    A11, A12, A21, A22 = Split(A)
    B11, B12, B21, B22 = Split(B)
    
    P = Strassen((A11 + A22), (B11 + B22))
    Q = Strassen((A11 + A12), B22)
    R = Strassen((A22 + A21), B11)
    S = Strassen(A22, (B21 - B11))
    T = Strassen(A11, (B12 - B22))
    U = Strassen((A12 - A22), (B22 + B21))
    V = Strassen((A21 - A11), (B11 + B12))

    C11 = P-Q+S+U
    C12 = Q + T
    C21 = R + S
    C22 = P-R+T+V    
    return np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))


def Split(M):
    if len(M)%2 != 0:
        return
    mid = len(M)//2

    return M[:mid, :mid], M[:mid, mid:], M[mid:, :mid], M[mid:, mid:]

def Multiplication(A, B):
    n = len(A)
    C = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == "__main__":
    def generate_random_matrix(n):
        return np.random.randint(0, 10, size = (n, n))

    x, y1, y2 = [], [], []

    for i in range(2, 9):
        A = generate_random_matrix(i)
        B = generate_random_matrix(i)

        x.append(i)
        
        start_time = timer()
        C = Strassen(A, B)
        end_time = timer() - start_time
        y1.append(end_time)

        start_time = timer()
        D = Multiplication(A, B)
        end_time = timer() - start_time
        y2.append(end_time)

    bar_width = 0.35

    r1 = range(len(x))
    r2 = [x + bar_width for x in r1]

    plt.bar(r1, y1, color='b', width=bar_width, edgecolor='grey', label='Strassen')
    plt.bar(r2, y2, color='r', width=bar_width, edgecolor='grey', label='Naive')

    plt.xlabel('X')
    plt.ylabel('Values')
    plt.xticks([r + bar_width/2 for r in range(len(x))], x)

    plt.legend()
    plt.show()
