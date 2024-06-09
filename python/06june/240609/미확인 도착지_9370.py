# float('inf') 쓰니깐 안됨
# int(1e9) 쓰자
# float('inf') + float('inf') = float('inf') 인 경우가 있어서 그런듯

from heapq import heappop, heappush

def dijkstra(start):
    distance = [int(1e9)] * (n+1)
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
                prev_city[next_] = now
                heappush(pq, [next_dist, next_])

    return distance

testcase = int(input())

for _ in range(testcase):
    n, m, t = map(int, input().split())
    start, city1, city2 = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([c, b])
        graph[b].append([c, a])
    # print(graph)
    candidate = [int(input()) for _ in range(t)]

    # 지나온 곳 확인용
    prev_city = [0] * (n+1)
    distance = dijkstra(start)
    distance_1 = dijkstra(city1)
    distance_2 = dijkstra(city2)
    # print('distance: ', distance)
    # print('prev_city: ', prev_city)

    ans = []

    # 목적지 후보들
    for i in range(t):
        end = candidate[i]
        # start -> city1 -> city2 -> end
        method1 = distance[city1] + distance_1[city2] + distance_2[end]

        # start -> city2 -> city1 -> end
        method2 = distance[city2] + distance_2[city1] + distance_1[end]

        origin = distance[end]

        if origin == method1 or origin == method2:
            ans.append(end)

    ans.sort()
    print(*ans)
