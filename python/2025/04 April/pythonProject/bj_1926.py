import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def dfs(row, col):
    global cnt
    arr[row][col] = 0
    cnt += 1
    for dij in range(4):
        nxt_row = row + di[dij]
        nxt_col = col + dj[dij]

        if nxt_row < 0 or nxt_row >= n or nxt_col < 0 or nxt_col >= m:
            continue

        if arr[nxt_row][nxt_col] == 1:
            dfs(nxt_row, nxt_col)

ans = 0
max_cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            continue
        cnt = 0
        dfs(i, j)
        max_cnt = max(max_cnt, cnt)
        ans += 1

print(ans)
print(max_cnt)