import pprint

# 색종이의 장수
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

plane = [[0] * 1001 for _ in range(1001)]

# arr을 순회
for i in range(n):
    # x, y 좌표
    x, y = arr[i][0], arr[i][1]
    # 너비, 높이
    dx, dy = arr[i][2], arr[i][3]
    # plane에 덮을 숫자
    num = i + 1
    for xx in range(x, x+dx):
        for yy in range(y, y+dy):
            plane[xx][yy] = num

# pprint.pprint(plane)

for paper in range(1, n+1):
    answer = 0
    for i in range(1001):
        for j in range(1001):
            if plane[i][j] == paper:
                answer += 1
    print(answer)