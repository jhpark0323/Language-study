import sys
from pprint import pprint
from heapq import heappush,heappop

ipt = sys.stdin.readline

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def dijkstra():
    # 시작점
    distance[0][0] = arr[0][0]
    # priority queue
    pq = []
    # 가중치, 시작_row, 시작_col
    heappush(pq, (arr[0][0], 0, 0))

    while pq:
        dist, row, col = heappop(pq)

        # 저장된 값이 새로 찾은 거리 dist보다 이미 작으면 넘어감
        if distance[row][col] < dist:
            continue

        # 4방향 순회
        for dij in range(4):
            next_row = row + di[dij]
            next_col = col + dj[dij]

            # 범위안에있고
            if 0 <= next_row < n and 0 <= next_col < n:

                # distance보다 작으면
                next_dist = dist + arr[next_row][next_col]
                # if distance[next_row][next_col] > next_dist:
                if distance[next_row][next_col] > next_dist:
                    # 갱신
                    distance[next_row][next_col] = next_dist
                    # append
                    heappush(pq, (next_dist, next_row, next_col))


test_case = 1
while 1:
    n = int(ipt().strip())

    if n == 0:
        break

    arr = [list(map(int, ipt().strip().split())) for _ in range(n)]
    # pprint(arr)

    inf = float('inf')
    distance = [[inf] * n for _ in range(n)]
    dijkstra()
    # pprint(distance)

    print(f'Problem {test_case}: {distance[-1][-1]}')

    test_case += 1