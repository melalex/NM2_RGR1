import numpy as np
import itertools


def max_eigen_pair(matrix, eps, p, q, delta):
    dimension = len(matrix)
    y = np.ones(dimension).reshape(dimension, 1)

    u_next = np.full(dimension, 9.)
    u_prev = np.full(dimension, 9.)
    u_prev_prev = None

    z_next = y / np.linalg.norm(y)
    z_prev = np.copy(z_next)

    s = [i for i in range(dimension)]
    k = 0

    for k in itertools.count(1):
        z_prev_prev = z_prev
        z_prev = z_next
        u_prev_prev = u_prev
        u_prev = np.copy(u_next)
        y = np.dot(matrix, z_prev)
        s_prev = s
        s = [index for index, value in enumerate(z_prev) if value > delta]
        s_inter = list(set(s_prev) & set(s))

        u_next = y / z_prev
        z_next = y

        if k % p == 0:
            z_next = z_next / np.linalg.norm(z_next)

        if k % q == 0:
            z_next = z_prev_prev - np.square(z_prev - z_prev_prev) / (z_next - 2 * z_prev + z_prev_prev)

        if (np.absolute(u_next[s_inter] - u_prev[s_inter]) <= eps).all():
            break

    u = u_prev_prev - np.square(u_prev - u_prev_prev) / (u_next - 2 * u_prev + u_prev_prev)

    return (np.sum(u[s])) / len(s), z_next / np.linalg.norm(z_next), k
