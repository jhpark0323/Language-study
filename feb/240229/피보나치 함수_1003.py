def fibonacci(n):
    # 이미 계산한 값이 있는지 확인
    if n in memo:
        return memo[n]

    if n == 0:
        return 0

    elif n == 1:
        return 1

    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    # print(memo)
    return memo[n]

T = int(input())

for tc in range(T):
    n = int(input())
    # memorization
    memo = {}

    fibonacci(n)
    # print(memo)

    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        print(memo[n-1], memo[n])
