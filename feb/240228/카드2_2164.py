from collections import deque

n = int(input())

p = deque([i for i in range(1, n+1)])
# print(p)

while len(p) != 1:
    # 먼저 한장 버린다
    p.popleft()
    # 다음 장은 꺼내서 맨뒤에 넣는다
    next = p.popleft()
    p.append(next)

print(p.popleft())