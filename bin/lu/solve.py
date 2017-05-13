def solve(l, u, b):
    n = len(b)
    y = [[0.] for _ in range(n)]
    x = [[0.] for _ in range(n)]

    for i in range(n):
        y[i][0] = b[i][0] - sum([l[i][j] * y[j][0] for j in range(i)])

    for i in range(n - 1, -1, -1):
        x[i][0] = y[i][0] - sum((u[i][j] * x[j][0] for j in range(i + 1, n)))
        x[i][0] /= u[i][i]

    return x
