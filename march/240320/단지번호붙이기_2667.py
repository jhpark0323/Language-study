import sys
from pprint import pprint
from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(start_row, start_col):
    visited = [[0] * n for _ in range(n)]
    visited[start_row][start_col] = 1
    q = deque([[start_row, start_col]])
    cnt = 1

    while q:
        current_row, current_col = q.popleft()
        # 4dir
        for dij in range(4):
            next_row = current_row + di[dij]
            next_col = current_col + dj[dij]

            if 0 <= next_row < n and 0 <= next_col < n and not visited[next_row][next_col]:
                if arr[next_row][next_col] == 1:
                    q.append([next_row, next_col])
                    visited[next_row][next_col] = 1
                    arr[next_row][next_col] = 0
                    cnt += 1
    return cnt


ipt = sys.stdin.readline

n = int(ipt().strip())
arr = [list(map(int, ipt().strip())) for _ in range(n)]
# pprint(arr)

ans_ls = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            ans_ls.append(bfs(i, j))

# print(ans_ls)
ans_ls.sort()

print(len(ans_ls))
for i in ans_ls:
    print(i)