def f(weight_sum, cnt, value):
    global val
    if cnt == n:
        # 다 돌았을 때 무게의 합이 k이하이면
        if weight_sum <= k:
            if val < value:
                val = value
            return

    # 무게의 합이 k를 넘으면 실패
    if weight_sum > k:
        return
    # 무게의 합이 k이면 그값 return
    elif weight_sum == k:
        if val < value:
            val = value
        return
        # return value

    for i in range(n):
        for j in range(i, n):
            p[i], p[j] = p[j], p[i]
            f(weight_sum+arr[p[j]][0], cnt+1, value+arr[p[j]][1])
            p[i], p[j] = p[j], p[i]

n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
p = [i for i in range(n)]

val = 0

f(0, 1, 0)
print(val)