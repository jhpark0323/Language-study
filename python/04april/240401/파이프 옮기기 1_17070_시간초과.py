import sys
from collections import deque

'''
1. 방향을 설정
-> 가로방향 : 0, 대각선 방향 : 1, 세로방향 : 2
2. 방향과 끝점을 q에 넣어 bfs 돌림
'''

# 방향 가로 대각선 세로
di = [0, 1, 1]
dj = [1, 1, 0]

def bfs():
    global cnt
    # visited = [[False]*n for _ in range(n)]
    # visited[0][1] = True
    # row, col, dir
    q = deque([[0, 1, 0]])

    while q:
        current_row, current_col, dir = q.popleft()

        if current_row == n-1 and current_col == n-1:
            cnt += 1

        # 방향이 가로일 때
        if dir == 0:
            for dij in range(2):
                next_r = current_row + di[dij]
                next_c = current_col + dj[dij]
                # 범위 안에 있고 방문하지 않았고
                # if 0 <= next_r < n and 0 <= next_c < n and not visited[next_r][next_c]:
                if 0 <= next_r < n and 0 <= next_c < n:
                    # 가로방향일 때
                    if dij == 0:
                        # 벽이 아니면
                        if arr[next_r][next_c] != 1:
                            q.append([next_r, next_c, dij])
                            # visited[next_r][next_c] = True

                    # 대각선 방향 일 때
                    if dij == 1:
                        # 저 중에 벽이 없으면
                        if not arr[next_r][next_c] and not arr[next_r-1][next_c] and not arr[next_r][next_c-1]:
                            q.append([next_r, next_c, dij])
                            # visited[next_r][next_c] = True

        # 방향이 대각선일 때
        if dir == 1:
            for dij in range(3):
                next_r = current_row + di[dij]
                next_c = current_col + dj[dij]
                # 범위 안에 있고 방문하지 않았고
                # if 0 <= next_r < n and 0 <= next_c < n and not visited[next_r][next_c]:
                if 0 <= next_r < n and 0 <= next_c < n:
                    # 대각선 방향 일 때
                    if dij == 1:
                        # 저 중에 벽이 없으면
                        if not arr[next_r][next_c] and not arr[next_r-1][next_c] and not arr[next_r][next_c]:
                            q.append([next_r, next_c, dij])
                            # visited[next_r][next_c] = True
                    # 나머지 방향 일 때
                    else:
                        # 벽이 아니면
                        if arr[next_r][next_c] != 1:
                            q.append([next_r, next_c, dij])
                            # visited[next_r][next_c] = True

        # 방향이 세로일 때
        if dir == 2:
            for dij in range(1, 3):
                next_r = current_row + di[dij]
                next_c = current_col + dj[dij]
                # 범위 안에 있고 방문하지 않았고
                # if 0 <= next_r < n and 0 <= next_c < n and not visited[next_r][next_c]:
                if 0 <= next_r < n and 0 <= next_c < n:
                    # 대각선 방향 일 때
                    if dij == 1:
                        # 저 중에 벽이 없으면
                        if not arr[next_r][next_c] and not arr[next_r - 1][next_c] and not arr[next_r][next_c]:
                            q.append([next_r, next_c, dij])
                            # visited[next_r][next_c] = True
                    # 세로일 때
                    else:
                        # 벽이 아니면
                        if arr[next_r][next_c] != 1:
                            # 방향은 가로 혹은 대각선만 가능
                            q.append([next_r, next_c, dij])
                            # visited[next_r][next_c] = True





input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
# print(arr)

cnt = 0
if arr[n-1][n-1] == 1:
    print(0)
    exit()
bfs()
#애초에 도착점이 빈칸이 아닌
print(cnt)

'''
16
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
'''