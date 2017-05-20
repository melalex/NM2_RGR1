import numpy as np

from bin.rq_method.eigen_pairs import eigen_pairs

__all__ = ['eigen_pairs']
target = eigen_pairs


def eigen_pairs_decorator(matrix, eps):
    o, p, k = target(matrix, eps)
    w, v = np.linalg.eig(matrix)
    return o, v, k

eigen_pairs = eigen_pairs_decorator
