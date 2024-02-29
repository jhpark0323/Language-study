def factorial(num):
    if num <= 1:
        return 1

    else:
        return num * factorial(num-1)

n, k = map(int, input().split())
# print(factorial(5))

answer = factorial(n) // (factorial(n-k) * factorial(k))
print(answer)