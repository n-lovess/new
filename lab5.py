import numpy as np

def classical_gs(A):

    a1 = A[:, 0]
    a2 = A[:, 1]

    q1 = a1 / np.linalg.norm(a1)

    r12 = np.dot(q1, a2)
    u2 = a2 - r12 * q1

    q2 = u2 / np.linalg.norm(u2)

    Q = np.column_stack((q1, q2))
    R = Q.T @ A
    return Q, R

def toupper(R):
    return np.triu(R)

eps_list = [1e-6, 1e-7, 1e-8, 1e-10, 1e-12, 1e-14, 1e-16]

print(f"{'eps':>12}  {'error1':>12}  {'error2':>12}  {'error3':>12}")

for eps in eps_list:
    A = np.array([[1, 1 + eps], [1 + eps, 1]], dtype=float)
    Q, R = classical_gs(A)

    error1 = np.linalg.norm(A - Q @ R, 2)
    error2 = np.linalg.norm(Q.T @ Q - np.eye(2), 2)
    error3 = np.linalg.norm(R - toupper(R), 2)

    print(f"{eps:12.1e}  {error1:12.3e}  {error2:12.3e}  {error3:12.3e}")
