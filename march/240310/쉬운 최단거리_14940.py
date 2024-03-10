from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs():
    global visited
    visited[start_row][start_col] = 0
    cnt = 1
    # cnt를 하나씩 늘려서 visited에 넣기
    q = deque([[start_row, start_col, cnt]])

    while q:
        current_row, current_col, count = q.popleft()
        # print(current_row, current_col, count)
        # print(visited)
        for dij in range(4):
            ni = current_row+di[dij]
            nj = current_col+dj[dij]
            # 범위에 들어가 있고 방문하지 않았고 arr이 0이 아니면
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == None and arr[ni][nj] != 0:
                q.append([ni, nj, count+1])
                visited[ni][nj] = count


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            start_row, start_col = i, j
# print(start_row, start_col)
visited = [[None] * m for _ in range(n)]

bfs()

# 0과 -1을 visited에 넣기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            visited[i][j] = 0
        if visited[i][j] == None:
            visited[i][j] = -1

for i in visited:
    print(*i)