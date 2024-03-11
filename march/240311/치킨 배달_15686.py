import sys
from pprint import pprint
from itertools import combinations
from collections import deque

'''
1. 치킨집이 있는 위치를 전부 찾기
2. m을 이용해 치킨집의 모든 조합을 찾음
ex) chicken C m -> 최대 13C6 -> 1716 할만할듯?
3. 각 조합에서 각 집마다의 최소거리를 다 더해줌
4. 최솟값 찾기 
'''

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(ls):
    global distance
    visited = [[0] * n for _ in range(n)]
    for ii in ls:
        visited[ii[0]][ii[1]] = 1
    # pprint(visited)

    q = deque(ls)

    while q:
        current_row, current_col, cnt = q.popleft()
        # print(current_row, current_col, cnt)

        for dij in range(4):
            nr = current_row+di[dij]
            nc = current_col+dj[dij]

            # 범위 안에 있고 방문하지 않았으면
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = 1
                # 1을 찾으면 distance에 cnt를 더해줌
                if arr[nr][nc] == 1:
                    distance += cnt
                q.append([nr, nc, cnt+1])



n, m = map(int, sys.stdin.readline().strip().split())

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
# pprint(arr)

# 치킨과 집의 위치를 담은 ls
chicken_ls = []
house_ls = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house_ls.append([i, j])

        elif arr[i][j] == 2:
            chicken_ls.append([i, j])
# print('chicken_ls :', chicken_ls)
# print('house_ls :', house_ls)

# 조합구하기
p = [i for i in range(len(chicken_ls))]
combi = list(combinations(p, m))
# print('combi :', combi)

min_distance = float('inf')
for i in combi:
    # 치킨집 조합으로 만든 치킨집 위치, cnt를 넣어주는데 1부터 시작
    combi_chicken = [chicken_ls[j] + [1] for j in i]
    # print(combi_chicken)

    distance = 0
    bfs(combi_chicken)

    if min_distance > distance:
        min_distance = distance

print(min_distance)