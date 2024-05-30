import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
dp[0][0] = arr[0][0]

di = [-1, 0, -1]
dj = [0, -1, -1]

for i in range(n):
    for j in range(m):
        # 3방향중 최댓값을 찾아 더해줌
        max_ = 0
        # 3방향을 다 돌았을 때
        for k in range(3):
            next_r = i+di[k]
            next_c = j+dj[k]

            if 0 <= next_r < n and 0 <= next_c < m:
                if max_ < dp[next_r][next_c]:
                    max_ = dp[next_r][next_c]

        dp[i][j] = arr[i][j] + max_

print(dp[-1][-1])