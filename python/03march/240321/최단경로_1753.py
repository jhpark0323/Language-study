import sys
from heapq import heappush, heappop
'''
서로 다른 두 간선 사이에 여러개의 간선이 존재 할 수도 있다??
'''

def dijkstra():
    # 시작점 갱신
    distance[start] = 0
    # pq 생성
    pq = []
    # 거리, 시작점
    heappush(pq, (0, start))

    while pq:
        dist, current = heappop(pq)

        # 다음 위치와 거리
        for neighbor in graph[current]:
            next_dist = dist + neighbor[0]
            next_ = neighbor[1]

            # 최솟값 갱신
            if distance[next_] > next_dist:
                distance[next_] = next_dist
                heappush(pq, (next_dist, next_))

ipt = sys.stdin.readline
v, e = map(int, ipt().strip().split())
start = int(ipt().strip())

graph = [[] for _ in range(v+1)]
# graph 만들기
for i in range(e):
    s, e, w = map(int, ipt().strip().split())
    # graph에 가중치와 도착 노드 올림
    graph[s].append([w, e])
# print(graph)

inf = float('inf')
distance = [inf] * (v+1)
dijkstra()

# print(distance[1:])

ans = distance[1:]

for i in ans:
    if i == float('inf'):
        print('INF')
    else:
        print(i)