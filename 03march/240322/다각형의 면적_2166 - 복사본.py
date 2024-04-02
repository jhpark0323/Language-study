import sys

'''
1사분면을 기준으로 반시계방향을 돌며 순서 정함
'''

ipt = sys.stdin.readline

n = int(ipt())
arr = [list(map(int, ipt().strip().split())) for _ in range(n)]

zero = []
first = []
fir_sec = []
second = []
sec_thi = []
third = []
thi_fou = []
fourth = []
fou_fir = []
for i in arr:
    # 원점
    if i[0] == 0 and i[1] == 0:
        zero.append(i)
    # 1사분면
    elif 0 < i[0] and 0 < i[1]:
        first.append(i)
    # y축 상단
    elif i[0] == 0 and 0 < i[1]:
        fir_sec.append(i)
    # 2사분면
    elif i[0] < 0 and 0 < i[1]:
        second.append(i)
    # x축 하단
    elif i[0] < 0 and i[1] == 0:
        sec_thi.append(i)
    # 3사분면
    elif i[0] < 0 and i[1] < 0:
        third.append(i)
    # y축 하단
    elif i[0] == 0 and i[1] < 0:
        thi_fou.append(i)
    # 4사분면
    elif 0 < i[0] and i[1] < 0:
        fourth.append(i)
    # x축 상단
    elif 0 < i[0] and i[1] == 0:
        fou_fir.append(i)

# 반시계 방향으로 각 ls 정렬
# 1사분면은 y좌표가 작을수록 그다음 x좌표가 클 수록 먼저 나옴
first.sort(key=lambda x: (x[1], -x[0]))
print(first)
second.sort(key=lambda x: (x[0], x[1]))


total_ls = zero + first + fir_sec + second + sec_thi + third + thi_fou + fourth + fou_fir
print(total_ls)