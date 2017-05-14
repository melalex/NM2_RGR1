import numpy as np


def zeroing_givens_coefficients(x, z):
    if z == 0.0:
        return 1.0, 0.0
    r = np.hypot(x, z)
    return x / r, -z / r


def givens_rotation(coefficients, a, r1, r2):
    c, s = coefficients
    givens = np.array([[c, -s],
                       [s, c]])

    a[[r1, r2], :] = np.dot(givens, a[[r1, r2], :])


# def givens_rotation(matrix, i, j):
#     n = len(matrix)
#
#     c = matrix[i][i] / math.sqrt(matrix[i][i] * matrix[i][i] + matrix[i][j] * matrix[i][j])
#     s = matrix[i][j] / math.sqrt(matrix[i][i] * matrix[i][i] + matrix[i][j] * matrix[i][j])
#
#     g = np.identity(n)
#
#     g[i][i] = c
#     g[i][j] = -s
#     g[j][i] = s
#     g[j][j] = c
#
#
#     return g.dot(matrix)
