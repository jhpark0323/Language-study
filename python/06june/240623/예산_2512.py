import sys

input = sys.stdin.readline
n = int(input())
ls = list(map(int, input().split()))
m = int(input())

ans = 0
start, end = 1, max(ls)

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in ls:
        if i > mid:
            total += mid
        else:
            total += i

    if total <= m:
        ans = mid
        start = mid + 1

    else:
        end = mid - 1
print(ans)