import numpy as np

from bin.power_method.second_max_pair import second_max_pair


def second_min_pair(matrix, min_pair, eps, delta):
    b = np.linalg.inv(matrix)
    ev = second_max_pair(b, min_pair, eps, delta)[1]
    kev = np.dot(matrix, ev)
    return kev[0] / ev[0], ev
