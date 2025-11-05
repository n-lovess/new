import numpy as np
import time
import matplotlib.pyplot as plt
from lu_factorisation import lu_factorisation
from scipy.sparse import diags

def generate_safe_system(n):
    k = [np.ones(n - 1), -2 * np.ones(n), np.ones(n - 1)]
    offset = [-1, 0, 1]
    A = diags(k, offset).toarray()
    x_true = np.ones((n, 1))
    b = A @ x_true
    return A, b, x_true

def gaussian_elimination(A, b):
    A = A.copy().astype(float)
    b = b.copy().astype(float)
    n = len(b)
    for i in range(n):
        for j in range(i+1, n):
            factor = A[j,i] / A[i,i]
            A[j,i:] -= factor * A[i,i:]
            b[j] -= factor * b[i]
    x = np.zeros_like(b)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i,i+1:], x[i+1:])) / A[i,i]
    return x

sizes = [2**j for j in range(1,6)]
times_lu = []
times_gauss = []

for n in sizes:
    A, b, x = generate_safe_system(n)
    start = time.perf_counter()
    lu_factorisation(A)
    times_lu.append(time.perf_counter() - start)
    start = time.perf_counter()
    gaussian_elimination(A, b)
    times_gauss.append(time.perf_counter() - start)

plt.plot(sizes, times_lu, marker='o', label='LU factorisation')
plt.plot(sizes, times_gauss, marker='o', label='Gaussian elimination')
plt.xlabel('Matrix size n')
plt.ylabel('Runtime (seconds)')
plt.title('Runtime comparison of LU vs Gaussian elimination')
plt.legend()
plt.grid(True)
plt.savefig('runtime_plot.png', dpi=300)
plt.show()