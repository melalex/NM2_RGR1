import itertools
import numpy as np


def eigen_pairs(matrix, eps):
    n = len(matrix)
    b = np.array(matrix)
    p = np.identity(n)
    k = 0

    rows, cols = np.tril_indices(n, -2, n)
    for row, col in zip(rows, cols):
        if b[row, col] != 0:
            g = givens_rotation_matrix(b, row, col)
            b = g.transpose().dot(b).dot(g)

    for k in itertools.count(1):
        b_prev = b
        q, r = givens_rq(b)
        p = p.dot(q)
        b = r.dot(q)

        if (np.diagonal(b) - np.diagonal(b_prev) <= eps).all():
            break

    return np.diagonal(b), p, k
