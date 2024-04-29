d, k = map(int, input().split())

# a + b의 형태로 만들때 dp의 각 원소들은 a, b의 계수
dp = [[0, 0], [1, 0], [0, 1]]

for i in range(3, d+1):
    first, second = dp[i-2], dp[i-1]
    dp.append([first[0] + second[0], first[1] + second[1]])
# print(dp)

a_coef = dp[-1][0]
b_coef = dp[-1][1]

# 첫날은 1이상 k // 2 이하임
# -> a = k // 2, b = k // 2
# -> 3일째 : k (∵  3 <= d)
for a in range(1, k//2+1):
    # 둘째날은 많아도 k-1 까지
    # -> a가 1이상임
    for b in range(a, k):
        if a_coef * a + b_coef * b == k:
            print(a)
            print(b)
            exit()