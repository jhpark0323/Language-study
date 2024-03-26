import sys
from pprint import pprint
from collections import deque

ipt = sys.stdin.readline

# delta
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs():
    # 벽을 얼마나 부순지에 대해서도 visited에 대입
    visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
    # 시작점
    visited[0][0][k] = 1
    # 시작 row, col, 벽 부술수있는 갯수, 거리
    q = deque([[0, 0, k, 1]])

    while q:
        current_r, current_c, wall, cnt = q.popleft()

        # 현재 위치가 도착지면
        if current_r == n-1 and current_c == m-1:
            return cnt

        for dij in range(4):
            next_r = current_r + di[dij]
            next_c = current_c + dj[dij]

            # 범위안에 있고
            if 0 <= next_r < n and 0 <= next_c < m:
                # 벽이아니면 -> 벽을 안뚫을 거기 때문에 visited의 마지막은 wall이 됨
                if arr[next_r][next_c] == 0 and not visited[next_r][next_c][wall]:
                    visited[next_r][next_c][wall] = 1
                    q.append([next_r, next_c, wall, cnt+1])
                # 벽이나오고 만약 벽을 뚫을 수 있다면
                elif arr[next_r][next_c] == 1 and wall > 0 and not visited[next_r][next_c][wall-1]:
                    # 방문
                    visited[next_r][next_c][wall-1] = 1
                    q.append([next_r, next_c, wall-1, cnt+1])


    return -1


n, m, k = map(int, ipt().strip().split())
# n, m, k = map(int, input().split())
arr = [list(map(int, list(ipt().strip()))) for _ in range(n)]
# arr = [list(map(int, list(input().strip()))) for _ in range(n)]
# pprint(arr)

count = bfs()
print(count)
