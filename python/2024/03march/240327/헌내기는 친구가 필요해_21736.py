import sys
from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(s_r, s_c):
    global cnt
    visited = [[0] * m for _ in range(n)]
    visited[s_r][s_c] = 1
    q = deque([[s_r, s_c]])

    while q:
        current_row, current_col = q.popleft()

        for dij in range(4):
            next_r = current_row + di[dij]
            next_c = current_col + dj[dij]

            if 0 <= next_r < n and 0 <= next_c < m and not visited[next_r][next_c]:
                if arr[next_r][next_c] != 'X':
                    if arr[next_r][next_c] == 'P':
                        cnt += 1

                    visited[next_r][next_c] = 1
                    q.append([next_r, next_c])


ipt = sys.stdin.readline

n, m = map(int, ipt().strip().split())
arr = [list(ipt().strip()) for _ in range(n)]
# print(arr)

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            bfs(i, j)
            break
if cnt:
    print(cnt)
else:
    print('TT')