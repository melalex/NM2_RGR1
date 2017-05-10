import numpy as np
import itertools
import math


def __vector_orthogonalization(vec, basis):
    return vec - np.sum((np.dot((vec * ep).sum(), ep) for ep in basis))


def next_eigen_pair(matrix, eigen_pairs, eps, l):
    dimension = len(matrix)
    y = np.array([[1.] for _ in range(dimension)])
    y = __vector_orthogonalization(y, (x[1] for x in eigen_pairs))
    s = (y * y).sum()
    p = math.sqrt(s)
    z_next = y / p
    lambda_ = 0.

    for k in itertools.count(1):
        z_prev = z_next
        y = np.dot(matrix, y)
        s = (y * y).sum()
        t = (y * z_prev).sum()
        p = math.sqrt(s)
        z_next = y / p

        lambda_ = s / t

        if k % l == 0:
            z_next = __vector_orthogonalization(z_next, (x[1] for x in eigen_pairs))

        print('k=', k)
        print('y=', y)
        print('s=', s)
        print('t=', t)
        print('p=', p)
        print('z_n=', z_next)
        print('z_p=', z_prev)
        print('lambda=', lambda_, '\n')

        if np.linalg.norm(np.subtract(z_next, z_prev)) <= eps:
            break

    return lambda_, z_next
