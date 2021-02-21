import heapq

n, m, x, y = map(int, input().split())

train = [[] for _ in range(n)]
for _ in range(m):
    a, b, t, k = map(int, input().split())
    train[a - 1].append((b - 1, t, k))
    train[b - 1].append((a - 1, t, k))


def dijkstra(s):
    d = [float("inf")] * n
    d[s] = 0
    hq = [(0, s)]
    visit = [False] * n
    while hq:
        di, i = heapq.heappop(hq)
        visit[i] = True
        if d[i] < di:
            continue
        for j, t, k in train[i]:
            if visit[j]:
                continue
            dj = -(-di // k) * k + t
            if dj < d[j]:
                d[j] = dj
                heapq.heappush(hq, (dj, j))
    return d


ans = dijkstra(x - 1)[y - 1]
print(ans if ans < float("inf") else -1)
