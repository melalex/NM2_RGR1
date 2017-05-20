import numpy as np
from bin.power_method.max_eigen_pair import max_eigen_pair


def min_eigen_pair(matrix, eps, p, delta):
    b = np.linalg.inv(matrix)
    ep = max_eigen_pair(b, eps, p, delta)
    ev = ep[1]
    kev = np.dot(matrix, ev)
    return kev[0] / ev[0], ev, ep[2]
