from pprint import pprint
from heapq import heappop, heappush

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    dp = [[INF] * w for _ in range(h)]
    dp[start[0][0]][start[0][1]] = 0
    pq = []
    # 가중치, 시작 행, 열, 방향
    heappush(pq, [0, start[0][0], start[0][1], 0])
    heappush(pq, [0, start[0][0], start[0][1], 1])
    heappush(pq, [0, start[0][0], start[0][1], 2])
    heappush(pq, [0, start[0][0], start[0][1], 3])

    arr[start[0][0]][start[0][1]] = "*"

    while pq:
        dist, x, y, dir = heappop(pq)

        if arr[x][y] == 'C':
        #     # print(dp)
        #     for ii in range(h):
        #         for jj in range(w):
        #             print(dp[ii][jj], end=' ')
        #         print()
            return dp

        if dp[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != '*':
                if dir == i and dist <= dp[nx][ny]:
                    dp[nx][ny] = dist
                    heappush(pq, [dist, nx, ny, dir])

                elif dir != i and dist + 1 <= dp[nx][ny]:
                    dp[nx][ny] = dist + 1
                    heappush(pq, [dist+1, nx, ny, i])

    return dp


w, h = map(int, input().split())
arr = [list(input()) for _ in range(h)]
# pprint(arr)

INF = int(1e9)

start = []

for i in range(h):
    for j in range(w):
        if arr[i][j] == "C":
            start.append([i, j])
distance = dijkstra()
# for ii in range(h):
#     for jj in range(w):
#         print(distance[ii][jj], end=' ')
#     print()
print(distance[start[1][0]][start[1][1]])

'''
15 10
...*...***.C..*
.*.*.*........*
.*...*...*....*
.*.*....****.**
.*..**........*
.**..********.*
.*...*...*..*.*
.**..***.*.**.*
C........*.....
..***..........
답: 6
'''