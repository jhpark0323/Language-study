import sys
import math
from decimal import Decimal, ROUND_HALF_UP

'''
1사분면을 기준으로 반시계방향을 돌며 순서 정함
정렬 후 대각선 공식으로 넓이 구하기
'''

ipt = sys.stdin.readline

n = int(ipt())
arr = [list(map(int, ipt().strip().split())) for _ in range(n)]

# 라디안 -> 각도를 만들어 ls에 append
ls = []
for i in arr:
    x, y = i[0], i[1]
    radian = math.atan2(y, x)
    degree = math.degrees(radian)
    # if degree < 0:
    #     degree += 360
    ls.append((x, y, degree))
# print(ls)

# # 중복제거
# ls = list(set(ls))
# # 각도가 작은 순으로 정렬, 각도가 같으면 길이가 짧은거 순서로
# ls.sort(key=lambda x: (x[2], math.sqrt(x[0]**2 + x[1]**2)))
# # print(ls)

ans = 0
for i in range(len(ls)-1):
    x1, y1 = ls[i][0], ls[i][1]
    x2, y2 = ls[i+1][0], ls[i+1][1]
    ans += x1*y2 - x2*y1

# 마지막 한번 더 해야함 (xn*y1 - x1*yn)
xn, yn = ls[-1][0], ls[-1][1]
x1, y1 = ls[0][0], ls[0][1]
ans += xn*y1 - x1*yn

# answer = abs(ans) / 2
# print(round(answer, 1))

answer = Decimal(str(abs(ans) / 2))
rounded_number = answer.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
print(rounded_number)
