from heapq import heappush, heappop

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    # 양방향 길 append
    graph[a].append([c, b])
    graph[b].append([c, a])
# print(graph)
u, v = map(int, input().split())

# 어디서 시작하는지가 중요
def dijkstra(start):
    distance = [float('inf')] * (n+1)
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
                heappush(pq, [next_dist, next_])

    return distance

start_from_1 = dijkstra(1)
start_from_u = dijkstra(u)
start_from_v = dijkstra(v)

ver_1 = start_from_1[u] + start_from_u[v] + start_from_v[n]
ver_2 = start_from_1[v] + start_from_v[u] + start_from_u[n]

ans = min(ver_1, ver_2)

if ans == float('inf'):
    print(-1)
else:
    print(ans)