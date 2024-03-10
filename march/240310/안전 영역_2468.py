import copy
from pprint import pprint
from collections import deque

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(i, j):
    global cnt
    visited = [[0] * n for _ in range(n)]
    visited[i][j] = 1
    q = deque([[i, j]])

    while q:
        current_i, current_j = q.popleft()
        visited[current_i][current_j] = 1
        for dij in range(4):
            # 범위안에 있고
            if 0 <= current_i+di[dij] < n and 0 <= current_j+dj[dij] < n:
                # 방문하지 않았고
                if not visited[current_i+di[dij]][current_j+dj[dij]]:
                    # 그 자리가 0이 아니면
                    if new_arr[current_i+di[dij]][current_j+dj[dij]]:
                        q.append([current_i+di[dij], current_j+dj[dij]])
                        # 그 부분을 0으로 만들어 다시 i, j값으로 찾지 않게 함
                        new_arr[current_i+di[dij]][current_j+dj[dij]] = 0
    cnt += 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_height = 0
for i in range(n):
    if max_height < max(arr[i]):
        max_height = max(arr[i])
# print(max_height)

max_cnt = 0
for rain_height in range(max_height):
    new_arr = copy.deepcopy(arr)

    for i in range(n):
        for j in range(n):
            # 비의 높이이하이면 잠김
            if new_arr[i][j] <= rain_height:
                # 잠긴 곳은 0으로 만듬
                new_arr[i][j] = 0
    # pprint(new_arr)

    cnt = 0
    for i in range(n):
        for j in range(n):
            # 그 자리가 잠기지 않았을 때
            if new_arr[i][j]:
                bfs(i, j)
                # print(cnt)
            if max_cnt < cnt:
                max_cnt = cnt

print(max_cnt)