import math
import sys

input = sys.stdin.readline

n = int(input())
left = list(map(int, input().split()))
plan = list(map(int, input().split()))

ans = 0

arr = []
for i, j in zip(left, plan):
    arr.append([i, j])

# print(arr)

# 계획일을 기준으로 정렬, 그 후 남은 기간 순으로 정렬
arr = sorted(arr, key=lambda x: (x[1], x[0]))

# print(arr)

# 구간의 최댓값
max_ = arr[0][0]
# 구간의 기준
standard = arr[0][1]

cnt = 0
for i in range(n):
    if standard > arr[i][0]:
        tmp = math.ceil((standard - arr[i][0]) / 30)
        cnt += tmp
        arr[i][0] += tmp * 30

    max_ = max(max_, arr[i][0])

    # 다음 계획일의 구간의 값이 달라지면 구간 기준점 재정의
    if i+1 < n and arr[i][1] != arr[i+1][1]:
        standard = max(max_, arr[i+1][1])

print(cnt)