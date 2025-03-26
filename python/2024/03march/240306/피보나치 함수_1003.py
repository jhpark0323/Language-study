def fibonacci(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    # 이미 계산한 값이 있는지 확인
    if n in memo:
        return memo[n]

    # n-1과 n-2 값에 대한 피보나치 수 계산
    memo[n-1] = fibonacci(n-1)
    memo[n-2] = fibonacci(n-2)

    # memo에 값을 저장하고 반환
    memo[n] = memo[n-1] + memo[n-2]
    # print(memo)
    return memo[n]

T = int(input())

for tc in range(T):
    n = int(input())
    # memorization
    memo = {}

    # print(memo)

    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        fibonacci(n)
        print(memo[n-1], memo[n])
