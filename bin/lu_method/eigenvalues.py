import itertools
import numpy as np

from bin.lu.decompose import decomposition


def eigenvalues(matrix, eps):
    a = np.array(matrix)

    for k in itertools.count(1):
        l, u = decomposition(a)
        a = np.dot(u, l)

        if np.linalg.norm(np.tril(a, -1)) <= eps:
            break

    return a.diagonal()
