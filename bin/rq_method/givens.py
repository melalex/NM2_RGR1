import numpy as np

from math import hypot


def givens_rq(a):
    n, m = np.shape(a)

    q = np.identity(n)
    r = np.copy(a)

    rows, cols = np.tril_indices(n, -1, m)
    for row, col in zip(rows, cols):
        if r[row, col] != 0:
            g = givens_rotation_matrix(r, row, col)

            r = np.dot(g, r)
            q = np.dot(q, g.T)

    return q, r


def givens_rotation_matrix(matrix, row, col):
    a = matrix[col, col]
    b = matrix[row, col]
    n = len(matrix)

    r = hypot(a, b)
    c = a / r
    s = -b / r

    g = np.identity(n)
    g[[col, row], [col, row]] = c
    g[row, col] = s
    g[col, row] = -s

    return g
