from heapq import heappop, heappush
from collections import deque

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    start, end = map(int, input().split())
    graph = [[] for _ in range(n)]
    graph_inv = [[] for _ in range(n)]
    edges = [[False] * n for _ in range(n)]
    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([c, b])
        graph_inv[b].append([c, a])
    # print(graph)
    INF = int(1e9)

    def dijkstra(start):
        distance = [INF] * n
        distance[start] = 0
        pq = []
        heappush(pq, [0, start])

        while pq:
            dist, now = heappop(pq)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                next_dist = i[0] + dist
                next_ = i[1]

                # 만약 기록된거면 넘겨주는건가?
                if edges[now][next_]:
                    continue

                if distance[next_] > next_dist:
                    distance[next_] = next_dist
                    heappush(pq, [next_dist, next_])
        return distance

    def bfs():
        q = deque([end])

        while q:
            now = q.popleft()

            if now == start:
                continue

            for i in graph_inv[now]:
                prev_ = i[1]
                prev_dist = i[0] + distance[prev_]

                if prev_dist == distance[now] and not edges[prev_][now]:
                    edges[prev_][now] = True
                    q.append(prev_)


    distance = dijkstra(start)
    # print('distance : ', distance)
    bfs()
    distance = dijkstra(start)

    if distance[end] == INF:
        print(-1)

    else:
        print(distance[end])