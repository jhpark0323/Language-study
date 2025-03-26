from heapq import heappush, heappop
from pprint import pprint

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

def dijkstra():
    distance = [[float('inf')] * (n) for _ in range(n)]
    distance[0][0] = 0
    pq = []
    # 시작시 바꿔진 방의 개수, row, col
    heappush(pq, [0, 0, 0])

    while pq:
        dist, row, col = heappop(pq)

        if distance[row][col] < dist:
            continue

        for dij in range(4):
            next_row = row + di[dij]
            next_col = col + dj[dij]

            # 범위 안에 있으면
            if 0 <= next_row < n and 0 <= next_col < n:
                # 검은방이면
                if not arr[next_row][next_col]:
                    next_dist = dist + 1
                # 흰방이면
                else:
                    next_dist = dist

                if distance[next_row][next_col] > next_dist:
                    distance[next_row][next_col] = next_dist
                    heappush(pq, [next_dist, next_row, next_col])

    return distance

distance = dijkstra()
# pprint(distance)
print(distance[-1][-1])