import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
ls = list(map(int, input().split()))
# print(ls)

ls.sort()
ls = deque(ls)

# 짝수이면
if n % 2 == 0:
    max_val = 0

# 홀수이면
else:
    # 맨 마지막꺼 하나 빼서 max 값으로 둠
    max_val = ls.pop()

while ls:
    first, last = ls.popleft(), ls.pop()
    val = first + last
    if max_val < val:
        max_val = val

print(max_val)