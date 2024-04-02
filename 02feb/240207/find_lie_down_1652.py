import pprint

n = int(input())
# ls에 str값을 그대로 input받아 1차원 list를 만듬
ls = [input() for _ in range(n)]

# bed에는 ls의 각 원소들을 X를 기준으로 split해서 2차원 list로 만듬
bed = []
for i in ls:
    bed.append(i.split('X'))


# print(ls)    # ['....X', '..XX.', '.....', '.XX..', 'X....']
# print(bed)    # [['....', ''], ['..', '', '.'], ['.....'], ['.', '', '..'], ['', '....']]

# 가로
cnt_garo = 0
for i in bed:
    # bed의 각원소(list)들을 순회하는데 하나씩 pop해서 길이가 2보다 크면 cnt += 1
    # pop해서 다 뽑으면 끝
    while i:
        if len(i.pop()) >= 2:
            cnt_garo += 1
# print(cnt_garo)

# 세로
# bed를 전치 시켜서 가로랑 같은 방법 이용
ls_t = []
# 0~n까지 순회
for i in range(n):
    word = ''
    # ls의 i번째 글자들만 모아서 word에 대입
    for j in ls:
        word += j[i]
    ls_t.append(word)

# pprint.pprint(bed_t)

bed_t = []
for i in ls_t:
    bed_t.append(i.split('X'))

cnt_sero = 0
for i in bed_t:
    while i:
        if len(i.pop()) >= 2:
            cnt_sero += 1
# print(cnt_sero)

print(cnt_garo, cnt_sero)