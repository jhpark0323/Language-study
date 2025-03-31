import sys
from collections import deque
input = sys.stdin.readline
r, c = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

cheeze = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == 1:
            cheeze += 1

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def bfs():
    visited = [[False] * c for _ in range(r)]
    visited[0][0] = True
    q = deque([[0, 0]])
    melt = []
    while q:
        now_r, now_c = q.popleft()
        for dij in range(4):
            nxt_r = now_r + di[dij]
            nxt_c = now_c + dj[dij]

            if nxt_r < 0 or nxt_r >= r or nxt_c < 0 or nxt_c >= c:
                continue
            if visited[nxt_r][nxt_c]:
                continue

            visited[nxt_r][nxt_c] = True
            if arr[nxt_r][nxt_c] == 0:
                q.append([nxt_r, nxt_c])
            elif arr[nxt_r][nxt_c] == 1:
                melt.append([nxt_r, nxt_c])

    for row, col in melt:
        arr[row][col] = 0
    return len(melt)

idx = 1
while True:
    cnt = bfs()
    cheeze -= cnt
    if cheeze == 0:
        break
    idx += 1

print(idx)
print(cnt)