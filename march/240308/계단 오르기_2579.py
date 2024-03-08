def solve(N, stair):
    dp = [0] * (N + 1)
    # print(dp)

    dp[1] = stair[0]
    if N >= 2:
        dp[2] = stair[0] + stair[1]

    if N >= 3:
        for i in range(2, N+1):
            dp[i] = max(dp[i-2] + stair[i-1], dp[i-3] + stair[i-2] + stair[i-1])

    return dp[N]

n = int(input())
stair = [int(input()) for _ in range(n)]

print(solve(n, stair))