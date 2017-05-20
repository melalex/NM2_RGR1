import numpy as np

from bin.power_method.max_eigen_pair import max_eigen_pair
from bin.power_method.second_max_pair import second_max_pair


def second_min_pair(matrix, min_pair, eps, delta):
    u, v, k = min_pair
    b = np.linalg.inv(matrix)
    b = b - u * np.dot(v, np.transpose(v))
    return max_eigen_pair(b, eps, 3, delta)
