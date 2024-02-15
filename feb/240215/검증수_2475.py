ls = list(map(int, input().split()))

total = 0

for i in ls:
    total += i ** 2

total %= 10
print(total)