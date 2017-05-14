import numpy as np

from bin.lu.decompose import decomposition


def eigen_pairs(matrix, eps):
    a = np.array(matrix)
    p = np.identity(len(matrix))

    while True:
        l, u = decomposition(a)
        p = np.dot(p, l)
        a = np.dot(u, l)

        if np.linalg.norm(np.tril(a, -1)) <= eps:
            break

    return a.diagonal()