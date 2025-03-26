import sys

input = sys.stdin.readline
n = int(input())
ai = list(map(int, input().split()))
# print(ai)

dp = [0] * n
dp[0] = 1

for i in range(1, n):
    if ai[i] > ai[i-1]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]

print(dp[-1])