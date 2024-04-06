import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
print(arr)

answer_1 = []
answer_2 = []
answer_3 = []

for i in arr:
    if i[1]