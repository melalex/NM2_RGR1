import numpy as np
import itertools


def max_eigen_pair(matrix, eps, p, delta):
    dimension = len(matrix)
    y = np.ones(dimension).reshape(dimension, 1)
    lambda_next = np.full(dimension, 9.)
    z_next = y / np.linalg.norm(y)
    s = []

    for k in itertools.count(1):
        z_prev = z_next
        lambda_prev = np.copy(lambda_next)
        y = np.dot(matrix, z_prev)
        s = [index for index, value in enumerate(z_prev) if value > delta]

        for i in s:
            lambda_next[i] = y.item(i) / z_prev.item(i)

        if k % p == 0:
            z_next = y / np.linalg.norm(y)
        else:
            z_next = y

        if (np.absolute(lambda_next - lambda_prev) <= eps).all():
            break

    return (np.sum(lambda_next[s])) / len(s), z_next / np.linalg.norm(z_next)
