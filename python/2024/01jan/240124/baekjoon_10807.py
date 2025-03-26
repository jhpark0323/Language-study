n = int(input())
ls = list(map(int, input().split()))
v = int(input())
count = 0

for i in range(len(ls)):
    if ls[i] == v:
        count += 1
print(count)