N = int(input())
TP = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

# 뒤에서 순회
for i in range(N-1, -1, -1):
    if i+TP[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+TP[i][0]]+TP[i][1])
print(dp[0])