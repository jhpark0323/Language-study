import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, c = map(int, input().split())
    graph[v].append([c, u])

interview = list(map(int, input().split()))

path = [int(1e11)] * (n+1)

def dijkstra():
    pq = []
    for i in interview:
        heappush(pq, (0, i))
        path[i] = 0

    while pq:
        weight, now = heappop(pq)

        if path[now] < weight:
            continue

        for dij in graph[now]:
            nxtWeight = weight + dij[0]
            nxt = dij[1]

            if path[nxt] < nxtWeight:
                continue
            heappush(pq, (nxtWeight, nxt))
            path[nxt] = nxtWeight

dijkstra()
ans = 0
ans_city = 0

for i in range(1, n+1):
    if ans_city < path[i] and path[i] != int(1e11):
        ans_city = path[i]
        ans = i
print(ans)
print(ans_city)