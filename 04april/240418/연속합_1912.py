import sys

input = sys.stdin.readline
n = int(input())
ls = list(map(int, input().split()))
# print(ls)

dp = [0] * (n)
dp[0] = ls[0]

ans = ls[0]
for i in range(1, n):
    dp[i] = max(ls[i], ls[i]+dp[i-1])
    ans = max(ans, dp[i])

# print(dp)
print(ans)