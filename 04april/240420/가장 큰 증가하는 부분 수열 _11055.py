import sys
input = sys.stdin.readline
n = int(input())
ls = list(map(int, input().split()))
# print(ls)

dp = [0] * n
dp[0] = ls[0]

ans = ls[0]
for i in range(n):
    # i부터 뒤로 돌면서 전에 나온 값의 크기랑 비교
    for j in range(i):
        # j의 값의 크기보다 현재의 크기가 더 크면
        if ls[j] < ls[i]:
            # 현재 dp자리에 있는 숫자와 j값의 크기 + ls[i]를 비교 후 큰 숫자 대입
            # print(dp)
            dp[i] = max(dp[i], dp[j] + ls[i])
        else:
            dp[i] = max(dp[i], ls[i])

        ans = max(ans, dp[i])


# print(dp)
print(ans)