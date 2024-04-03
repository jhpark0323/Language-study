import sys
from itertools import combinations
from collections import deque

'''
궁수들을 세울수있는 모든 경우의 수를 다 찾음
궁수의 위치 바로 윗칸 (arr의 마지막줄)을 기준으로 시작
-> 대신 거리 1 먹고시작
'''

input = sys.stdin.readline

# delta탐색인데 좌 상 우 순서로 돔
di = [0, -1, 0]
dj = [-1, 0, 1]

n, m, d = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
# print(arr)

p = [i for i in range(n)]
combi = list(combinations(p, 3))
# print(combi)

# 적의 갯수
enemy = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            enemy += 1

ans_ls = []
# 모든 경우를 순회
for each in combi:
    start1, start2, start3 = each[0], each[1], each[2]
    print('start1 :', start1)
    print('start2 :', start2)
    print('start3 :', start3)

    ans = 0

    while True:
        enemy1_row, enemy1_col = False, False
        enemy2_row, enemy2_col = False, False
        enemy3_row, enemy3_col = False, False

        # 시작시 거리1을 먹고 시작함
        # 시작 row, col, 거리
        GameOver = False
        q1 = deque([[n-1, start1, 1]])
        while q1:
            current_row, current_col, dist = q1.popleft()

            # 1이면 바로 반환
            if arr[current_row][current_col] == 1:
                # 없앨 적의 위치 확인
                enemy1_row, enemy1_col = current_row, current_col
                print(enemy1_row, enemy1_col)
                # 더이상 할 필요 없음
                GameOver = True
                break

            if GameOver:
                break

            # 갈수있는방향
            for dij in range(3):
                next_row = current_row + di[dij]
                next_col = current_col + dj[dij]

                # 배열안에 있으면
                if 0 <= next_row < n and 0 <= next_col < m:
                    # 1이면 바로 반환
                    if arr[next_row][next_col] == 1:
                        pass
                    # 0이면
                    else:
                        # 거리가 아직 안됬으면
                        # 그 위치를 다시 q에 담음
                        if dist + 1 <= d:
                            q1.append([next_row, next_col, dist + 1])

        # 시작시 거리1을 먹고 시작함
        # 시작 row, col, 거리
        GameOver = False
        q2 = deque([[n-1, start2, 1]])
        while q2:
            current_row, current_col, dist = q2.popleft()

            # 1이면 바로 반환
            if arr[current_row][current_col] == 1:
                # 없앨 적의 위치 확인
                enemy2_row, enemy2_col = current_row, current_col
                # 더이상 할 필요 없음
                GameOver = True
                break

            if GameOver:
                break

            # 갈수있는방향
            for dij in range(3):
                next_row = current_row + di[dij]
                next_col = current_col + dj[dij]

                # 배열안에 있으면
                if 0 <= next_row < n and 0 <= next_col < m:
                    # 1이면 바로 반환
                    if arr[next_row][next_col] == 1:
                        pass

                    # 0이면
                    else:
                        # 거리가 아직 안됬으면
                        # 그 위치를 다시 q에 담음
                        if dist + 1 <= d:
                            q2.append([next_row, next_col, dist + 1])


        # 시작시 거리1을 먹고 시작함
        # 시작 row, col, 거리
        GameOver = False
        q3 = deque([[n-1, start3, 1]])
        while q3:
            current_row, current_col, dist = q3.popleft()

            # 1이면 바로 반환
            if arr[current_row][current_col] == 1:
                # 없앨 적의 위치 확인
                enemy3_row, enemy3_col = current_row, current_col
                # 더이상 할 필요 없음
                GameOver = True
                break

            if GameOver:
                break

            # 갈수있는방향
            for dij in range(3):
                next_row = current_row + di[dij]
                next_col = current_col + dj[dij]

                # 배열안에 있으면
                if 0 <= next_row < n and 0 <= next_col < m:
                    # 1이면 바로 반환
                    if arr[next_row][next_col] == 1:
                        pass
                    # 0이면
                    else:
                        # 거리가 아직 안됬으면
                        # 그 위치를 다시 q에 담음
                        if dist + 1 <= d:
                            q3.append([next_row, next_col, dist + 1])

        # enemy1_row가 존재하고 그 위치에 적이 있으면
        if enemy1_row and arr[enemy1_row][enemy1_col]:
            print(enemy1_row)
            arr[enemy1_row][enemy1_col] = 0
            ans += 1

        if enemy2_row and arr[enemy2_row][enemy2_col]:
            arr[enemy2_row][enemy2_col] = 0
            ans += 1

        if enemy3_row and arr[enemy3_row][enemy3_col]:
            arr[enemy3_row][enemy3_col] = 0
            ans += 1

        # 적의 갯수
        enemy_left = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    enemy_left += 1
        # print(enemy_left)


        n -= 1

        ans_ls.append(ans)

        # 남은 적이 없으면 나와라
        if not enemy_left:
            break

print(ans_ls)