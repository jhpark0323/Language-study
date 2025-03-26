n = int(input())
ls = list(map(int, input().split()))

cnt = 0
for num in ls:
    real = 0

    # 1은 소수가 아님
    if num == 1:
        real -= 1

    for i in range(1, num+1):
        if i == num or i == 1:
            continue
        else:
            if num % i == 0:
                real = 1
                break
    if real == 0:
        cnt += 1

print(cnt)