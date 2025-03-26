alpha = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'D' : 4,
    'E' : 5,
    'F' : 6
}

ls = [input() for _ in range(36)]
# 겹치는게 하나라도 있으면 안됨
if len(set(ls)) < 36:
    print('Invalid')

# 안겹친다는 가정 하에
else:
    # 맨 마지막에 첫번째 원소를 추가하면서 다시 원점으로 돌아올수 있는지 파악
    ls.append(ls[0])
    # print(ls)

    cnt = 0
    # 37개의 list에서 두개씩 각각 비교 할 것이므로 36번 반복
    for i in range(36):
        # 첫번째, 두번째
        first, second = ls[i], ls[i+1]

        # 첫번째와 두번쨰의 x, y좌표를 구함
        first_x, first_y = alpha[first[0]], int(first[1])
        second_x, second_y = alpha[second[0]], int(second[1])

        # print(first_x, first_y)
        # print(second_x, second_y)

        # x좌표를 기준으로 한칸 차이 날 때
        if abs(first_x - second_x) == 1:
            # y좌표가 두칸 차이나면 성공
            if abs(first_y - second_y) == 2:
                cnt += 1

        # x좌표를 기준으로 두칸 차이 날 때
        if abs(first_x - second_x) == 2:
            # y좌표가 한칸 차이나면 성공
            if abs(first_y - second_y) == 1:
                cnt += 1
    # print(cnt)

    if cnt == 36:
        print('Valid')

    else:
        print('Invalid')