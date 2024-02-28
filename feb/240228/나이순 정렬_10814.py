import sys

n = int(input())
arr = [list(sys.stdin.readline().split()) for _ in range(n)]

for i in arr:
    i[0] = int(i[0])

# print(arr)

arr.sort(key=lambda x: x[0])

for i in arr:
    print(*i)