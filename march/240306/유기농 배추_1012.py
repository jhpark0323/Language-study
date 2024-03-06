
'''
dfs사용 -> 1이 있는 곳 cabbage_field 돌며 찾아서 dfs로 전부 visited 처리 -> 방문하지 않은 곳으로 다시 1 찾음
'''

import sys
from pprint import pprint

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def dfs(row, col):
    visited = [[False] * n for _ in range(m)]
    visited[row][col] = True
    stack = [[row, col]]

    while stack:
        current_m, current_n = stack.pop()
        visited[current_m][current_n] = True
        bug[current_m][current_n] = True

        for i in range(4):
            # 범위안에 존재하고 방문하지 않았고
            if 0 <= current_m+di[i] < m and 0 <= current_n+dj[i] < n and not visited[current_m+di[i]][current_n+dj[i]]:
                # 1이면
                if cabbage_field[current_m+di[i]][current_n+dj[i]] == 1:
                    stack.append([current_m+di[i], current_n+dj[i]])


T = int(input())

for test_case in range(T):
    # m : 가로길이, n : 세로길이, k : 배추 위치 개수
    m, n, k = map(int, sys.stdin.readline().strip().split())

    arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(k)]
    # print(arr)

    # 가로, 세로가 반대로 되어있는듯?
    cabbage_field = [[0] * n for _ in range(m)]
    for i in arr:
        cabbage_field[i[0]][i[1]] = 1

    # pprint(cabbage_field)

    # 벌레를 이미 놔둬서 갈 수 있는 곳
    bug = [[False] * n for _ in range(m)]

    cnt = 0
    for i in range(m):
        for j in range(n):
            if not bug[i][j] and cabbage_field[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)