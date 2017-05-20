import math
import itertools
import numpy as np


def __iter_process(matrix, eps):
    n = len(matrix)
    b = np.array(matrix)
    t_array = []

    for k in itertools.count(1):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                p = 2 * b[i][j]
                q = b[i][i] - b[j][j]
                d = math.sqrt(p * p + q * q)
                r = math.fabs(q) / (2 * d)
                c = math.sqrt(0.5 + r)
                s = np.sign(p * q) * math.sqrt(0.5 - r)

                t = np.identity(n)
                t_array.append(t)

                t[i][i] = c
                t[i][j] = -s
                t[j][i] = s
                t[j][j] = c

                b = t.transpose().dot(b).dot(t)

                v = b.copy()
                np.fill_diagonal(v, 0)

                if np.linalg.norm(v, ord='fro') <= eps:
                    return b, t_array, k


def eigen_pairs(matrix, eps):
    n = len(matrix)
    b, t_array, k = __iter_process(matrix, eps)
    x = np.identity(n)

    for t in t_array:
        x = np.dot(x, t)

    return np.diagonal(b), x * -1, k
