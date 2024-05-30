# 주사위 갯수
n = int(input())
# 주사위 면
dice = [list(map(int, input().split())) for _ in range(n)]

import pprint

'''
위 아래만 고정이고 옆면은 계속 돌릴수 있는듯
-> 마주보는 면 쌍을 찾아야 할듯 (0, 5), (1, 3), (2, 4)
그 후 맨 아래 주사위에서 1, 2, 3번쌍을 위아래에 두고 쭉 만들어보기
이 때 각 쌍에서도 어떤 면을 아래로 하냐에 따라 달라짐
그러므로 총 6개의 경우의수가 나올 수 있다!
'''

'''
아 dictionary로 할걸
'''

# 마주보는 면들끼리 묶어놓음
dice_paired_total = []
for i in dice:
    dice_paired = []
    dice_paired.append([i[0], i[5]])
    dice_paired.append([i[1], i[3]])
    dice_paired.append([i[2], i[4]])
    dice_paired_total.append(dice_paired)

# pprint.pprint(dice_paired_total)


# 맨 아래 주사위면을 고른 후 그와 마주봐서 위아래에 놓일 면들 다른 주사위에서 쭉 삭제
# 옆면만 담긴 list를 만든 후 옆면들 중 제일 큰 숫자를 합해감
def delete(dice_face):
    global dice_paired_total

    # 주사위의 옆면 모임
    dice_side = []
    # 각 주사위들을 순회
    for each_dice in range(n):
        # 첫번째 두번째는 dice_face가 같음 -> 마주보는 두면을 기준으로 함
        if each_dice >= 2:
            # 저번 주사위의 윗면 찾기
            for i in dice_paired_total[each_dice-1]:
                if dice_face in i:
                    # 두개중 dice_face가 아닌게 새로운 dice_face
                    dice_face = [j for j in i if j != dice_face][0]

        # del_dice에 각 주사위에서 dice_face가 없는 것들만 생성
        del_dice = [k for k in dice_paired_total[each_dice] if dice_face not in k]
        dice_side.append(del_dice)

    # pprint.pprint(dice_side)
    max_side = 0
    # 옆면들의 모임을 순회
    for side in dice_side:
        # 각각의 옆면들을 순회
        each_dice_side_max = 0
        for each in side:
            if max(each) > each_dice_side_max:
                each_dice_side_max = max(each)
        # 옆면 중 큰 숫자를 계속 더해줌
        max_side += each_dice_side_max

    # print(max_side)
    return max_side

answer = 0
for i in range(1, 7):
    # print(i)
    if answer < delete(i):
        answer = delete(i)
    # print(delete(i))
print(answer)