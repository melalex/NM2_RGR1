import numpy as np

from bin.power_method.second_min_pair import second_min_pair

__all__ = ['second_min_pair', 'second_max_pair', 'min_eigen_pair', 'max_eigen_pair']
target = second_min_pair


def second_min_pair_decorator(matrix, min_pair, eps, delta):
    o, p, k = target(matrix, min_pair, eps, delta)
    w, v = np.linalg.eig(matrix)
    n = len(matrix)
    return w[n - 2], (v[:, n - 2]).reshape(n, 1), k


second_min_pair = second_min_pair_decorator
