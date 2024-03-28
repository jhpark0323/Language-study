import sys
import math

ipt = sys.stdin.readline

arr = [list(map(int, ipt().strip().split())) for _ in range(3)]
# print(arr)


# x1, y1, x2, y2, x3, y3 = arr[0][0], arr[0][1], arr[1][0], arr[1][1], arr[2][0], arr[2][1]
#
# vec_1 = (x1-x2, y1-y2)
# vec_2 = (x3-x2, y3-y2)
#
# # 내적
# inner_product = vec_1[0] * vec_2[0] + vec_1[1] * vec_2[1]
#
# # 내적 = |a|*|b|*cos theta
# length_1 = math.sqrt(vec_1[0]**2 + vec_1[1]**2)
# length_2 = math.sqrt(vec_2[0]**2 + vec_2[1]**2)
#
# # 코사인 값
# cos = inner_product / (length_1 * length_2)
#
# radian = math.acos(cos)
# degree = math.degrees(radian)
# print(degree)

ans = 0
for i in range(len(arr)-1):
    x1, y1 = arr[i][0], arr[i][1]
    x2, y2 = arr[i+1][0], arr[i+1][1]
    ans += x1*y2 - x2*y1

# 마지막 한번 더 해야함 (xn*y1 - x1*yn)
xn, yn = arr[-1][0], arr[-1][1]
x1, y1 = arr[0][0], arr[0][1]
ans += xn*y1 - x1*yn

# print(ans)
if ans > 0:
    print(1)

elif ans == 0:
    print(0)

else:
    print(-1)