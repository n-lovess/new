import numpy as np

def gram_schmidt_qr(A):
    n, m = A.shape
    if n != m:
        raise ValueError(f"the matrix A is not square, {A.shape=}")

    Q = np.empty_like(A)
    R = np.zeros_like(A)

    for j in range(n):
        u = A[:, j].copy()

        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            u -= R[i, j] * Q[:, i]

        R[j, j] = np.linalg.norm(u)
        Q[:, j] = u / R[j, j]

    return Q, R

def toupper(R):
    return np.triu(R)

eps_list = [1e-6, 1e-7, 1e-8, 1e-10, 1e-12, 1e-14, 1e-16]

print(f"{'eps':>12}  {'error1':>12}  {'error2':>12}  {'error3':>12}")

for eps in eps_list:
    A = np.array([[1, 1 + eps],
                  [1 + eps, 1]], dtype=float)

    Q, R = gram_schmidt_qr(A)

    error1 = np.linalg.norm(A - Q @ R, 2)
    error2 = np.linalg.norm(Q.T @ Q - np.eye(2), 2)
    error3 = np.linalg.norm(R - toupper(R), 2)

    print(f"{eps:12.1e}  {error1:12.3e}  {error2:12.3e}  {error3:12.3e}")
