from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs():
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    q = deque([[0, 0, 0]])

    while q:
        row, col, wall = q.popleft()

        if row == n-1 and col == m-1:
            return visited[row][col][wall]

        for dij in range(4):
            next_row = row + di[dij]
            next_col = col + dj[dij]

            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= m:
                continue

            if arr[next_row][next_col] == 1 and wall == 0:
                visited[next_row][next_col][1] = visited[row][col][0] + 1
                q.append([next_row, next_col, 1])

            elif arr[next_row][next_col] == 0 and visited[next_row][next_col][wall] == 0:
                visited[next_row][next_col][wall] = visited[row][col][wall] + 1
                q.append([next_row, next_col, wall])

    return -1

print(bfs())