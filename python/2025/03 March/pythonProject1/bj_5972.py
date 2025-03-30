import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])
# print(graph)
path = [int(1e9)] * (n+1)

def dijkstra():
    path[1] = 0
    pq = []
    # 0 : weight, 1 : start
    heappush(pq, [0, 1])

    while pq:
        weight, now = heappop(pq)

        # weight가 현재 길이보다 크면 볼 필요도 없음
        if path[now] < weight:
            continue

        for neighbor in graph[now]:
            nxtWeight = weight + neighbor[0]
            nxtPath = neighbor[1]

            if nxtWeight >= path[nxtPath]:
                continue
            path[nxtPath] = nxtWeight
            heappush(pq, [nxtWeight, nxtPath])

dijkstra()
print(path[n])