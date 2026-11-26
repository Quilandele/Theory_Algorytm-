V = 8
EDGES = [
    (1, 3, 7), (1, 4, 3), (1, 6, 6),
    (2, 3, 2), (2, 4, 9), (2, 6, 9),
    (3, 8, 4), (4, 5, 5), (5, 6, 4),
    (5, 7, 1), (6, 7, 8), (6, 8, 7),
    (7, 8, 5),
]


def build_matrix(n, edges):
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    for u, v, w in edges:
        matrix[u][v] = w
        matrix[v][u] = w
    return matrix


def build_lists(n, edges):
    lists = {v: [] for v in range(1, n + 1)}
    for u, v, w in edges:
        lists[u].append((v, w))
        lists[v].append((u, w))
    for v in lists:
        lists[v].sort()
    return lists


matrix = build_matrix(V, EDGES)
lists = build_lists(V, EDGES)

print("Матриця суміжності:")
print("   " + " ".join(str(v) for v in range(1, V + 1)))
for u in range(1, V + 1):
    print(f"{u}: " + " ".join(str(matrix[u][v]) for v in range(1, V + 1)))

print("Списки суміжності (вершина, вага):")
for u in range(1, V + 1):
    print(f"{u}: " + " -> ".join(f"({v}, {w})" for v, w in lists[u]))
