import sys
input = sys.stdin.readline
n = int(input())
ls = [int(input()) for _ in range(n)]
# print(ls)

ls.sort()

score = 0
for i in range(n):
    score += abs(i+1 - ls[i])

print(score)