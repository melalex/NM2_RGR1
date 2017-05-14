import numpy as np

from scipy import linalg as ln


def eigen_pairs(matrix, eps):
    b = np.array(ln.hessenberg(matrix))
    p = np.identity(len(matrix))

    while True:
        b_prev = b
        q, r = np.linalg.qr(b)
        p = p.dot(q)
        b = r.dot(q)

        if (np.diagonal(b) - np.diagonal(b_prev) <= eps).all():
            break

    return np.diagonal(b), p
