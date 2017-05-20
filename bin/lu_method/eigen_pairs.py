import itertools
import numpy as np
from scipy import linalg as ln


def eigen_pairs(matrix, eps):
    a = np.array(matrix)
    k = 0

    for k in itertools.count(1):
        l, u = ln.lu(a, True)
        a = np.dot(u, l)

        if np.linalg.norm(np.tril(a, -1)) <= eps:
            break

    return a.diagonal(), [], k
