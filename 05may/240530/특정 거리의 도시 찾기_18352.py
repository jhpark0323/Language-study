import sys
from collections import deque

input = sys.stdin.readline

def bfs(start_city):
    visited = [False] * (n+1)
    visited[start_city] = True
    q = deque([[start_city, 0]])
    dist = []

    while q:
        now, distance = q.popleft()

        if distance == k:
            dist.append(now)
            continue

        for next_city in graph[now]:
            if not visited[next_city]:
                visited[next_city] = True
                q.append([next_city, distance + 1])

    return dist

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
# print(graph)
for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
# print(graph)

dist = bfs(x)

if dist:
    dist.sort()
    for j in dist:
        print(j)
else:
    print(-1)