import sys
from collections import  deque

input = sys.stdin.readline
n = int(input().strip())

ls_1 = deque([input().strip() for _ in range(n)])
ls_2 = deque([input().strip() for _ in range(n)])
# print(ls_1)
# print(ls_2)

cnt = 0
while ls_2:
    out = ls_2.popleft()

    for i in range(len(ls_1)):
        # 나간 차와 남은차 중에서 맨앞에 들어온차가 같으면
        if out == ls_1[i]:
            # 없앰
            ls_1.remove(ls_1[i])
            if i == 0:
                pass
            else:
                cnt += 1
            break
print(cnt)