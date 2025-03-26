from heapq import heappop, heappush

n, m = map(int, input().split())
ls = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    # 마지막은 추가해야하기 때문에 먼저 걸어줌
    if a == n-1 or b == n-1:
        # 넥서스가 아닌데 시야에 보이는 곳이 있으면 continue
        if (a == n-1 and ls[b]) or (b == n-1 and ls[a]):
            continue
        # 아니면 패스
        pass

    # 만약 출발지나 도착지가 시야에 보이면 graph에 추가하지 않음
    elif ls[a] or ls[b]:
        continue

    graph[a].append([c, b])
    graph[b].append([c, a])

INF = float('inf')

def dijkstra():
    distance = [INF] * n
    distance[0] = 0
    pq = []
    heappush(pq, [0, 0])

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

distance = dijkstra()
# print(distance)

if distance[-1] == INF:
    print(-1)
else:
    print(distance[-1])