import pprint

# 가로, 세로
x, y = map(int, input().split())

# 상점 수
n = int(input())

# 상점들 + 동근이 위치
arr = [list(map(int, input().split())) for _ in range(n)]

# 동근이의 위치
dong = list(map(int, input().split()))

# print(arr)
# print(dong)

# 동근이의 방향, 거리
dong_directions, dong_distance = dong[0], dong[1]
# print(dong_directions, dong_distance)

# 동근이가 북쪽에 있을 때
if dong_directions == 1:
    # 동근이의 x, y좌표
    dong_x, dong_y = dong_distance, y
# 남쪽
elif dong_directions == 2:
    # 동근이의 x, y좌표
    dong_x, dong_y = dong_distance, 0
# 서쪽
elif dong_directions == 3:
    # 동근이의 x, y좌표
    dong_x, dong_y = 0, y - dong_distance
# 동쪽
elif dong_directions == 4:
    # 동근이의 x, y좌표
    dong_x, dong_y = x, y - dong_distance

# print(dong_x, dong_y)
total = 0

for i in arr:
    # 방향, 거리
    directions, distance = i[0], i[1]
    # 북쪽
    if directions == 1:
        # x, y좌표
        shop_x, shop_y = distance, y
    # 남쪽
    elif directions == 2:
        # x, y좌표
        shop_x, shop_y = distance, 0
    # 서쪽
    elif directions == 3:
        # x, y좌표
        shop_x, shop_y = 0, y - distance
    # 동쪽
    elif directions == 4:
        # x, y좌표
        shop_x, shop_y = x, y - distance

    # print(shop_x, shop_y)

    # ---------- 여기 까지 각상점의 좌표가 나옴 ---------------------------

    # 둘이 남북쪽의 평행한 곳에 있으면
    if dong_directions in [1, 2] and directions in [1, 2]:
        # 그중 둘이 같으면
        if dong_directions == directions:
            answer = abs(dong_x - shop_x)
        # 둘이 다르면 -> 평행하면
        else:
            answer1 = dong_x + shop_x + y
            answer2 = 2*(x+y) - answer1
            answer = min(answer1, answer2)

    # 둘이 동서쪽에 평행한 곳에 있으면
    elif dong_directions in [3, 4] and directions in [3, 4]:
        # 그중 둘이 같으면
        if dong_directions == directions:
            answer = abs(dong_y - shop_y)
        # 둘이 다르면 -> 평행하면
        else:
            answer1 = dong_y + shop_y + x
            answer2 = 2*(x+y) - answer1
            answer = min(answer1, answer2)

    # 둘이 평행하지 않으면
    else:
        # 서, 남
        if dong_directions in [2, 3] and directions in [2, 3]:
            # 각 좌표값중 distance가 아닌것은 0이기 때문에
            answer = dong_x + dong_y + shop_x + shop_y
        # 남, 동
        elif dong_directions in [2, 4] and directions in [2, 4]:
            # 종이에 그려보면 왜 이런지 나옴 글로 설명을 못하겠음
            if dong_y == 0:
                answer = x - dong_x + shop_y
            else:
                answer = x - shop_x + dong_y
        # 북, 동
        elif dong_directions in [1, 4] and directions in [1, 4]:
            # 종이에 그려보면 왜 이런지 나옴 글로 설명을 못하겠음
            answer = 2*(x+y) - (dong_x + dong_y + shop_x + shop_y)
        # 북, 서
        else:
            # 종이에 그려보면 왜 이런지 나옴 글로 설명을 못하겠음
            if dong_x == 0:
                answer = shop_x + y - dong_y
            else:
                answer = dong_x + y - shop_y

    total += answer

print(total)