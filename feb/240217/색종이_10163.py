'''
arr을 거꾸로 순회하여 visited를 활용해 방문한곳은 칠하지 않는다
-> arr돌리면서 바로 센다
'''

import pprint

# 색종이의 장수
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

plane = [[0] * 1001 for _ in range(1001)]
visited = [[False] * 1001 for _ in range(1001)]
answer_ls = []

# arr을 순회
for i in range(n-1, -1, -1):
    # x, y 좌표
    x, y = arr[i][0], arr[i][1]
    # 너비, 높이
    dx, dy = arr[i][2], arr[i][3]
    # answer 초기화
    answer = 0
    for xx in range(x, x+dx):
        for yy in range(y, y+dy):
            # 방문하지 않은 곳이면 answer += 1
            if not visited[xx][yy]:
                visited[xx][yy] = True
                answer += 1
    answer_ls.append(answer)

for i in range(n-1, -1, -1):
    print(answer_ls[i])
