from pprint import pprint

n, m = map(int, input().split())

dp = [[0] * m for _ in range(n)]
dp[0] = [1] * m
# pprint(dp)

di = [0, -1, -1]
dj = [-1, -1, 0]

for i in range(1, n):
    for j in range(m):
        for k in range(3):
            pre_r = i + di[k]
            pre_c = j + dj[k]

            if 0 <= pre_r < n and 0 <= pre_c < m:
                dp[i][j] += dp[pre_r][pre_c]
            dp[i][j] = dp[i][j] % 1000000007

print(dp[n-1][m-1])
# pprint(dp)