import sys

n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
# print(arr)

arr.sort(key=lambda x: (x[1], x[0]))

for i in arr:
    print(*i)