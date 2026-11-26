V = 8
EDGES = [
    (1, 3, 7), (1, 4, 3), (1, 6, 6),
    (2, 3, 2), (2, 4, 9), (2, 6, 9),
    (3, 8, 4), (4, 5, 5), (5, 6, 4),
    (5, 7, 1), (6, 7, 8), (6, 8, 7),
    (7, 8, 5),
]

parent = list(range(V + 1))
rank = [0] * (V + 1)


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(a, b):
    if rank[a] < rank[b]:
        a, b = b, a
    parent[b] = a
    if rank[a] == rank[b]:
        rank[a] += 1


def kruskal(n, edges):
    tree_edges = []
    examined = 0
    ordered = sorted(edges, key=lambda e: (e[2], e[0], e[1]))
    print("Відсортовані ребра:", [f"{u}-{v}={w}" for u, v, w in ordered])
    for u, v, w in ordered:
        if len(tree_edges) == n - 1:
            break
        examined += 1
        a = find(u)
        b = find(v)
        if a == b:
            print(f"Ребро ({u}, {v}) = {w}: FIND({u}) = FIND({v}) = {a}, цикл, пропускаємо")
            continue
        union(a, b)
        tree_edges.append((u, v, w))
        print(f"Ребро ({u}, {v}) = {w}: FIND({u}) = {a}, FIND({v}) = {b}, додаємо")
    return tree_edges, examined


edges, examined = kruskal(V, EDGES)
print("Ребра МКД (алгоритм Крускала):")
for u, v, w in edges:
    print(f"{u} - {v} : {w}")
print("Вага МКД:", sum(w for u, v, w in edges))
print("Переглянуто ребер:", examined, "з", len(EDGES))
