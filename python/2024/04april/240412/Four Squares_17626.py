n = int(input())

# dp[i] : i를 만들 수 있는 제곱수의 합의 최소 갯수
dp = [0, 1]

for i in range(2, n+1):
    j = 1
    min_val = float('inf')
    while j**2 <= i:
        min_val = min(min_val, dp[i-j**2])
        j += 1
    dp.append(min_val+1)
print(dp[n])