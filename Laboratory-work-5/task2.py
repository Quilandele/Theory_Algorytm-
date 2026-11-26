import heapq

V = 8
EDGES = [
    (1, 3, 7), (1, 4, 3), (1, 6, 6),
    (2, 3, 2), (2, 4, 9), (2, 6, 9),
    (3, 8, 4), (4, 5, 5), (5, 6, 4),
    (5, 7, 1), (6, 7, 8), (6, 8, 7),
    (7, 8, 5),
]


def build_lists(n, edges):
    lists = {v: [] for v in range(1, n + 1)}
    for u, v, w in edges:
        lists[u].append((v, w))
        lists[v].append((u, w))
    for v in lists:
        lists[v].sort()
    return lists


def prim(n, lists, start):
    tree_vertices = [start]
    in_tree = {start}
    tree_edges = []
    queue = []
    pushed = 0
    skipped = 0

    for v, w in lists[start]:
        heapq.heappush(queue, (w, start, v))
        pushed += 1
    print(f"Початок: VT = {tree_vertices}, E = {sorted(queue)}")

    while len(tree_edges) < n - 1:
        w, u, v = heapq.heappop(queue)
        if v in in_tree:
            print(f"  Ребро ({u}, {v}) = {w} пропускаємо: утворює цикл")
            skipped += 1
            continue
        tree_vertices.append(v)
        in_tree.add(v)
        tree_edges.append((u, v, w))
        for x, wx in lists[v]:
            if x not in in_tree:
                heapq.heappush(queue, (wx, v, x))
                pushed += 1
        print(f"Додаємо ребро ({u}, {v}) = {w}, VT = {tree_vertices}")
        print(f"  E = {sorted(queue)}")

    return tree_edges, pushed, skipped


edges, pushed, skipped = prim(V, build_lists(V, EDGES), 1)
print("Ребра МКД (алгоритм Пріма):")
for u, v, w in edges:
    print(f"{u} - {v} : {w}")
print("Вага МКД:", sum(w for u, v, w in edges))
print("Додано ребер у чергу:", pushed)
print("Вилучено з черги:", len(edges) + skipped, "з них пропущено:", skipped)
