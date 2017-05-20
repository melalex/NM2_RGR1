import math
import itertools
import numpy as np


def max_eigen_pair(matrix, eps):
    dimension = len(matrix)
    y = np.ones(dimension).reshape(dimension, 1)
    lambda_next = 1
    k = 0

    z_next = y / np.linalg.norm(y)

    for k in itertools.count(1):
        z_prev = z_next
        lambda_prev = lambda_next
        y = np.dot(matrix, z_prev)

        lambda_next = np.sum(y * z_prev) / np.sum(z_prev * z_prev)
        z_next = y / np.linalg.norm(y)

        if math.fabs(lambda_next - lambda_prev) <= eps:
            break

    return lambda_next, z_next * -1, k
