import numpy as np

def lu_factorisation(A):
    """
    Compute the LU factorisation of a square matrix A such that A = L U
    """
    A = A.astype(float)
    n = A.shape[0]
    L = np.zeros_like(A)
    U = np.zeros_like(A)

    for i in range(n):
        # upper triangle
        for j in range(i, n):
            sum_val = sum(L[i, k] * U[k, j] for k in range(i))
            U[i, j] = A[i, j] - sum_val

        L[i, i] = 1.0

        for j in range(i + 1, n):
            sum_val = sum(L[j, k] * U[k, i] for k in range(i))
            L[j, i] = (A[j, i] - sum_val) / U[i, i]

    return L, U