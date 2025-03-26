from heapq import heappop, heappush

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])
# print(graph)

INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (n+1)
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

            if distance[next_] > next_dist:
                distance[next_] = next_dist
                prev[next_] = now
                heappush(pq, [next_dist, next_])


for start in range(1, n+1):
    prev = [0] * (n+1)
    dijkstra(start)

    for end in range(1, n+1):
        current = end
        path = []
        while current:
            path.append(current)
            current = prev[current]
        path = path[::-1]
        # print(path)

        if len(path) == 1:
            print("-", end=" ")

        else:
            print(path[1], end=" ")

    print()