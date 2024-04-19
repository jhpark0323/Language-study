n = int(input())

dp = [0, 1, 0, 1, 1]


for i in range(5, n+1):
    if dp[i-1] == 1 and dp[i-3] == 1 and dp[i-4] == 1:
        dp.append(0)
    else:
        dp.append(1)

if dp[n] == 1:
    print('SK')

else:
    print('CY')