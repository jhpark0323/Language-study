import sys
from itertools import permutations

ipt = sys.stdin.readline
n = int(ipt())
arr = [list(map(int, ipt().split())) for _ in range(n)]
# print(arr)

p = [i for i in range(1, 9)]

# 나중에 할 때 index 3번 자리에 첫번째 선수 넣기(4번타자)
# # 이거하면 시간 너무 오래 걸림
# for order_except_4 in per:
#     order = list(order_except_4[:3]) + [3] + list(order_except_4[3:])
#     print(order)

def f(start, order):
    global score
    # base의 갯수
    # 0 : 홈, # : #루
    base = [0] * 4

    out = 0
    # 3아웃 될 때 까지
    while out != 3:
        # 타자
        hitter = order[start]
        # 친 결과
        hit = arr[innings][hitter]

        # 쳤으면
        if hit:
            # 모든 베이스를 뒤에서 부터 순회
            for i in range(3, 0, -1):
                # base에 사람이 있으면
                if base[i]:
                    # 친만큼 base 옮김
                    new = i + hit
                    # 만약 base가 4보다 커지면
                    if new >= 4:
                        # 점수 1씩 올림
                        score += 1
                        # base에서 주자 삭제
                        base[i] = 0
                    # 옮긴 base가 4보다 작으면
                    else:
                        # 그자리에 주자 추가
                        base[new] = 1
                        # 원래자리 주자 삭제
                        base[i] = 0
                    # # 만약 hit와 i가 같다면
                    # # 주자 놓기
                    # if hit == i:
                    #     base[i] = 1

                if hit == i:
                    base[i] = 1
                # # 만약base에 주자가 없으면
                # else:
                #     # 만약 hit와 i가 같다면
                #     # 주자 놓기
                #     if hit == i:
                #         base[i] = 1
        # 못쳤으면
        else:
            out += 1

        if hit == 4:
            score += 1

        # 다음 타석
        start = (start + 1) % 9

    # 순회가 끝난 후 주자가 어디서 끝났는지 알아야 함
    return start

max_score = 0
# 모든 경우의수 순회
for case in permutations(p, 8):
    order = list(case[:3]) + [0] + list(case[3:])

    # 첫 이닝 시작은 맨 처음 사람 부터
    start = 0
    # 점수
    score = 0
    # 이닝 수 만큼 순회
    for innings in range(n):
        # 다음 타석 까지 가져옴
        start = f(start, order)

    if max_score < score:
        max_score = score
print(max_score)