def backtracking(row, col, cnt):
    global ans
    # 종료조건
    if cnt == k:
        if row == 0 and col == c-1:
            ans += 1
        return

    for dij in range(4):
        next_r = row + di[dij]
        next_c = col + dj[dij]

        # 범위안에 들어있을 때, T가 아니고 방문하지 않았을 때
        if 0 <= next_r < r and 0 <= next_c < c and arr[next_r][next_c] != 'T' and not visited[next_r][next_c]:
            visited[next_r][next_c] = 1
            backtracking(next_r, next_c, cnt+1)
            visited[next_r][next_c] = 0

r, c, k = map(int, input().split())
arr = [list(input()) for _ in range(r)]
# print(arr)

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

visited = [[0] * c for _ in range(r)]
visited[r-1][0] = 1

ans = 0
if k >= r + c - 1:
    backtracking(r-1, 0, 1)
print(ans)