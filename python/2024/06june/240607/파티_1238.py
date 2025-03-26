from heapq import heappush, heappop

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, t = map(int, input().split())
    graph[a].append([t, b])
# print(graph)

def dijkstra(start, end):
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    pq = []
    # 첫 시작시 소요 거리, 위치
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

    # print(distance)
    return distance[end]

ans = 0
for stu in range(1, n+1):
    new_ans = dijkstra(stu, x) + dijkstra(x, stu)

    if ans < new_ans:
        ans = new_ans

print(ans)