import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)

new_arr = [[0] * 3 for _ in range(n)]

for i in range(3):
    new_arr[0][i] = arr[0][i]

# print(new_arr)

for i in range(1, n):
    new_arr[i][0] = min(new_arr[i-1][1], new_arr[i-1][2]) + arr[i][0]
    new_arr[i][1] = min(new_arr[i-1][0], new_arr[i-1][2]) + arr[i][1]
    new_arr[i][2] = min(new_arr[i-1][0], new_arr[i-1][1]) + arr[i][2]

print(min(new_arr[-1]))