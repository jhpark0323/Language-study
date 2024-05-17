import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp_max = arr
dp_min = arr

for i in range(n-1):
    arr = list(map(int, input().split()))

    dp_max = [max(dp_max[0], dp_max[1]) + arr[0], max(dp_max) + arr[1], max(dp_max[1], dp_max[2]) + arr[2]]
    dp_min = [min(dp_min[0], dp_min[1]) + arr[0], min(dp_min) + arr[1], min(dp_min[1], dp_min[2]) + arr[2]]

print(max(dp_max), min(dp_min))