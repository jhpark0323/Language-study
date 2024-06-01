import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append([cost, end])

start, end = map(int, input().split())

def dijkstra():
    # 시작점
    distance[start] = 0

    # pq생성
    pq = []
    heappush(pq, (0, start))

    while pq:
        dist, current = heappop(pq)

        if distance[current] < dist:
            continue

        for i in graph[current]:
            next_dist = dist + i[0]
            next_ = i[1]

            if distance[next_] > next_dist:
                distance[next_] = next_dist
                heappush(pq, (next_dist, next_))


distance = [float('inf')] * (n+1)
dijkstra()
print(distance[end])