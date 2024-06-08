from heapq import heappop, heappush

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
start, end = map(int, input().split())

def dijkstra():
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    pq = []
    # 시작점에서의 비용, 위치
    heappush(pq, [0, start])

    while pq:
        cost, now = heappop(pq)

        if distance[now] < cost:
            continue

        for i in graph[now]:
            next_cost = cost + i[0]
            next_ = i[1]

            if distance[next_] > next_cost:
                distance[next_] = next_cost
                prev_node[next_] = now
                heappush(pq, [next_cost, next_])

    return distance

prev_node = [0] * (n+1)
distance = dijkstra()
# print(distance)
print(distance[end])
# print(prev_node)

path = []
current = end
while current:
    path.append(current)
    current = prev_node[current]
print(len(path))
for i in path[::-1]:
    print(i, end=' ')