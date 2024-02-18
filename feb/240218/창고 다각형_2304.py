import pprint

'''
먼저 기둥을 1로 다 채워 놓고 시작
그 후 아래에서부터 처음과 끝 1을 확인 후 다 칠하기?
'''

# 기둥의 개수
n = int(input())
# 기둥 list
gidung = [list(map(int, input().split())) for _ in range(n)]


# 가로세로 최댓값 찾기
max_x = 0
max_y = 0
for i in gidung:
    x, y = i[0], i[1]
    if max_x < x:
        max_x = x
    if max_y < y:
        max_y = y

# print(max_x, max_y)

# max_x, max_y 만큼의 창고를 만듬 -> 이 때 row, col이랑 x, y랑 헷갈릴거 같아서 그냥 x, y로 통일
# -> 아마 그림 자체는 위아래가 뒤집어서 나올듯
storage = [[0] * (max_x+1) for _ in range(max_y)]

# pprint.pprint(storage)

for i in gidung:
    x, y = i[0], i[1]
    for dy in range(y):
        # x, y 안헷갈리게 조심
        storage[dy][x] = 1

# pprint.pprint(storage)

answer = 0
# 처음과 끝에있는 1 찾기
for i in storage:
    # 시작 idx는 바로 찾기
    start_idx = i.index(1)
    # 끝 idx는 뒤집어서 찾기
    i = i[::-1]
    end_idx = max_x - i.index(1)
    # 끝 - 처음 + 1 이 그 행에서의 1이 채워진 갯수
    answer += end_idx - start_idx + 1
    # print(start_idx, end_idx)
print(answer)