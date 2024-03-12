def dfs():
    global cnt
    visited = [[False] * m for _ in range(n)]
    visited[start_row][start_col] = True
    stack = [[start_row, start_col]]


    while stack:
        current_row, current_col = stack.pop()
        cnt += 1

        for dij in range(4):
            next_r = current_row+di[dij]
            next_c = current_col+dj[dij]
            if 0 <= next_r < n and 0 <= next_c < m and arr[next_r][next_c] == 0:
                stack.append([next_r, next_c])
                visited[next_r][next_c] = True

n, m = map(int, input().split())
start_row, start_col, dir = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 반시계 방향 북동남서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

cnt = 0
visited = [[False] * m for _ in range(n)]
while 1:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재칸 청소 -> 청소 한 칸은 2로만들기
    if arr[start_row][start_col] == 0:
        arr[start_row][start_col] = 2
        # 청소 한칸함
        cnt += 1
        # 방문 표시
        visited[start_row][start_col] = True

    # 현재칸의 주변 4칸중 청소되지 않은 빈 칸이 없는 경우
    for dij in range(4):
        next_r = start_row + di[dij]
        next_c = start_col + dj[dij]
        # 청소되지 않은 빈칸이 하나라도 존재하면 break
        # 3. 현재 칸의 주변 4칸 중 청소 되지 않은 빈칸이 있는 경우
        if arr[next_r][next_c] == 0:
            # 반시계 방향으로 90도 회전
            dir = (dir+3) % 4
            # 그 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈칸(0) 이면
            if not arr[start_row+di[dir]][start_col+dj[dir]]:
                # 한칸 전진
                start_row += di[dir]
                start_col += dj[dir]
            # 방향을 돌리고 앞에 빈칸이 있든 말든 일단 break
            break

    # 2. 현재칸의 주변 4칸중 청소되지 않은 빈 칸이 없는 경우
    else:
        # 바라보는 방향의 반대 방향으로
        back = dir-2
        # 한칸 이동
        start_row += di[back]
        start_col += dj[back]

        # 뒤쪽이 벽이라 이동 못하면 작동 중지
        if arr[start_row][start_col] == 1:
            break

print(cnt)