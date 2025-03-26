from pprint import pprint
import sys
from heapq import heappush, heappop

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(m)]
# pprint(arr)

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def dijkstra():
    distance = [[float('inf')] * n for _ in range(m)]
    distance[0][0] = 0
    pq = []
    # 시작점의 벽 유무, row, col
    heappush(pq, [arr[0][0], 0, 0])

    while pq:
        dist, row, col = heappop(pq)

        if distance[row][col] < dist:
            continue

        # 4바퀴 돌기
        for dij in range(4):
            next_r = row+di[dij]
            next_c = col+dj[dij]
            if 0 <= next_r < m and 0 <= next_c < n:
                next_dist = dist+arr[next_r][next_c]
                # 범위 안에있고 현재 distance에 저장되어 있는거 보다 다음게 더 크다면
                if distance[next_r][next_c] > next_dist:
                    distance[next_r][next_c] = next_dist
                    heappush(pq, [next_dist, next_r, next_c])

    return distance

distance = dijkstra()
# pprint(distance)
print(distance[-1][-1])