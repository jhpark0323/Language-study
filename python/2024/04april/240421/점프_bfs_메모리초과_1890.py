import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)

di = [0, 1]
dj = [1, 0]

def bfs():
    q = deque([[0, 0]])
    cnt = 0
    while q:
        current_row, current_col = q.popleft()

        if arr[current_row][current_col] == 0:
            cnt += 1
            continue

        for dij in range(2):
            next_row = current_row + di[dij] * arr[current_row][current_col]
            next_col = current_col + dj[dij] * arr[current_row][current_col]
            # print('next_row :', next_row)
            # print('next_col :', next_col)

            if 0 <= next_row < n and 0 <= next_col < n:
                q.append([next_row, next_col])

    return cnt

ans = bfs()
print(ans)