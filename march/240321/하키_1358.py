import sys
import math

def find(row, col):
    # 사각형의 범위 안에 있으면
    if x <= row <= x+w and y <= col <= y+h:
        return 1
    # 그림 기준 왼쪽 원 안에 있음
    d = math.sqrt((x - row)**2 + (y + h//2 - col)**2)
    if d <= h//2:
        return 1

    # 그림 기준 오른쪽 원 안에 있음
    d = math.sqrt((x+w-row)**2 + (y+h//2 - col)**2)
    if d <= h//2:
        return 1

    return 0

ipt = sys.stdin.readline

w, h, x, y, p = map(int, ipt().strip().split())
arr = [list(map(int, ipt().strip().split())) for _ in range(p)]

cnt = 0
for i in arr:
    row, col = i[0], i[1]
    cnt += find(row, col)

print(cnt)