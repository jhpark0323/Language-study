import sys
from pprint import pprint
from collections import deque


input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# pprint(arr)

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def f(array, year):
    new_arr = [[0] * m for _ in range(n)]
    # 새로운 섬의 사이즈를 구해 나중에 bfs와 비교해 크기가 같은지 비교
    # 크기가 다르면 섬이 한덩어리가 아님
    new_arr_size = 0
    for row in range(n):
        for col in range(m):
            # 0이 아니면
            if array[row][col]:
                cnt = 0
                for dir in range(4):
                    next_row = row + di[dir]
                    next_col = col + dj[dir]

                    # 범위안에있고 0이면
                    if 0 <= next_row < n and 0 <= next_col < m and not arr[next_row][next_col]:
                        cnt += 1
                new_arr[row][col] = array[row][col] - cnt
                if new_arr[row][col] <= 0:
                    new_arr[row][col] = 0
                # 0이 아니면 섬이 남아있음
                else:
                    new_arr_size += 1

    pprint(new_arr)
    size = bfs(new_arr)

    # 사이즈가 같으면 다시 해야함
    if size == new_arr_size:
        return new_arr

    # 사이즈가 다르면 끝
    else:
        return year


def bfs(new_arr):
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    q = deque([[0, 0]])
    size = 0

    while q:
        current_row, current_col = q.popleft()
        size += 1

        # 값이 있으면
        if new_arr[current_row][current_col]:
            for dij in range(4):
                n_r = current_row + di[dij]
                n_c = current_col + dj[dij]

                if 0 <= n_r < n and 0 <= n_c < m and not visited[n_r][n_c]:
                    visited[n_r][n_c] = True
                    q.append([n_r, n_c])

    return size

ans = 0
while True:
    arr = f(arr, ans)
    if arr == ans:
        break

    ans += 1




pprint(ans)
