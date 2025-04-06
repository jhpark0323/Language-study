import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    visited = [False] * (n+1)
    visited[start] = True
    q = deque([start])
    max_cnt = 0
    while q:
        now = q.popleft()

        max_cnt += 1

        for nxt in graph[now]:
            if visited[nxt]:
                continue
            visited[nxt] = True
            q.append(nxt)

    return max_cnt

ans = []
total = 0
for i in range(1, n+1):
    new_cnt = bfs(i)
    if new_cnt == total:
        ans.append(i)
        total = new_cnt
    elif new_cnt > total:
        ans = [i]
        total = new_cnt

print(*ans)