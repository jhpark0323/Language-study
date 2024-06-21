from collections import deque
from itertools import combinations
from copy import deepcopy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(row, col):
    visited = [[False] * m for _ in range(n)]
    visited[row][col] = True
    q = deque([[row, col]])

    while q:
        now_row, now_col = q.popleft()

        for dij in range(4):
            next_r = now_row + di[dij]
            next_c = now_col + dj[dij]

            if 0 <= next_r < n and 0 <= next_c < m and new_arr[next_r][next_c] == 0:
                q.append([next_r, next_c])
                visited[next_r][next_c] = True
                # 새로 생긴 바이러스들은 어짜피 bfs에서 다 돌려봤으니 그냥 표시만 해둠
                new_arr[next_r][next_c] = 3

virus = []
empty = []
# virus와 empty에 담기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            empty.append([i, j])

        elif arr[i][j] == 2:
            virus.append([i, j])

combi = list(combinations(empty, 3))
# print(combi)
#
# print(virus)

ans = 0
# combi를 순회
for each in combi:
    new_arr = deepcopy(arr)
    # 3군데 벽세우기
    for j in range(3):
        new_arr[each[j][0]][each[j][1]] = 1

    # 바이러스 위치를 bfs에 대입
    for vi in virus:
        bfs(vi[0], vi[1])

    new_ans = 0
    for safe_r in range(n):
        for safe_c in range(m):
            if new_arr[safe_r][safe_c] == 0:
                new_ans += 1

    if ans < new_ans:
        ans = new_ans

print(ans)