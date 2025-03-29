import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input().strip()) for _ in range(n)]

def check(num):
    a = 0
    for i in range(n):
        if arr[i] > num:
            continue
        a += num - arr[i]

    if k >= a:
        return True

    return False

left = min(arr)
right = 2000000000

while left <= right:
    mid = (left + right) // 2

    if check(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right)