import math
import itertools
import numpy as np


def __orthogonalization(vec, pairs):
    return vec - np.sum((sum(x * vec) * x for x in (ev[1] for ev in pairs)))


def next_pair(matrix, pairs, l, eps):
    y = np.array([[1] for _ in range(len(pairs[0][1]))])
    y = __orthogonalization(y, pairs)
    lambda_next = 1
    k = 0

    z = y / np.linalg.norm(y)

    for k in itertools.count(1):
        lambda_prev = lambda_next

        y = np.dot(matrix, z)

        lambda_next = np.sum(y * z) / np.sum(z * z)
        z = y / np.linalg.norm(y)

        if k % l:
            z = __orthogonalization(z, pairs)

        if math.fabs(lambda_next - lambda_prev) <= eps:
            break

    return lambda_next, z * -1, k
