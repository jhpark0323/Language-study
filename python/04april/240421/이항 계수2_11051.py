n, k = map(int, input().split())

factorial = [1, 1]

for i in range(2, n+1):
    factorial.append(i*factorial[-1])
# print(factorial[n])

print(factorial[n] // (factorial[k] * factorial[n-k]) % 10007)