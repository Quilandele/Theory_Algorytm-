INF = float("inf")
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


def show(x):
    return "∞" if x == INF else str(x)


def extract_min(pq):
    u = min(pq, key=lambda v: (pq[v], v))
    del pq[u]
    return u


def dijkstra(n, lists, s):
    pred = {}
    dist = {}
    pq = {}
    checks = 0
    updates = 0
    for v in range(1, n + 1):
        pred[v] = -1
        dist[v] = 0 if v == s else INF
        pq[v] = dist[v]
    step = 0
    while pq:
        u = extract_min(pq)
        step += 1
        print(f"{step}. u = {u}, dist[{u}] = {dist[u]}")
        for v, w in lists[u]:
            if v not in pq:
                continue
            checks += 1
            new = dist[u] + w
            if dist[v] > new:
                print(f"  v = {v}: {show(dist[v])} > {dist[u]} + {w} = {new} -> оновлюємо")
                dist[v] = new
                pred[v] = u
                pq[v] = new
                updates += 1
            else:
                print(f"  v = {v}: {show(dist[v])} > {dist[u]} + {w} = {new} -> ні")
        print("  dist =", [show(dist[v]) for v in range(1, n + 1)])
        print("  pred =", [pred[v] for v in range(1, n + 1)])
    return pred, dist, checks, updates


def path_to(pred, v):
    path = [v]
    while pred[v] != -1:
        v = pred[v]
        path.append(v)
    return path[::-1]


pred, dist, checks, updates = dijkstra(V, build_lists(V, EDGES), 1)
print("Найкоротші шляхи з вершини 1:")
for v in range(2, V + 1):
    path = " -> ".join(str(x) for x in path_to(pred, v))
    print(f"{v}: {path}, довжина {dist[v]}")
print("Перевірок умови релаксації:", checks)
print("Оновлень dist:", updates)
