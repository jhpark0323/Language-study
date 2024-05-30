from collections import deque
n, m = map(int, input().split())
ls = list(map(int, input().split()))
q = deque([i for i in range(1, n+1)])

cnt = 0
for target in ls:
    while True:
        # q의 맨 왼쪽 원소가 target과 같으면 popleft
        if q[0] == target:
            q.popleft()
            break

        else:
            if q.index(target) < len(q) / 2:
                while q[0] != target:
                    q.append(q.popleft())
                    cnt += 1

            else:
                while q[0] != target:
                    q.appendleft(q.pop())
                    cnt += 1

print(cnt)