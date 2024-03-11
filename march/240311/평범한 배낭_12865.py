from pprint import pprint

N, K = map(int, input().split())
items = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight, value = items[i]
        if j >= weight:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
        else:
            dp[i][j] = dp[i-1][j]
pprint(dp)
print(dp[N][K])
