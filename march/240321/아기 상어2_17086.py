import sys
from collections import deque

di = [1, -1, 0, 0, 1, -1, 1, -1]
dj = [0, 0, 1, -1, 1, 1, -1, -1]

def bfs(row, col):
    visited = [[0] * m for _ in range(n)]
    visited[row][col] = 1
    # 시작 row, col, cnt
    q = deque([[row, col, 0]])

    while q:
        current_row, current_col, cnt = q.popleft()

        if arr[current_row][current_col] == 1:
            return cnt

        for dij in range(8):
            next_row, next_col = current_row + di[dij], current_col + dj[dij]
            # 범위안에 있고 방문안했을 때
            if 0 <= next_row < n and 0 <= next_col < m and not visited[next_row][next_col]:
                visited[next_row][next_col] = 1
                q.append([next_row, next_col, cnt+1])

ipt = sys.stdin.readline

n, m = map(int, ipt().strip().split())
arr = [list(map(int, ipt().strip().split())) for _ in range(n)]

max_cnt = -float('inf')
for i in range(n):
    for j in range(m):
        count = bfs(i, j)
        if max_cnt < count:
            max_cnt = count

print(max_cnt)