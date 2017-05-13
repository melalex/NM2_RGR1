import numpy as np
import itertools
import math

from bin.lu.decompose import decomposition
from bin.lu.solve import solve


def mix_eigen_pair(matrix, eps):
    dimension = len(matrix)
    y = np.ones(dimension).reshape(dimension, 1)
    lambda_next = 1

    z_next = y / np.linalg.norm(y)

    l, u = decomposition(matrix)

    for k in itertools.count(1):
        z_prev = z_next
        lambda_prev = lambda_next
        y = solve(l, u, z_prev)

        lambda_next = np.sum(y * z_prev) / np.sum(z_prev * z_prev)
        z_next = y / np.linalg.norm(y)

        # print('======#', k, '======')
        # print('u =', lambda_next)
        # print('z =', z_next, '\n')

        if math.fabs(lambda_next - lambda_prev) <= eps:
            break

    return 1 / lambda_next, z_next
