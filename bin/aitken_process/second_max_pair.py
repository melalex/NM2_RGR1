import numpy as np
import itertools
import math


def __get_initial_y(x, eps):
    y = np.array([[5.] for _ in range(len(x))])
    while np.linalg.norm(np.subtract(y, x)) <= eps:
        y *= 2

    return y


def second_max_pair(matrix, first_pair, eps, q, delta):
    y_next = __get_initial_y(first_pair[1], eps)
    y_prev = np.copy(y_next)

    lambda_1 = first_pair[0]
    lambda_next = np.array([[1.] for _ in range(len(first_pair[1]))])
    lambda_prev = np.copy(lambda_next)

    s = [i for i in range(len(matrix))]
    k = 0

    for k in itertools.count(1):
        lambda_prev_prev = lambda_prev
        lambda_prev = np.copy(lambda_next)

        y_prev_prev = y_prev
        y_prev = y_next
        y_next = np.dot(matrix, y_prev)

        s_prev = s
        s = [i for i, v in enumerate(y_next) if math.fabs(y_prev.item(i) - lambda_1 * y_prev_prev.item(i)) > delta]
        s_inter = list(set(s_prev) & set(s))

        for i in s:
            lambda_next[i] = (y_next.item(i) - lambda_1 * y_prev.item(i)) / \
                             (y_prev.item(i) - lambda_1 * y_prev_prev.item(i))

        if k % q == 0:
            y_next = y_prev_prev - np.square(y_prev - y_prev_prev) / (y_next - 2 * y_prev + y_prev_prev)

        if k > 5 and ((lambda_next[s_inter] < 0).all() or (lambda_next[s_inter] > 0).all()):
            delta_1 = np.abs(lambda_next[s_inter] - lambda_prev[s_inter])
            delta_2 = np.abs(lambda_prev[s_inter] - lambda_prev_prev[s_inter])
            if (delta_1 > delta_2).all():
                lambda_next = lambda_prev
                y_next = y_prev
                y_prev = y_prev_prev
                break

        if (np.absolute(lambda_next[s_inter] - lambda_prev[s_inter]) <= eps).all():
            break

    z = y_next - lambda_1 * y_prev

    return (np.sum(lambda_next[s])) / len(s), z / np.linalg.norm(z), k
