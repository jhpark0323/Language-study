import sys

input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))

def f(antenna):
    global ans
    global min_distance
    distance = 0
    for i in ls:
        # 거리는 i-antenna의 절댓값
        distance += abs(i-antenna)
        if distance >= min_distance:
            return

    if min_distance > distance:
        min_distance = distance
        ans = antenna

min_distance = float('inf')
ans = 0
# 안테나의 위치를 순회

ls.sort()
new_ls = ls[n//2-1:n//2+1]

for antenna in new_ls:
    f(antenna)
# print(min_distance)
print(ans)