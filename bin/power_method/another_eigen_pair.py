import numpy as np
import itertools


def another_eigen_pair(matrix, eigen_pairs, eps, delta, l):
    dimension = len(matrix)
    y = np.ones(dimension)

    return np.dot(y, np.reshape(eigen_pairs[0][1], dimension))
