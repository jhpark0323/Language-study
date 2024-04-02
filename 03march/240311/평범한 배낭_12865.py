from pprint import pprint

n, k = map(int, input().split())
items = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
# pprint(items)

dp = [[0] * (k+1) for _ in range(n+1)]
# pprint(dp)

# n개의 물품을 돌며 1~k까지의 무게에서 제일 가치가 높을 수 있는 방법을 선택 하여 dp[i][j]에 할당
for i in range(1, n+1):
    # j : j만큼의 무게를 배낭에 넣을 수 있을 때
    for j in range(1, k+1):
        weight, value = items[i]
        # print(weight, value)

        # j가 weight보다 크면
        if j >= weight:
            # 저번 j와 비교
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
        # j가 weight보다 작으면 현재는 담을 수 없으므로 저번 물건에서 j에 담았던걸 담음
        else:
            dp[i][j] = dp[i-1][j]

# pprint(dp)
print(dp[n][k])