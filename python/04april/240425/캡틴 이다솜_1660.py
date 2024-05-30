n = int(input())

dp = [0]
real_dp = [0]
for i in range(1, n+1):
    dp.append(i+dp[i-1])
    real_dp.append(dp[i] + real_dp[i-1])
    if real_dp[i] >= n:
        break
# print(dp)
# print(real_dp)

ans = [0, 1, 2, 3, 1]
standard = 2
for i in range(5, n+1):
    # standard를 기준으로 for문 돌리기

    if i in real_dp:
        ans.append(1)
        # 새로운거 나오면 standard 하나 증가
        standard += 1

    else:
        min_val = float('inf')
        for j in range(1, standard+1):
            val = ans[real_dp[j]] + ans[i-real_dp[j]]
            if min_val > val:
                min_val = val
                # print(min_val)
        ans.append(min_val)

# print(ans)
print(ans[-1])
# print(standard)
# print(ans[35])
# print(ans[56])
# print(ans[84])