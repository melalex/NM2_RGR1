import numpy as np


def pivot_matrix(m):
    n = len(m)

    id_mat = [[float(i == j) for i in range(n)] for j in range(n)]

    for j in range(n):
        row = max(range(j, n), key=lambda i: abs(m[i][j]))
        if j != row:
            id_mat[j], id_mat[row] = id_mat[row], id_mat[j]

    return id_mat


def decomposition(a):
    n = len(a)

    l = [[0.0] * n for _ in range(n)]
    u = [[0.0] * n for _ in range(n)]

    p = pivot_matrix(a)
    p_a = np.dot(p, a)

    for j in range(n):
        l[j][j] = 1.0

        for i in range(j + 1):
            s1 = sum(u[k][j] * l[i][k] for k in range(i))
            u[i][j] = p_a[i][j] - s1

        for i in range(j, n):
            s2 = sum(u[k][j] * l[i][k] for k in range(j))
            l[i][j] = (p_a[i][j] - s2) / u[j][j]

    return l, u
