import sys
import math
from itertools import combinations

# 각도 구하는 함수
def angle(x1, y1, x2, y2):
    a = x1 - x2
    b = y1 - y2
    # 각도를 구함
    return math.degrees(math.atan2(b, a))


'''
50C2 = 1225 가능할듯
두 빌딩의 꼭대기를 기준으로 각도를 구함
각도가 음수다? -> 자기보다 아래에 있음
각도가 양수다? -> 자기보다 고층임
본인을 기준으로 좌, 우도 구분
'''

ipt = sys.stdin.readline
n = int(ipt())
ls = list(map(int, ipt().strip().split()))
# print(ls)

# 좌표를 만들어줌
new_ls = []
for i in range(n):
    new_ls.append((i+1, ls[i]))
print(new_ls)

# p = [i for i in range(n)]
#
# combi = list(combinations(p, 2))
# print(combi)

new_dict = {}

for i in range(n):
    val_ls = []
    for j in range(n):
        # # 높이가 더 높은 것을 먼저 둠
        # if ls[i] > ls[j]:
        #     x1, y1, x2, y2 = new_ls[i][0], new_ls[i][1], new_ls[j][0], new_ls[j][1]
        #
        # else:
        #     x1, y1, x2, y2 = new_ls[j][0], new_ls[j][1], new_ls[i][0], new_ls[i][1]

        # 뒤에서 앞을 기준으로 잼
        # 본인보다 고층 빌딩을 봐야하기 때문
        x1, y1, x2, y2 = new_ls[j][0], new_ls[j][1], new_ls[i][0], new_ls[i][1]

        val_ls.append(angle(x1, y1, x2, y2))
    new_dict[new_ls[i]] = val_ls

# print(new_dict)

# 빌딩 순회
max_cnt = 0
idx = 0
for standard in range(n):
    building = new_dict[new_ls[i]]
    # 왼쪽 최소값 -> 왼쪽은 90도를 넘기 때문에 각도가 작을 수록 높음
    min_l = float('inf')
    # 오른쪽 최댓값
    max_r = 0
    cnt = 0
    for j in range(n-1, -1, -1):
        # index가 기준보다 왼쪽에 있으면
        if j < standard:
            if min_l >= building[j]:
                if min_l > building[j]:
                    cnt += 1
                # 갱신
                min_l = building[j]


    for j in range(n):
        # # index가 기준보다 왼쪽에 있으면
        # if j < standard:
        #     # 왼쪽 최솟값 갱신
        #     if min_l >= building[j]:
        #         min_l = building[j]
        #
        #     # 최댓값이 갱신되지 않으면 cnt 하나 증가
        #     else:
        #         cnt += 1
        # index가 기준보다 오른쪽이면
        if standard < j:
            if max_r <= building[j]:
                # 여기서는 최댓값 갱신시마다 cnt 1씩 더해줌
                # 같을 때는 접하기 때문에 하나 더 올리지 않음
                if max_r < building[j]:
                    cnt += 1
                # 갱신
                max_r = building[j]

    if max_cnt < cnt:
        max_cnt = cnt
        idx = standard

print(new_dict[(6, 3)])
print(max_cnt, idx)