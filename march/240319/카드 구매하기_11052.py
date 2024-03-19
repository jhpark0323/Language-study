import sys

ipt = sys.stdin.readline
n = int(ipt().strip())
pi = list(map(int, ipt().strip().split()))
# print(pi)

# dp써보자
dp = [0] * n

# 하나씩 올림
for i in range(n):
    # 첫번째는 그냥 pi에서 가져옴
    if i == 0:
        dp[i] = pi[0]
    # 두번째 부터
    else:
        # 일단 pi[i]를 넣어둠
        dp[i] = pi[i]
        # 그리고 처음부터 i까지 순회하며
        for j in range(i):
            # dp[i]에 dp[i-1-j]+dp[j]와 비교해서 큰걸 넣음
            # ex) 4 -> 1+3 or 2+2 or 3+1 를 순회하게 됨
            dp[i] = max(dp[i-1-j]+dp[j], dp[i])

# print(dp)
print(dp[-1])