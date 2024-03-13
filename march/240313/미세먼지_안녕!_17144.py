# 입력 처리
R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치 찾기
for i in range(R):
    if room[i][0] == -1:
        air_cleaner = (i, i+1)
        break

# 미세먼지 확산 함수
def spread_dust():
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우, 하, 좌, 상
    new_room = [[0]*C for _ in range(R)] # 확산된 먼지를 임시 저장할 배열
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                spread_amount = 0
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < R and 0 <= ny < C and room[nx][ny] != -1:
                        new_room[nx][ny] += room[i][j] // 5
                        spread_amount += room[i][j] // 5
                room[i][j] -= spread_amount
    for i in range(R):
        for j in range(C):
            room[i][j] += new_room[i][j]

# 공기청정기 작동 함수
def operate_air_cleaner():
    upper, lower = air_cleaner
    # 위쪽 공기청정기
    for i in range(upper-1, 0, -1):
        room[i][0] = room[i-1][0]
    for i in range(C-1):
        room[0][i] = room[0][i+1]
    for i in range(upper):
        room[i][C-1] = room[i+1][C-1]
    for i in range(C-1, 1, -1):
        room[upper][i] = room[upper][i-1]
    room[upper][1] = 0
    # 아래쪽 공기청정기
    for i in range(lower+1, R-1):
        room[i][0] = room[i+1][0]
    for i in range(C-1):
        room[R-1][i] = room[R-1][i+1]
    for i in range(R-2, lower-1, -1):
        room[i+1][C-1] = room[i][C-1]
    for i in range(C-1, 1, -1):
        room[lower][i] = room[lower][i-1]
    room[lower][1] = 0

# T초 동안 시뮬레이션 실행
for _ in range(T):
    spread_dust()
    operate_air_cleaner()

# 미세먼지 총량 계산
answer = sum(map(sum, room)) + 2
print(answer)
