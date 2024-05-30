import sys
from pprint import pprint
from collections import deque

ipt = sys.stdin.readline

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs():
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    q = deque([[0, 0, 0]])

    while q:
        current_row, current_col, cnt = q.popleft()

        if arr[current_row][current_col] == 2:
            return cnt+1

        for dij in range(4):
            next_row = current_row + di[dij]
            next_col = current_col + dj[dij]

            # 범위안에 있고 방문하지 않았고 0이아니면
            if 0 <= next_row < n and 0 <= next_col < m and not visited[next_row][next_col] and arr[next_row][next_col] != 0:
                visited[next_row][next_col] = 1
                q.append([next_row, next_col, cnt+1])


n, m = map(int, ipt().strip().split())
arr = [list(map(int, list(ipt().strip()))) for _ in range(n)]
# pprint(arr)

# 도착지점 표시
arr[n-1][m-1] = 2
count = bfs()
print(count)