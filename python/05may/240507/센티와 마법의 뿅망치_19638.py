from heapq import heappop, heappush, heapify
import sys
input = sys.stdin.readline
n, h, t = map(int, input().split())
arr = [-int(input()) for _ in range(n)]
# print(arr)

heapify(arr)
# print(arr)

cnt = 0
# 횟수만큼 반복
for i in range(t):
    biggest = heappop(arr)
    # 키가 1이면 더이상 안줄어듬
    if biggest == -1:
        heappush(arr, -1)

    # 제일 큰 길이가 센티의 키보다 작다면
    elif -biggest < h:
        print('YES')
        print(cnt)
        exit()

    # 제일 큰 길이가 센티의 키보다 크다면
    else:
        heappush(arr, -(-biggest // 2))
        cnt += 1

# 마지막까지 돌았음
else:
    # 마지막 검사
    biggest = heappop(arr)

    # 제일 큰 길이가 센티의 키보다 작다면
    if -biggest < h:
        print('YES')
        print(cnt)
        exit()

    else:
        print('NO')
        print(-biggest)