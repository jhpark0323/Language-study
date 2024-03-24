import sys
from collections import deque
from pprint import pprint

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(arr, row, col, color, visited):

    visited[row][col] = True
    q = deque([[row, col]])

    while q:
        current_row, current_col = q.popleft()

        for dij in range(4):
            next_row = current_row + di[dij]
            next_col = current_col + dj[dij]
            # 범위 안에 있고 방문하지 않았다면
            if 0 <= next_row < n and 0 <= next_col < n and not visited[next_row][next_col]:
                # 색이 같다면
                if arr[next_row][next_col] == color:
                    q.append([next_row, next_col])
                    visited[next_row][next_col] = True


ipt = sys.stdin.readline
n = int(ipt())
arr = [list(ipt().strip()) for _ in range(n)]
# print(arr)

arr_rg = [[0] * n for _ in range(n)]
# 적록색약의 기준 (R == G)
for i in range(n):
    for j in range(n):
        # 빨간색과 초록색이면
        if arr[i][j] == 'R' or arr[i][j] == 'G':
            arr_rg[i][j] = 'R'
        # 파란색이면
        else:
            arr_rg[i][j] = 'B'


# pprint(arr_rg)

# normal
visited_n = [[False] * n for _ in range(n)]

# rg
visited_rg = [[False] * n for _ in range(n)]

cnt_normal = 0
cnt_rg = 0

# arr을 돌며 확인
for i in range(n):
    for j in range(n):
        color = arr[i][j]

        # 아직 방문하지 않은 곳이면
        if not visited_n[i][j]:
            bfs(arr, i, j, color, visited_n)
            cnt_normal += 1

        if not visited_rg[i][j]:
            if color == 'G':
                color = 'R'
            bfs(arr_rg, i, j, color, visited_rg)
            # pprint(visited_rg)
            cnt_rg += 1

print(cnt_normal, cnt_rg)