# 가로, 세로
full_width, full_length = map(int, input().split())

# 잘라야하는 점선의 갯수
n = int(input())

# 가로로 자르면 arr[i] : 0, 세로로 자르면 arr[i] : 1
arr_width = []
arr_length = []
for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:
        arr_length.append(a[1])
    else:
        arr_width.append(a[1])

arr_width.sort()
arr_length.sort()

# print(arr_width, arr_length)

width = [0] * (full_width)
length = [0] * (full_length)

# arr_width을 거꾸로 순회
for i in range(len(arr_width)-1, -1, -1):
    # 뒤에서부터 순회해서 1을 그 index에 넣음
    width.insert(arr_width[i], 1)

# arr_length를 거꾸로 순회
for i in range(len(arr_length)-1, -1, -1):
    # 뒤에서부터 순회해서 1을 그 index에 넣음
    length.insert(arr_length[i], 1)

# print(width, length)

# 1 사이의 0들 만큼 길이가 나옴
max_cnt_w = 0
cnt_w = 0
for i in range(len(width)):
    # 0이면 cnt_w에 1씩더함
    if width[i] == 0:
        cnt_w += 1
    # 1이면
    else:
        # max값 확인
        if max_cnt_w < cnt_w:
            max_cnt_w = cnt_w
        # cnt_w 초기화
        cnt_w = 0
    # 끝까지 돌았을 때 max값 확인
    if i == len(width)-1:
        if max_cnt_w < cnt_w:
            max_cnt_w = cnt_w

# 1 사이의 0들 만큼 길이가 나옴
max_cnt_l = 0
cnt_l = 0
for i in range(len(length)):
    # 0이면 cnt_l에 1씩 더함
    if length[i] == 0:
        cnt_l += 1
    # 1이면
    else:
        # max값 확인
        if max_cnt_l < cnt_l:
            max_cnt_l = cnt_l
        # cnt_l 초기화
        cnt_l = 0
    # 끝까지 돌았을 때 max값 확인
    if i == len(length)-1:
        if max_cnt_l < cnt_l:
            max_cnt_l = cnt_l

print(max_cnt_w * max_cnt_l)