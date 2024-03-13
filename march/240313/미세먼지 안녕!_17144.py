from pprint import pprint

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
# pprint(arr)


# 우상좌하
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

# 공기청정기의 윗부분 위치
air_cleaner = 0
# 공기청정기 위치 찾기
for i in range(r):
    if arr[i][0] == -1:
        air_cleaner = i
        break


# t초가 지난 후를 구하기 위해 t초간 순회
for time in range(t):
    # 확산 된 만큼의
    diffusion = [[0] * c for _ in range(r)]
    # 1. 미세먼지 확산
    for i in range(r):
        for j in range(c):
            # -1과 0이 아니면
            # 5보다 작으면 확산이 안됨
            if arr[i][j] >= 5:
                # 확산 되는 양은 무조건 5로 나눈 몫
                spread = arr[i][j] // 5
                # 주위 4곳을 순회후 확산
                for k in range(4):
                    nr = i+di[k]
                    nc = j+dj[k]

                    # print('nr :', nr)
                    # print('nc :', nc)
                    # print(r, c)
                    # pprint(arr)

                    # 범위안에 있고 공기청정기가 없으면 (-1이 아니면)
                    if 0 <= nr < r and 0 <= nc < c and arr[nr][nc] != -1:
                        # diffusion에 확산되는 양만큼 더해주고
                        diffusion[nr][nc] += spread
                        # 본인 자리는 그만큼 뺴줌
                        arr[i][j] -= spread

    # 확산된 배열을 본 배열에 더해줌
    for i in range(r):
        for j in range(c):
            # arr에 확산된만큼을 저장한 배열을 더해줌
            arr[i][j] += diffusion[i][j]
    # 성공한듯? 1번 테케랑 같음
    # pprint(arr)

    # 2. 공기 청정기 작동
    # 위쪽구간
    # 한바퀴 도는 구간을 do_it으로 만듬
    do_it = arr[air_cleaner] + [arr[i][-1] for i in range(air_cleaner-1, 0, -1)] + arr[0][::-1] + [arr[i][0] for i in range(1, air_cleaner)]
    # print(do_it)

    do_it = do_it[-1:] + do_it[:-1]
    # 공기 청정기의 위치와 그 바로 다음칸은 변동없이 항상 -1과 0임
    do_it[0] = -1
    do_it[1] = 0
    # print(do_it)

    arr[air_cleaner] = do_it[:c]
    # print(arr[air_cleaner])

    j = 0
    for i in range(air_cleaner-1, 0, -1):
        arr[i][c-1] = do_it[c+j]
        j += 1
    arr[0] = do_it[c+j:2*c+j][::-1]

    plus_1 = 0
    for i in range(1, air_cleaner-1):
        arr[i][0] = do_it[2*c+j+plus_1]
        plus_1 += 1

    # pprint(arr)

    # 아래쪽구간
    # 한바퀴 도는 구간을 do_it으로 만듬
    # print(air_cleaner)
    # print(arr[air_cleaner+1])
    # print([arr[i][c - 1] for i in range(air_cleaner+2, r-1)])
    do_it_under = arr[air_cleaner+1] + [arr[i][-1] for i in range(air_cleaner+2, r-1)] + arr[r-1][::-1] + [arr[i][0] for i in range(r-2, air_cleaner+1, -1)]
    # print(do_it_under)
    do_it_under = do_it_under[-1:] + do_it_under[:-1]
    # 공기 청정기의 위치와 그 바로 다음칸은 변동없이 항상 -1과 0임
    do_it_under[0] = -1
    do_it_under[1] = 0
    # print(do_it_under)

    arr[air_cleaner+1] = do_it_under[:c]
    j = 0
    for i in range(air_cleaner+2, r-1):
        arr[i][c - 1] = do_it_under[c + j]
        j += 1
    arr[r-1] = do_it_under[c+j:2*c+j][::-1]

    plus = 0
    for i in range(r-2, air_cleaner+1, -1):
        arr[i][0] = do_it_under[2*c + j + plus]
        plus += 1

    # pprint(arr)
    # print()

answer = 0
for i in arr:
    answer += sum(i)

# 공기청정기는 무조건 2칸이고 1칸당 -1을 가지고 있기에 마지막에 2를 더해줌
print(answer+2)