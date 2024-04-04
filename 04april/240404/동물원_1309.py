def f(n):
    # 사자가 없을때, 1번에 있을 떄, 2번에 있을 때를 따로 계산 해줌
    dp = [[0] * 3 for _ in range(n + 1)]
    # 사자가 없을 때
    dp[1][0] = 1
    # 사자가 1번쨰 열에 있을 떄
    dp[1][1] = 1
    # 사자가 2번째 열에 있을 때
    dp[1][2] = 1

    for i in range(2, n + 1):
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901
        dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
        dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

    return (dp[n][0] + dp[n][1] + dp[n][2]) % 9901

n = int(input())
ans = f(n)
print(ans)
