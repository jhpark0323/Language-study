import sys
from pprint import pprint
input = sys.stdin.readline
n = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def back(cnt):
    global mincnt, minmove
    location = []
    for i in range(5):
        for j in range(9):
            # 현재 위치가 o이면
            if arr[i][j] == 'o':
                location.append((j, i))

    if len(location) < mincnt:
        minmove = cnt
        mincnt = len(location)

    for x, y in location:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx+dx[i] < 9 and -1 < ny+dy[i] < 5:
                if arr[ny][nx] == 'o' and arr[ny+dy[i]][nx+dx[i]] == '.':
                    arr[ny][nx] = '.'
                    arr[ny+dy[i]][nx+dx[i]] = 'o'
                    arr[y][x] = '.'
                    back(cnt+1)
                    arr[ny][nx] = 'o'
                    arr[ny + dy[i]][nx + dx[i]] = '.'
                    arr[y][x] = 'o'

for test_case in range(n):
    mincnt = 10
    minmove = 10
    arr = [list(input().strip()) for _ in range(5)]
    input()
    back(0)
    print(mincnt, minmove)