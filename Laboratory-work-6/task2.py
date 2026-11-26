INF = float("inf")
V = 8
EDGES = [
    (1, 3, 7), (1, 4, 3), (1, 6, 6),
    (2, 3, 2), (2, 4, 9), (2, 6, 9),
    (3, 8, 4), (4, 5, 5), (5, 6, 4),
    (5, 7, 1), (6, 7, 8), (6, 8, 7),
    (7, 8, 5),
]


def build_weights(n, edges):
    w = [[INF] * n for _ in range(n)]
    for i in range(n):
        w[i][i] = 0
    for u, v, weight in edges:
        w[u - 1][v - 1] = weight
        w[v - 1][u - 1] = weight
    return w


def print_matrix(title, d):
    print(title)
    for row in d:
        print(" ".join(f"{'∞' if x == INF else x:>3}" for x in row))


def floyd(w):
    n = len(w)
    d = [row[:] for row in w]
    comparisons = 0
    updates = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                comparisons += 1
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    updates += 1
        print_matrix(f"D({k + 1}):", d)
    return d, comparisons, updates


weights = build_weights(V, EDGES)
print_matrix("D(0) = W:", weights)
dist, comps, upds = floyd(weights)
print("Загальна кількість порівнянь:", comps)
print("Загальна кількість оновлень:", upds)
