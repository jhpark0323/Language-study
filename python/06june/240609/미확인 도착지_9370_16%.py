'''
이방법은 하나의 방법에 최단경로가 여러개 있을 수도 있어서 실패한듯
'''

from heapq import heappop, heappush

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
    # print('distance: ', distance)
    # print('prev_city: ', prev_city)

    ans = []

    # 목적지 후보들
    for i in range(t):
        end = candidate[i]

        # 도착 못했을 수도
        if distance[end] == float('inf'):
            continue

        # 경로 찾기
        path = []
        current = end
        while current:
            path.append(current)
            current = prev_city[current]

        path = path[::-1]
        # print(path)

        # 만약 경로에 city1, city2가 연속으로 들어가 있으면 성공
        # 도시를 다 돌아봄
        for j in range(len(path)-1):
            # 첫번째 도시는 두번째만 봄
            if j == 0:
                # 첫번째가 city1일때 두번째가 city2이면 성공
                if path[j] == city1 and path[j+1] == city2:
                    ans.append(end)
                    break
            # 두번째 이후부터는 앞뒤를 봄
            else:
                if path[j] == city1:
                    if path[j-1] == city2 or path[j+1] == city2:
                        ans.append(end)
                        break
    ans.sort()
    print(*ans)