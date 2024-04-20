import sys
input = sys.stdin.readline
n = int(input())
ls = list(map(int, input().split()))
# print(ls)

dp = [[0] * n for _ in range(2)]
dp[0][0] = ls[0]
dp[1] = ls
# print(dp)

ans = ls[0]
for i in range(1, n):
    # i부터 뒤로 돌면서 전에 나온 값의 크기랑 비교
    for j in range(i-1, -1, -1):
        # j의 값의 크기보다 현재의 크기가 더 크면
        if dp[1][j] < ls[i]:
            # 현재 dp자리에 있는 숫자와 j값의 크기 + ls[i]를 비교 후 큰 숫자 대입
            print(dp)
            dp[0][i] = max(dp[0][i], dp[0][j] + ls[i])
            ans = max(ans, dp[0][i])
        else:
            dp[0][i] = dp[1][i]


# print(dp)
print(ans)