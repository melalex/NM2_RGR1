import numpy as np


def inverse_iteration(matrix, eps):
    dimension = len(matrix)
    y = np.ones(dimension).reshape(dimension, 1)
    u = 1

    z = y / np.linalg.norm(y)

    np.lu

    return
