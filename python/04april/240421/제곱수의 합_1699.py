n = int(input())

dp = [0, 1]

squared = [1]

for i in range(2, n+1):
    # 제곱수이면
    if i**(1/2) == int(i**(1/2)):
        # print(i)
        squared.append(i)
        dp.append(1)
    # 제곱수가 아니면
    else:
        min_ = 100
        for sq in squared:
            new = dp[sq] + dp[i-sq]

            if min_ > new:
                min_ = new
        dp.append(min_)

print(dp[n])