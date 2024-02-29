import sys
from collections import deque

n = int(input())
arr = [list(sys.stdin.readline().strip().split()) for _ in range(n)]
# print(arr)

q = deque([])
# print(q)
for i in arr:
    if i[0] == 'push':
        num = i[1]
        q.append(num)

    elif i[0] == 'pop':
        # 안에 들어 있으면
        if q:
            # 맨앞의 수 출력
            print(q.popleft())
        # 없으면 -1 출력
        else:
            print(-1)

    elif i[0] == 'size':
        print(len(q))

    elif i[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)

    elif i[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)

    else:
        if q:
            print(q[-1])
        else:
            print(-1)